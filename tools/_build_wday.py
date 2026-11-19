#!/usr/bin/env python3
"""Women's Day (30) + Youth Woman vol. IV (10): crops, shop, costs, patterns, pages."""
import html
import json
from pathlib import Path
from PIL import Image, ImageFilter

ROOT = Path("/Users/rodrigomeriggi/Desktop/GRUT")
SRC = Path("/Users/rodrigomeriggi/.cursor/projects/Users-rodrigomeriggi-Desktop-GRUT/assets")
OUT = ROOT / "assets" / "wday"
OUT.mkdir(parents=True, exist_ok=True)

BOARDS = [
    (SRC / "GRUT__Coleccio_n_Femenina_de_Di_a-fac6cba1-7217-4957-82d1-d10e6b864648.jpg",
     [(1, 206), (208, 412), (414, 611), (613, 814), (816, 1023)],
     [(88, 322), (374, 618)]),
    (SRC / "Collage_editorial_de_moda_GRUT-88cfd22c-ab2a-4a6c-ba30-455c486bf094.jpg",
     [(1, 204), (206, 408), (410, 618), (620, 819), (821, 1023)],
     [(90, 330), (372, 640)]),
    (SRC / "Editorial_GRUT__Estilo_Urbano_Femenino-cc96656b-ea93-4044-b828-28218222a0ee.jpg",
     [(1, 206), (208, 410), (412, 610), (612, 814), (816, 1023)],
     [(90, 318), (370, 630)]),
    (SRC / "GRUT_Juventud__Coleccio_n_Di_a_y_Noche-3ca2140a-1c75-43c5-8ca5-91c24155bbed.jpg",
     [(1, 208), (210, 410), (412, 614), (616, 817), (819, 1023)],
     [(114, 378), (420, 728)]),
]

