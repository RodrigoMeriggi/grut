#!/usr/bin/env python3
"""Genera páginas estáticas rastreables (colecciones y productos) y sitemap.xml
a partir del array `products` de index.html. Volver a correr después de cada colección nueva:

    python3 tools/build_seo.py
"""
import datetime, html, json, os, re, shutil, subprocess, unicodedata

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE = "https://rodrigomeriggi.github.io/grut/"
TODAY = datetime.date.today().isoformat()
EXCLUDED_CATS = {"WATCHES"}  # piezas de terceros (GRUT no las fabrica): sin página ni Product schema

LABELS = {"DAY": "Day", "NIGHT": "Night", "RESORT": "Resort", "ESSENTIALS": "Essentials",
          "COCKTAIL": "Cocktail", "WINTER": "Winter", "FOOTWEAR": "Calzado", "WATCHES": "Relojes"}
GENDER = {"W": "Mujer", "M": "Hombre", "U": "Unisex"}

src = open(os.path.join(ROOT, "index.html"), encoding="utf-8").read()
start = src.index("const products=[") + len("const products=")
end = src.index("];let gender", start) + 1
products = json.loads(subprocess.run(
    ["node", "-e", "process.stdout.write(JSON.stringify(" + src[start:end] + "))"],
    capture_output=True, text=True, check=True).stdout)

for k, v in re.findall(r"c==='(\w+)'\?(?:'([^']*)'|\"[^\"]*\")", src):
    LABELS.setdefault(k, v)
LABELS["GENTLEMAN"] = "Gentleman's Club"


def slug(s):
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z0-9]+", "-", s).strip("-")


def intro(cat):
    k = src.find("class=\"small-link\" onclick=\"filter('%s')\"" % cat)
    if k < 0:
        return ""
    sec = src[src.rfind("<section", 0, k):k]
    ps = re.findall(r"<p[^>]*>(.*?)</p>", sec, re.S)
    if not ps:
        return ""
    t = html.unescape(re.sub(r"<[^>]+>", "", ps[-1])).strip()
    return re.sub(r"\s*Tocá (la|una) imagen[^.]*\.", "", t).strip()


def esc(s):
    return html.escape(s, quote=True)


def usd(n):
    return f"{n:,}".replace(",", ".")


def cls(p):
    return 'class="c" ' if p.get("accessory") else ""


def img_url(p):
    return BASE + "assets/" + p["img"]


CSS = """*{box-sizing:border-box}body{margin:0;background:#f6f3ed;color:#1f1b16;font-family:'DM Sans',system-ui,sans-serif;font-weight:300;line-height:1.6}
a{color:inherit}header,main,footer{max-width:1180px;margin:0 auto;padding:24px}header{display:flex;justify-content:space-between;align-items:center;border-bottom:1px solid #e2dbcf}
.logo{font-family:Italiana,serif;font-size:30px;letter-spacing:.18em;text-decoration:none}.logo small{display:block;font-family:'DM Sans';font-size:9px;letter-spacing:.4em}
h1,h2{font-family:Italiana,serif;font-weight:400;letter-spacing:.04em}h1{font-size:clamp(36px,6vw,64px);margin:.2em 0}.eyebrow{font-size:11px;letter-spacing:.25em;text-transform:uppercase;color:#8a8175}
nav.crumbs{font-size:12px;letter-spacing:.08em;color:#8a8175}nav.crumbs a{text-decoration:none}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(200px,1fr));gap:28px;list-style:none;padding:0}.grid a{text-decoration:none}
.grid img{width:100%;aspect-ratio:3/4;object-fit:cover;background:#efe8dc}.grid img.c{object-fit:contain}.grid h3{font-weight:400;margin:10px 0 0;font-size:16px}.grid span{font-size:13px;color:#8a8175}
.product{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:48px;align-items:start}.product img{width:100%;background:#efe8dc}
.price{font-size:20px;letter-spacing:.06em}.btn{display:inline-block;margin-top:18px;padding:14px 26px;background:#1f1b16;color:#f6f3ed;text-decoration:none;font-size:12px;letter-spacing:.2em}
footer{border-top:1px solid #e2dbcf;font-size:12px;letter-spacing:.12em;color:#8a8175}@media(max-width:760px){.product{grid-template-columns:1fr}}"""