# id, slug, name, price, incluye, desc, bom, cat
LOOKS = [
(878,"city-chic","City Chic",2480,"Sweater y pantalón","Sweater de punto crudo, pantalón beige y cinturón. Incluye sweater y pantalón. Los anteojos y el bolso son de styling.",[["merino",5],["gabardina",1.4]],"WDAY"),
(879,"college-prep","College Prep",3280,"Blazer, polo y falda","Blazer navy con escudo G, polo a rayas y falda plisada. Incluye blazer, polo y falda.",[["lana",1.8],["forro",1.2],["entretela",0.5],["boton",4],["jersey",0.8],["algodon",1.2]],"WDAY"),
(880,"casual-denim","Casual Denim",2680,"Campera, musculosa y jean","Campera de denim, musculosa blanca y jean. Incluye campera, musculosa y jean.",[["denim",2.6],["jersey",0.4],["boton",6]],"WDAY"),
(881,"weekend-lounge","Weekend Lounge",1980,"Hoodie","Hoodie oversized crudo con logo GRUT. Incluye el hoodie.",[["felpa",1.8],["cordon",0.8],["elastico",0.4]],"WDAY"),
(882,"riviera-day","Riviera Day",1880,"Camisa y short","Camisa a rayas abierta y short blanco. Incluye camisa y short. El bikini y el bolso son de styling.",[["lino",1.6],["gabardina",0.7],["boton",6]],"WDAY"),
(883,"sport-club","Sport Club",2280,"Musculosa, falda y sweater","Musculosa blanca con letra G, falda plisada y sweater navy. Incluye musculosa, falda y sweater. La raqueta es de styling.",[["jersey",0.4],["algodon",1.2],["merino",3]],"WDAY"),
(884,"modern-safari","Modern Safari",2480,"Camisa y short","Camisa safari beige con cinturón y short al tono. Incluye camisa y short. Los anteojos son de styling.",[["lino",2.2],["boton",8]],"WDAY"),
(885,"urban-minimal","Urban Minimal",1980,"Musculosa y pantalón","Musculosa negra y pantalón blanco. Incluye musculosa y pantalón. Los anteojos y el bolso son de styling.",[["jersey",0.4],["gabardina",1.4]],"WDAY"),
(886,"garden-day","Garden Day",2780,"Vestido","Vestido corto de broderie con escote cuadrado y mangas abullonadas. Incluye el vestido.",[["algodon",2.4]],"WDAY"),
(887,"art-culture","Art & Culture",2480,"Sweater y pantalón","Top de punto marrón, con un hombro descubierto, y pantalón blanco. Incluye sweater y pantalón. El pañuelo es de styling.",[["merino",3],["gabardina",1.4]],"WDAY"),
(888,"gallery-tour","Gallery Tour",2980,"Campera, musculosa y pantalón","Campera de ante chocolate, musculosa blanca y pantalón blanco. Incluye campera, musculosa y pantalón.",[["cueroNapa",1.4],["forro",1.0],["jersey",0.4],["gabardina",1.3],["cierre",1]],"WDAY"),
(889,"brunch-club","Brunch Club",2680,"Sweater y falda","Sweater crudo de un hombro y falda al tono. Incluye sweater y falda. Los anteojos son de styling.",[["merino",4],["algodon",1.2]],"WDAY"),
(890,"bookstore-mood","Bookstore Mood",2480,"Cárdigan, camisa y falda","Cárdigan navy con letra G, camisa blanca y falda gris. Incluye cárdigan, camisa y falda. Los anteojos son de styling.",[["merino",4],["camiseria",1.6],["gabardina",1.1],["boton",6]],"WDAY"),
(891,"bike-day","Bike Day",1880,"Buzo y short","Buzo navy con logo GRUT y short negro. Incluye buzo y short. La gorra, los auriculares y la bici son de styling.",[["felpa",1.4],["jersey",0.5],["elastico",0.6]],"WDAY"),
(892,"sunset-picnic","Sunset Picnic",2980,"Vestido","Vestido de flores con escote cuadrado y mangas abullonadas. Incluye el vestido.",[["viscosa",2.8]],"WDAY"),
(893,"art-studio","Art Studio",1780,"Camisa","Camisa blanca oversized, con pintura de atelier. Incluye la camisa. Los pinceles son de styling.",[["camiseria",2.0],["boton",7]],"WDAY"),
(894,"wellness-day","Wellness Day",2180,"Musculosa, pantalón y campera","Top deportivo gris con letra G, calza al tono y campera clara. Incluye musculosa, pantalón y campera.",[["jersey",1.4],["gabardina",0.8],["elastico",1.2],["cierre",1]],"WDAY"),
(895,"airport-look","Airport Look",4280,"Abrigo, buzo y pantalón","Abrigo camel, buzo crudo y pantalón al tono. Incluye abrigo, buzo y pantalón. Los anteojos son de styling.",[["lana",2.4],["forro",1.6],["felpa",1.2],["gabardina",1.3],["boton",4]],"WDAY"),
(896,"dinner-date","Dinner Date",3480,"Vestido","Vestido slip negro de satén, con breteles finos. Incluye el vestido. Los anteojos son de styling.",[["saten",1.8],["forro",1.2],["cierre",1]],"WDAY"),
(897,"rooftop-night","Rooftop Night",3280,"Top y jean","Top strapless de lentejuela y jean negro. Incluye top y jean. La campera es de styling.",[["lent",0.6],["denim",1.4]],"WDAY"),
(898,"off-duty-luxe","Off-Duty Luxe",2180,"Hoodie y short","Hoodie crudo con logo GRUT y short al tono. Incluye hoodie y short. Los anteojos son de styling.",[["felpa",2.0],["elastico",0.8],["cordon",0.8]],"WDAY"),
(899,"varsity-icon","Varsity Icon",2880,"Campera, musculosa y jean","Campera varsity navy y crudo con letra G, musculosa blanca y jean. Incluye campera, musculosa y jean.",[["lana",1.4],["cueroNapa",0.7],["jersey",0.4],["denim",1.4],["boton",6]],"WDAY"),
(900,"timeless-shirt","Timeless Shirt",1980,"Camisa y pantalón","Camisa a rayas celestes y pantalón blanco. Incluye camisa y pantalón. Los anteojos son de styling.",[["lino",1.8],["gabardina",1.3],["boton",7]],"WDAY"),
(901,"modern-utility","Modern Utility",2680,"Campera, musculosa y short","Campera de ante chocolate, musculosa blanca y short blanco. Incluye campera, musculosa y short.",[["cueroNapa",1.3],["forro",0.9],["jersey",0.4],["gabardina",0.7],["cierre",1]],"WDAY"),
(902,"nautical-spirit","Nautical Spirit",2280,"Polo y short","Polo a rayas navy con letra G y short blanco. Incluye polo y short.",[["jersey",0.9],["gabardina",0.7],["boton",3]],"WDAY"),
(903,"denim-essential","Denim Essential",1880,"Musculosa y jean","Musculosa de punto blanca y jean. Incluye musculosa y jean. Los anteojos son de styling.",[["algodon",3],["denim",1.4]],"WDAY"),
(904,"sport-heritage","Sport Heritage",2180,"Campera y pantalón","Campera deportiva negra con logo GRUT y pantalón al tono. Incluye campera y pantalón. Los auriculares son de styling.",[["gabardina",1.6],["jersey",1.2],["elastico",1.2],["cierre",1]],"WDAY"),
(905,"boho-contemporary","Boho Contemporary",2680,"Vestido","Vestido corto blanco de broderie, con mangas largas y volado. Incluye el vestido.",[["algodon",2.6]],"WDAY"),
(906,"knit-relax","Knit Relax",2280,"Sweater y short","Sweater gris y short de punto al tono. Incluye sweater y short. Los anteojos son de styling.",[["merino",5],["algodon",1.2]],"WDAY"),
(907,"city-cargo","City Cargo",2480,"Musculosa, campera y pantalón","Musculosa blanca, campera negra y pantalón cargo. Incluye musculosa, campera y pantalón. Los anteojos son de styling.",[["jersey",0.4],["gabardina",2.2],["cueroNapa",0.8],["forro",0.6],["cierre",1]],"WDAY"),
(908,"campus-hangout","Campus Hangout",1980,"Hoodie y jean","Hoodie azul con logo GRUT y jean cargo. Incluye hoodie y jean. Los auriculares son de styling.",[["felpa",1.8],["denim",1.8],["cordon",0.8],["elastico",0.6]],"YOUTH"),
(909,"skate-park","Skate Park Club",2680,"Campera, buzo y pantalón","Campera varsity bordó con letra G, buzo gris y pantalón cargo. Incluye campera, buzo y pantalón. La skate es de styling.",[["lana",1.4],["cueroNapa",0.6],["felpa",1.2],["gabardina",1.8],["boton",6]],"YOUTH"),
(910,"record-store","Record Store",2180,"Camisa, remera y pantalón","Camisa a cuadros, remera con logo GRUT y pantalón cargo. Incluye camisa, remera y pantalón.",[["camiseria",1.6],["jersey",0.6],["gabardina",1.8],["boton",6]],"YOUTH"),
(911,"weekend-brunch-yw","Weekend Brunch",2480,"Sweater, falda y pantalón","Sweater crudo con logo GRUT, falda de encaje y pantalón cargo verde. Incluye sweater, falda y pantalón.",[["merino",5],["algodon",1.0],["gabardina",1.6]],"YOUTH"),
(912,"city-stroll","City Stroll",2380,"Blazer, camisa y pantalón","Blazer gris, camisa con corbata y pantalón bordó. Incluye blazer, camisa y pantalón.",[["lana",1.6],["forro",1.1],["entretela",0.4],["camiseria",1.6],["gabardina",1.4],["boton",4]],"YOUTH"),
(913,"dance-floor-star","Dance Floor",2480,"Campera, remera y jean","Campera metalizada, remera con estrella y jean cargo. Incluye campera, remera y jean.",[["cueroMetal",1.2],["forro",0.8],["jersey",0.5],["denim",1.8],["cierre",1]],"YOUTH"),
(914,"after-dark-denim","After Dark Denim",2380,"Campera y jean","Campera de denim con estrellas y jean cargo. Incluye campera y jean.",[["denim",3.2],["boton",6]],"YOUTH"),
(915,"neon-crew","Neon Crew",2280,"Buzo y pantalón","Buzo negro y rosa y pantalón cargo lila. Incluye buzo y pantalón.",[["felpa",1.6],["gabardina",1.8],["elastico",1],["cordon",1]],"YOUTH"),
(916,"midnight-street","Midnight Street",2580,"Campera, remera y pantalón","Campera oliva con logo GRUT, remera negra y pantalón cargo. Incluye campera, remera y pantalón.",[["gabardina",1.8],["forro",1.0],["jersey",0.5],["cierre",1]],"YOUTH"),
(917,"party-oversize","Party Oversize",2380,"Sweater, falda y pantalón","Sweater lila con estrellas, falda a cuadros y pantalón cargo. Incluye sweater, falda y pantalón.",[["merino",5],["algodon",1.2],["gabardina",1.6]],"YOUTH"),
]

def crop_all():
    boxes = []
    for path, cols, rows in BOARDS:
        im = Image.open(path).convert("RGB")
        for y0, y1 in rows:
            for x0, x1 in cols:
                boxes.append(im.crop((x0, y0, x1, y1)))
    if len(boxes) != len(LOOKS):
        raise SystemExit(f"crops {len(boxes)} looks {len(LOOKS)}")
    for look, im in zip(LOOKS, boxes):
        w, h = im.size
        scale = 1000 / w
        up = im.resize((1000, max(1, round(h * scale))), Image.Resampling.LANCZOS)
        up = up.filter(ImageFilter.UnsharpMask(radius=1.2, percent=60, threshold=3))
        up.save(OUT / f"{look[1]}.webp", "WEBP", quality=86, method=6)
        print(look[0], look[1], w, h)

def js(s):
    return "'" + s.replace("\\", "\\\\").replace("'", "\\'") + "'"

def money(n):
    return f"{n:,}".replace(",", ".")

def patch_index():
    p = ROOT / "index.html"
    text = p.read_text()
    if "wday/city-chic" in text:
        raise SystemExit("index already")
    lines = []
    for i, slug, name, price, inc, desc, bom, cat in LOOKS:
        lines.append("{id:%d,g:'W',name:%s,cat:%s,price:%d,img:%s,pos:'center 15%%',desc:%s}," % (
            i, js(name), js(cat), price, js(f"wday/{slug}.webp?v=1"), js(desc)))
    needle = "\n];let gender"
    if text.count(needle) != 1:
        raise SystemExit("index anchor")
    text = text.replace(needle, "\n" + "\n".join(lines) + needle, 1)
    old = "<article class=\"collection-card\" onclick=\"filter('DAY')\"><img src=\"assets/bd1.webp\" alt=\"Colección Day\"><div><h3>Day</h3><p>Elegancia sin esfuerzo.</p><span>DESCUBRIR →</span></div></article><article class=\"collection-card\" onclick=\"filter('NIGHT')\"><img src=\"assets/ln2.webp\""
    new = old.replace("<article class=\"collection-card\" onclick=\"filter('NIGHT')\"><img src=\"assets/ln2.webp\"",
        "<article class=\"collection-card\" onclick=\"filter('WDAY')\"><img src=\"assets/wday/city-chic.webp?v=1\" alt=\"Women's Day\" style=\"object-position:center 15%\"><div><h3>Women's Day</h3><p>Día, ciudad y jardín.</p><span>DESCUBRIR →</span></div></article><article class=\"collection-card\" onclick=\"filter('NIGHT')\"><img src=\"assets/ln2.webp\"")
    if old not in text:
        raise SystemExit("day card missing")
    text = text.replace(old, new, 1)
    reps = [
        ("filter('DAY')\">Day</button><button role=\"menuitem\" onclick=\"filter('NIGHT')\">Night</button>",
         "filter('DAY')\">Day</button><button role=\"menuitem\" onclick=\"filter('WDAY')\">Women's Day</button><button role=\"menuitem\" onclick=\"filter('NIGHT')\">Night</button>"),
        ("filter('DAY')\">Day</button><button onclick=\"toggleMenu();filter('NIGHT')\">Night</button>",
         "filter('DAY')\">Day</button><button onclick=\"toggleMenu();filter('WDAY')\">Women's Day</button><button onclick=\"toggleMenu();filter('NIGHT')\">Night</button>"),
        ("filter('DAY')\">Day</button><button data-cat=\"NIGHT\" onclick=\"filter('NIGHT')\">Night</button>",
         "filter('DAY')\">Day</button><button data-cat=\"WDAY\" onclick=\"filter('WDAY')\">Women's Day</button><button data-cat=\"NIGHT\" onclick=\"filter('NIGHT')\">Night</button>"),
    ]
    for a, b in reps:
        if text.count(a) != 1:
            raise SystemExit("nav miss " + a[:40])
        text = text.replace(a, b, 1)
    a = "if(title)title.textContent="
    b = "if(title)title.textContent=c==='WDAY'?'Women\\'s Day':"
    if text.count(a) != 1:
        raise SystemExit("title fn")
    text = text.replace(a, b, 1)
    a = "if(current==='YOUTH'){const n=products.filter(p=>own(p)&&p.cat==='YOUTH').length;return 'Urban Youth · '+n+' looks'}"
    b = a + "if(current==='WDAY'){const n=products.filter(p=>own(p)&&p.cat==='WDAY').length;return 'Women\\'s Day · '+n+' looks'}"
    if text.count(a) != 1:
        raise SystemExit("eyebrow")
    text = text.replace(a, b, 1)
    a = "p.cat==='YOUTH'?'Urban Youth':"
    if text.count(a) != 2:
        raise SystemExit("cat labels " + str(text.count(a)))
    text = text.replace(a, "p.cat==='WDAY'?'Women\\'s Day':" + a)
    a = "filter('DAY');location.hash='shop'\">Day</a>"
    b = a + "<a href=\"colecciones/womens-day.html\" onclick=\"event.preventDefault();filter('WDAY');location.hash='shop'\">Women's Day</a>"
    if text.count(a) != 1:
        raise SystemExit("footer")
    text = text.replace(a, b, 1)
    p.write_text(text)
    print("index")