def page(title, desc, canonical, body, ld, image=None, depth=1):
    up = "../" * depth
    og_img = image or BASE + "assets/grut_home_nueva_hd.webp"
    return f"""<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
<link rel="canonical" href="{canonical}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="GRUT Buenos Aires">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{og_img}">
<meta name="twitter:card" content="summary_large_image">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@300;400&family=Italiana&display=swap">
<style>{CSS}</style>
<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>
</head>
<body>
<header><a class="logo" href="{up}">GRUT<small>BUENOS AIRES</small></a><a href="{up}catalogo.html">Colecciones</a></header>
<main>
{body}
</main>
<footer>GRUT BUENOS AIRES · MODA DE LUJO PRÊT-À-PORTER · PRESENTACIÓN PRIVADA · FABRICACIÓN BAJO PEDIDO · <a href="mailto:atelier@grut.com">atelier@grut.com</a></footer>
</body>
</html>
"""


ORG = {"@type": "Organization", "@id": BASE + "#organization", "name": "GRUT", "url": BASE}


def crumbs_ld(items):
    return {"@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "name": n, "item": u} for i, (n, u) in enumerate(items)]}


public = [p for p in products if p["cat"] not in EXCLUDED_CATS]
cats = []
for p in public:
    if p["cat"] not in cats:
        cats.append(p["cat"])

for d in ("colecciones", "productos"):
    shutil.rmtree(os.path.join(ROOT, d), ignore_errors=True)
    os.makedirs(os.path.join(ROOT, d))

urls = [BASE, BASE + "catalogo.html"]
cat_file = {c: f"colecciones/{slug(LABELS.get(c, c))}.html" for c in cats}
prod_file = {p["id"]: f"productos/{p['id']}-{slug(p['name'])}.html" for p in public}

for p in public:
    label = LABELS.get(p["cat"], p["cat"].title())
    g = p.get("g", "W")
    price = usd(p["price"])
    url = BASE + prod_file[p["id"]]
    title = f"{p['name']} — {label} | GRUT Buenos Aires"
    desc = f"{p['name']}, colección {label} de GRUT Buenos Aires ({GENDER[g]}). {p['desc']}"[:300]
    ld_prod = {"@type": "Product", "name": p["name"], "description": p["desc"], "image": img_url(p),
               "sku": f"GRUT-{p['id']}", "category": label, "url": url,
               "brand": {"@type": "Brand", "name": "GRUT"}, "manufacturer": {"@id": BASE + "#organization"},
               "offers": {"@type": "Offer", "price": p["price"], "priceCurrency": "USD",
                          "availability": "https://schema.org/MadeToOrder", "url": url,
                          "seller": {"@id": BASE + "#organization"}}}
    if g in ("W", "M"):
        ld_prod["audience"] = {"@type": "PeopleAudience", "suggestedGender": "female" if g == "W" else "male"}
    ld = {"@context": "https://schema.org", "@graph": [ORG, ld_prod, crumbs_ld(
        [("GRUT", BASE), (label, BASE + cat_file[p["cat"]]), (p["name"], url)])]}
    extra = ""
    if p.get("feat"):
        extra = f"<p class=\"eyebrow\">GRUT {esc(p['line'])} — Edition {esc(p['ed'])}</p>"
        if p.get("craft"):
            extra += f"<p>{esc(p['craft'])}</p>"
    body = f"""<nav class="crumbs"><a href="../">GRUT</a> / <a href="../{cat_file[p['cat']]}">{esc(label)}</a> / {esc(p['name'])}</nav>
<article class="product">
<img src="../assets/{esc(p['img'])}" alt="{esc(p['name'])} — GRUT {esc(label)}" width="800" height="1000">
<div>
<p class="eyebrow">GRUT · {esc(label)} · {GENDER[g]}</p>
<h1>{esc(p['name'])}</h1>
<p>{esc(p['desc'])}</p>
{extra}
<p class="price">USD {price}</p>
<p class="eyebrow">Presentación privada · Fabricación bajo pedido</p>
<a class="btn" href="../?p={p['id']}">VER EN LA TIENDA</a>
</div>
</article>"""
    open(os.path.join(ROOT, prod_file[p["id"]]), "w", encoding="utf-8").write(
        page(title, desc, url, body, ld, img_url(p)))
    urls.append(url)

cards = []
for c in cats:
    label = LABELS.get(c, c.title())
    items = [p for p in public if p["cat"] == c]
    url = BASE + cat_file[c]
    text = intro(c)
    genders = sorted({GENDER[p.get("g", "W")] for p in items})
    desc = (f"Colección {label} de GRUT Buenos Aires, moda de lujo prêt-à-porter. "
            f"{len(items)} piezas ({', '.join(genders)}). {text}").strip()[:300]
    lis = "\n".join(
        f"<li><a href=\"../{prod_file[p['id']]}\"><img loading=\"lazy\" {cls(p)}"
        f"src=\"../assets/{esc(p['img'])}\" alt=\"{esc(p['name'])}\"><h3>{esc(p['name'])}</h3>"
        f"<span>{GENDER[p.get('g', 'W')]} · USD {usd(p['price'])}</span></a></li>"
        for p in items)
    ld = {"@context": "https://schema.org", "@graph": [ORG, {
        "@type": "CollectionPage", "name": f"GRUT {label}", "url": url, "description": desc,
        "isPartOf": {"@type": "WebSite", "url": BASE, "name": "GRUT Buenos Aires"},
        "mainEntity": {"@type": "ItemList", "numberOfItems": len(items), "itemListElement": [
            {"@type": "ListItem", "position": i + 1, "url": BASE + prod_file[p["id"]], "name": p["name"]}
            for i, p in enumerate(items)]}}, crumbs_ld([("GRUT", BASE), (label, url)])]}
    body = f"""<nav class="crumbs"><a href="../">GRUT</a> / <a href="../catalogo.html">Colecciones</a> / {esc(label)}</nav>
<p class="eyebrow">GRUT Buenos Aires · Colección</p>
<h1>{esc(label)}</h1>
{f'<p>{esc(text)}</p>' if text else ''}
<p><a class="btn" href="../?c={c}">VER LA COLECCIÓN EN LA TIENDA</a></p>
<ul class="grid">
{lis}
</ul>"""
    open(os.path.join(ROOT, cat_file[c]), "w", encoding="utf-8").write(
        page(f"{label} — Colección | GRUT Buenos Aires", desc, url, body, ld, img_url(items[0])))
    urls.insert(2 + len(cards), url)
    cards.append(f"<li><a href=\"{cat_file[c]}\"><img loading=\"lazy\" {cls(items[0])}"
                 f"src=\"assets/{esc(items[0]['img'])}\" alt=\"GRUT {esc(label)}\"><h3>{esc(label)}</h3>"
                 f"<span>{len(items)} piezas</span></a></li>")

cat_desc = ("Todas las colecciones de GRUT Buenos Aires, marca de moda de lujo prêt-à-porter para mujer y hombre: "
            + ", ".join(LABELS.get(c, c) for c in cats) + ".")
ld = {"@context": "https://schema.org", "@graph": [ORG, {
    "@type": "CollectionPage", "name": "Colecciones GRUT", "url": BASE + "catalogo.html", "description": cat_desc,
    "mainEntity": {"@type": "ItemList", "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "url": BASE + cat_file[c], "name": LABELS.get(c, c)}
        for i, c in enumerate(cats)]}}]}
body = f"""<p class="eyebrow">GRUT Buenos Aires · Moda de lujo prêt-à-porter</p>
<h1>Colecciones</h1>
<p>{esc(cat_desc)}</p>
<ul class="grid">
{chr(10).join(cards)}
</ul>"""
open(os.path.join(ROOT, "catalogo.html"), "w", encoding="utf-8").write(
    page("Colecciones | GRUT Buenos Aires — Moda de lujo prêt-à-porter", cat_desc[:300],
         BASE + "catalogo.html", body, ld, depth=0).replace('href=""', 'href="./"'))

with open(os.path.join(ROOT, "sitemap.xml"), "w", encoding="utf-8") as f:
    f.write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n')
    for u in urls:
        f.write(f"  <url><loc>{esc(u)}</loc><lastmod>{TODAY}</lastmod></url>\n")
    f.write("</urlset>\n")

print(f"{len(cats)} colecciones, {len(public)} productos, {len(urls)} URLs en sitemap")