def patch_costos():
    p = ROOT / "costos.html"
    text = p.read_text()
    if "wday/city-chic" in text:
        raise SystemExit("costos already")
    rows = []
    for i, slug, name, price, inc, desc, bom, cat in LOOKS:
        bom_js = ",".join('["%s", %s]' % (k, q if isinstance(q, int) else q) for k, q in bom)
        rows.append('[%d,%s,%s,%d,%s,%s,[%s],\'W\'],' % (
            i, json.dumps(name, ensure_ascii=False), json.dumps(cat), price,
            json.dumps(f"wday/{slug}.webp?v=1"), json.dumps(inc, ensure_ascii=False), bom_js))
    needle = "].map(([id,name,cat,price,img,includes,bom,g='W'])"
    if text.count(needle) != 1:
        raise SystemExit("costos anchor")
    text = text.replace(needle, "\n" + "\n".join(rows) + "\n" + needle, 1)
    text = text.replace("'URBAN','YOUTH'", "'URBAN','YOUTH','WDAY'", 1)
    a = "c==='YOUTH'?'Urban Youth':"
    if text.count(a) != 1:
        raise SystemExit("costos label")
    text = text.replace(a, "c==='WDAY'?'Women\\'s Day':" + a, 1)
    p.write_text(text)
    print("costos")

def patch_moldes():
    p = ROOT / "moldes.html"
    text = p.read_text()
    if "wday/city-chic" in text:
        raise SystemExit("moldes already")
    objs, boms = [], []
    for i, slug, name, price, inc, desc, bom, cat in LOOKS:
        objs.append(json.dumps({
            "id": i, "name": name, "cat": cat, "g": "W",
            "img": f"wday/{slug}.webp?v=1", "desc": desc, "accessory": False,
        }, ensure_ascii=False))
        boms.append("  %d:[%s]," % (i, ", ".join('["%s", %s]' % (k, q) for k, q in bom)))
    anchor = '"id": 877, "name": "After Midnight"'
    i = text.find(anchor)
    j = text.find("}];", i)
    if i < 0 or j < 0:
        raise SystemExit("products anchor")
    text = text[:j] + "}," + ",".join(objs) + text[j+1:]
    bom_anchor = '  877:[["jersey", 1.3], ["gabardina", 2.0], ["elastico", 0.8]],\n};'
    if bom_anchor not in text:
        raise SystemExit("bom anchor")
    text = text.replace(bom_anchor, '  877:[["jersey", 1.3], ["gabardina", 2.0], ["elastico", 0.8]],\n' + "\n".join(boms) + "\n};", 1)
    text = text.replace("'URBAN','YOUTH'", "'URBAN','YOUTH','WDAY'")
    text = text.replace("YOUTH:'Urban Youth'", "YOUTH:'Urban Youth',WDAY:'Women\\'s Day'")
    a = "p.cat==='YOUTH'?'Urban Youth':"
    if text.count(a) != 1:
        raise SystemExit("moldes label " + str(text.count(a)))
    text = text.replace(a, "p.cat==='WDAY'?'Women\\'s Day':" + a)
    p.write_text(text)
    print("moldes")

PAGE_CSS = """*{box-sizing:border-box}body{margin:0;background:#f6f3ed;color:#1f1b16;font-family:'DM Sans',system-ui,sans-serif;font-weight:300;line-height:1.6}
a{color:inherit}header,main,footer{max-width:1180px;margin:0 auto;padding:24px}header{display:flex;justify-content:space-between;align-items:center;border-bottom:1px solid #e2dbcf}
.logo{font-family:Italiana,serif;font-size:30px;letter-spacing:.18em;text-decoration:none}.logo small{display:block;font-family:'DM Sans';font-size:9px;letter-spacing:.4em}
h1,h2{font-family:Italiana,serif;font-weight:400;letter-spacing:.04em}h1{font-size:clamp(36px,6vw,64px);margin:.2em 0}.eyebrow{font-size:11px;letter-spacing:.25em;text-transform:uppercase;color:#8a8175}
nav.crumbs{font-size:12px;letter-spacing:.08em;color:#8a8175}nav.crumbs a{text-decoration:none}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(200px,1fr));gap:28px;list-style:none;padding:0}.grid a{text-decoration:none}
.grid img{width:100%;aspect-ratio:3/4;object-fit:cover;background:#efe8dc}.grid h3{font-weight:400;margin:10px 0 0;font-size:16px}.grid span{font-size:13px;color:#8a8175}
.product{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:48px;align-items:start}.product img{width:100%;background:#efe8dc}
.price{font-size:20px;letter-spacing:.06em}.btn{display:inline-block;margin-top:18px;padding:14px 26px;background:#1f1b16;color:#f6f3ed;text-decoration:none;font-size:12px;letter-spacing:.2em}
footer{border-top:1px solid #e2dbcf;font-size:12px;letter-spacing:.12em;color:#8a8175}@media(max-width:760px){.product{grid-template-columns:1fr}}"""

def write_pages():
    day_items, day_cards = [], []
    youth_items, youth_cards = [], []
    for i, slug, name, price, inc, desc, bom, cat in LOOKS:
        coll = "womens-day" if cat == "WDAY" else "urban-youth"
        coll_name = "Women's Day" if cat == "WDAY" else "Urban Youth"
        url = f"https://rodrigomeriggi.github.io/grut/productos/{i}-{slug}.html"
        img = f"https://rodrigomeriggi.github.io/grut/assets/wday/{slug}.webp?v=1"
        meta = f"{name}, colección {coll_name} de GRUT Buenos Aires (Mujer). {desc}"
        graph = {"@context": "https://schema.org", "@graph": [
            {"@type": "Organization", "@id": "https://rodrigomeriggi.github.io/grut/#organization", "name": "GRUT", "url": "https://rodrigomeriggi.github.io/grut/"},
            {"@type": "Product", "name": name, "description": desc, "image": img, "sku": f"GRUT-{i}", "category": coll_name, "url": url,
             "brand": {"@type": "Brand", "name": "GRUT"}, "manufacturer": {"@id": "https://rodrigomeriggi.github.io/grut/#organization"},
             "offers": {"@type": "Offer", "price": price, "priceCurrency": "USD", "availability": "https://schema.org/MadeToOrder", "url": url, "seller": {"@id": "https://rodrigomeriggi.github.io/grut/#organization"}},
             "audience": {"@type": "PeopleAudience", "suggestedGender": "female"}},
            {"@type": "BreadcrumbList", "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": "GRUT", "item": "https://rodrigomeriggi.github.io/grut/"},
                {"@type": "ListItem", "position": 2, "name": coll_name, "item": f"https://rodrigomeriggi.github.io/grut/colecciones/{coll}.html"},
                {"@type": "ListItem", "position": 3, "name": name, "item": url}]}]}
        ld = json.dumps(graph, ensure_ascii=False, separators=(", ", ": "))
        (ROOT / "productos" / f"{i}-{slug}.html").write_text(f"""<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(name)} — {html.escape(coll_name)} | GRUT Buenos Aires</title>
<meta name="description" content="{html.escape(meta)}">
<link rel="canonical" href="{url}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="GRUT Buenos Aires">
<meta property="og:title" content="{html.escape(name)} — {html.escape(coll_name)} | GRUT Buenos Aires">
<meta property="og:description" content="{html.escape(meta)}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{img}">
<meta name="twitter:card" content="summary_large_image">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@300;400&family=Italiana&display=swap">
<style>{PAGE_CSS}</style>
<script type="application/ld+json">{ld}</script>
</head>
<body>
<header><a class="logo" href="../">GRUT<small>BUENOS AIRES</small></a><a href="../catalogo.html">Colecciones</a></header>
<main>
<nav class="crumbs"><a href="../">GRUT</a> / <a href="../colecciones/{coll}.html">{html.escape(coll_name)}</a> / {html.escape(name)}</nav>
<article class="product">
<img src="../assets/wday/{slug}.webp?v=1" alt="{html.escape(name)} — GRUT {html.escape(coll_name)}" width="1000" height="1400">
<div>
<p class="eyebrow">GRUT · {html.escape(coll_name)} · Mujer</p>
<h1>{html.escape(name)}</h1>
<p>{html.escape(desc)}</p>
<p class="price">USD {money(price)}</p>
<p class="eyebrow">Presentación privada · Fabricación bajo pedido</p>
<a class="btn" href="../?p={i}">VER EN LA TIENDA</a>
<p class="eyebrow"><a href="../moldes.html?id={i}">Ver moldes</a> · <a href="../costos.html">Ver costos</a></p>
</div>
</article>
</main>
<footer>GRUT BUENOS AIRES · MODA DE LUJO PRÊT-À-PORTER · PRESENTACIÓN PRIVADA · FABRICACIÓN BAJO PEDIDO · <a href="mailto:atelier@grut.com">atelier@grut.com</a></footer>
</body>
</html>
""")
        item = {"@type": "ListItem", "url": url, "name": name}
        card = f'<li><a href="../productos/{i}-{slug}.html"><img loading="lazy" src="../assets/wday/{slug}.webp?v=1" alt="{html.escape(name)}"><h3>{html.escape(name)}</h3><span>Mujer · USD {money(price)}</span></a></li>'
        if cat == "WDAY":
            day_items.append(item); day_cards.append(card)
        else:
            youth_items.append(item); youth_cards.append(card)
    blurb = "Women's Day Collection: treinta looks de día, de la ciudad al jardín y a la noche corta. Punto, lino, denim, ante y broderie, con la confección de la maison."
    desc = "Colección Women's Day de GRUT Buenos Aires, moda de lujo prêt-à-porter. 30 piezas (Mujer). " + blurb
    for n, it in enumerate(day_items, 1):
        it["position"] = n
    graph = {"@context": "https://schema.org", "@graph": [
        {"@type": "Organization", "@id": "https://rodrigomeriggi.github.io/grut/#organization", "name": "GRUT", "url": "https://rodrigomeriggi.github.io/grut/"},
        {"@type": "CollectionPage", "name": "GRUT Women's Day", "url": "https://rodrigomeriggi.github.io/grut/colecciones/womens-day.html", "description": desc,
         "isPartOf": {"@type": "WebSite", "url": "https://rodrigomeriggi.github.io/grut/", "name": "GRUT Buenos Aires"},
         "mainEntity": {"@type": "ItemList", "numberOfItems": 30, "itemListElement": day_items}},
        {"@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "GRUT", "item": "https://rodrigomeriggi.github.io/grut/"},
            {"@type": "ListItem", "position": 2, "name": "Women's Day", "item": "https://rodrigomeriggi.github.io/grut/colecciones/womens-day.html"}]}]}
    ld = json.dumps(graph, ensure_ascii=False, separators=(", ", ": "))
    (ROOT / "colecciones" / "womens-day.html").write_text(f"""<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Women's Day — Colección | GRUT Buenos Aires</title>
<meta name="description" content="{html.escape(desc)}">
<link rel="canonical" href="https://rodrigomeriggi.github.io/grut/colecciones/womens-day.html">
<meta property="og:type" content="website">
<meta property="og:site_name" content="GRUT Buenos Aires">
<meta property="og:title" content="Women's Day — Colección | GRUT Buenos Aires">
<meta property="og:description" content="{html.escape(desc)}">
<meta property="og:url" content="https://rodrigomeriggi.github.io/grut/colecciones/womens-day.html">
<meta property="og:image" content="https://rodrigomeriggi.github.io/grut/assets/wday/city-chic.webp?v=1">
<meta name="twitter:card" content="summary_large_image">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@300;400&family=Italiana&display=swap">
<style>{PAGE_CSS}</style>
<script type="application/ld+json">{ld}</script>
</head>
<body>
<header><a class="logo" href="../">GRUT<small>BUENOS AIRES</small></a><a href="../catalogo.html">Colecciones</a></header>
<main>
<nav class="crumbs"><a href="../">GRUT</a> / <a href="../catalogo.html">Colecciones</a> / Women's Day</nav>
<p class="eyebrow">GRUT Buenos Aires · Colección</p>
<h1>Women's Day</h1>
<p>{html.escape(blurb)}</p>
<p><a class="btn" href="../?c=WDAY">VER LA COLECCIÓN EN LA TIENDA</a></p>
<ul class="grid">
{''.join(day_cards)}
</ul>
</main>
<footer>GRUT BUENOS AIRES · MODA DE LUJO PRÊT-À-PORTER · PRESENTACIÓN PRIVADA · FABRICACIÓN BAJO PEDIDO · <a href="mailto:atelier@grut.com">atelier@grut.com</a></footer>
</body>
</html>
""")
    # youth woman onto the existing urban youth page
    uy = (ROOT / "colecciones" / "urban-youth.html").read_text()
    if "campus-hangout" in uy:
        raise SystemExit("youth page already")
    extra = []
    for n, it in enumerate(youth_items, 51):
        it["position"] = n
        extra.append(json.dumps(it, ensure_ascii=False, separators=(", ", ": ")))
    anchor = '"name": "After Midnight"}]}'
    if uy.count(anchor) != 1:
        raise SystemExit("youth json " + str(uy.count(anchor)))
    uy = uy.replace(anchor, '"name": "After Midnight"},' + ",".join(extra) + "]}", 1)
    uy = uy.replace('"numberOfItems": 50', '"numberOfItems": 60', 1)
    uy = uy.replace("50 piezas (Hombre, Mujer). Cápsula 2027 y Youth Collection 15 Years: cincuenta looks",
                    "60 piezas (Hombre, Mujer). Cápsula 2027, Youth Collection 15 Years y Youth Woman: sesenta looks", 1)
    uy = uy.replace("cincuenta looks, de campus", "sesenta looks, de campus", 1)
    uy = uy.replace("</ul>", "".join(youth_cards) + "\n</ul>", 1)
    (ROOT / "colecciones" / "urban-youth.html").write_text(uy)
    cat = (ROOT / "catalogo.html").read_text()
    li = '<li><a href="colecciones/day.html"><img loading="lazy" src="assets/bd1.webp" alt="GRUT Day"><h3>Day</h3><span>45 piezas</span></a></li>'
    add = li + '\n<li><a href="colecciones/womens-day.html"><img loading="lazy" src="assets/wday/city-chic.webp?v=1" alt="GRUT Women\'s Day"><h3>Women\'s Day</h3><span>30 piezas</span></a></li>'
    if li not in cat:
        raise SystemExit("catalog day")
    cat = cat.replace(li, add, 1)
    old = '<li><a href="colecciones/urban-youth.html"><img loading="lazy" src="assets/youth15/campus-club.webp?v=1" alt="GRUT Urban Youth"><h3>Urban Youth</h3><span>50 piezas</span></a></li>'
    new = old.replace("50 piezas", "60 piezas")
    if old not in cat:
        raise SystemExit("catalog youth")
    cat = cat.replace(old, new, 1)
    (ROOT / "catalogo.html").write_text(cat)
    sm = (ROOT / "sitemap.xml").read_text()
    urls = [f"https://rodrigomeriggi.github.io/grut/colecciones/womens-day.html"]
    urls += [f"https://rodrigomeriggi.github.io/grut/productos/{i}-{slug}.html" for i, slug, *_ in LOOKS]
    if "womens-day.html" in sm:
        raise SystemExit("sitemap already")
    block = "\n".join(f"  <url><loc>{u}</loc><lastmod>2026-11-19</lastmod></url>" for u in urls)
    sm = sm.replace("</urlset>", block + "\n</urlset>")
    sm = sm.replace("colecciones/urban-youth.html</loc><lastmod>2026-11-19", "colecciones/urban-youth.html</loc><lastmod>2026-11-19")
    (ROOT / "sitemap.xml").write_text(sm)
    print("pages", len(LOOKS))

if __name__ == "__main__":
    crop_all()
    patch_index()
    patch_costos()
    patch_moldes()
    write_pages()
