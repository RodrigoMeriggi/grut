#!/usr/bin/env python3
"""Colors 2027 Men: crop each look, upscale, shop, costs, patterns, pages."""
import html
import json
from pathlib import Path
from PIL import Image, ImageFilter, ImageEnhance

ROOT = Path("/Users/rodrigomeriggi/Desktop/GRUT")
SRC = Path("/Users/rodrigomeriggi/.cursor/projects/Users-rodrigomeriggi-Desktop-GRUT/assets")
OUT = ROOT / "assets" / "colors"
OUT.mkdir(parents=True, exist_ok=True)

BOARDS = [
    (SRC / "Colores_2027__Invierno_masculino_de_lujo-9f18afc7-7604-4229-b193-d7cb893b5c25.jpg",
     [(2, 186), (192, 372), (378, 559), (566, 746), (752, 933)],
     [(140, 528), (546, 1020)]),
    (SRC / "Cata_logo_Oton_o_2027__Colores_de_Hombre-c43ba9e7-9365-43cf-9dc0-19a1be9a3ee9.jpg",
     [(2, 186), (192, 372), (378, 559), (566, 746), (752, 933)],
     [(140, 528), (546, 1020)]),
    (SRC / "Editorial_masculina_de_oton_o_2027-3d7dbd0a-79c1-4aa8-8665-8cff73b7c1c3.jpg",
     [(2, 186), (192, 372), (378, 559), (566, 746), (752, 933)],
     [(140, 528), (546, 1020)]),
    (SRC / "Campan_a_de_moda_masculina_Colors_2027-29182822-2f52-4afe-83d7-e86c3b909178.jpg",
     [(2, 168), (170, 330), (334, 494), (498, 654), (658, 817)],
     [(112, 532), (540, 1022)]),
]

# id, slug, name, price, incluye, desc, bom
LOOKS = [
(968,"m-abrigo-teal","Teal Overcoat",4980,"Abrigo, sweater y pantalón","Abrigo largo verde petróleo, sweater de cuello alto y pantalón al tono, con cinturón. Incluye abrigo, sweater y pantalón. Los anteojos son de styling.",[["cashmerePano",2.6],["forro",1.6],["merino",3],["gabardina",1.5],["boton",4]]),
(969,"m-punto-bordo","Burgundy Cable",3280,"Sweater y pantalón","Sweater de punto trenzado bordó y pantalón amplio al tono. Incluye sweater y pantalón. El bolso es de styling.",[["merino",5],["gabardina",1.5]]),
(970,"m-capa-camel","Camel Layer",5480,"Abrigo, chaleco, sweater y pantalón","Abrigo camel, chaleco, sweater de cuello alto y pantalón crudo, con cinturón. Incluye abrigo, chaleco, sweater y pantalón. Los anteojos y los guantes son de styling.",[["cashmerePano",2.6],["lana",0.9],["forro",2.1],["entretela",0.3],["merino",3],["gabardina",1.5],["boton",8]]),
(971,"m-campo-oliva","Olive Field",4680,"Abrigo, sweater y pantalón","Abrigo de campo oliva, sweater de cuello alto y pantalón al tono, con cinturón. Incluye abrigo, sweater y pantalón. Los anteojos son de styling.",[["gabardina",4.3],["forro",1.4],["merino",3],["boton",6]]),
(972,"m-abrigo-violeta","Purple Coat",4980,"Abrigo, sweater y pantalón","Abrigo largo violeta, sweater de cuello alto y pantalón gris, con cinturón. Incluye abrigo, sweater y pantalón. Los anteojos y los guantes son de styling.",[["cashmerePano",2.6],["forro",1.6],["merino",3],["gabardina",1.5],["boton",6]]),
(973,"m-shearling-marfil","Ivory Shearling",5280,"Abrigo, sweater y pantalón","Abrigo marfil con cuello de shearling, sweater de punto trenzado y pantalón al tono, con cinturón. Incluye abrigo, sweater y pantalón. Los anteojos son de styling.",[["lana",2.2],["cordero",0.35],["forro",1.4],["merino",4],["gabardina",1.5],["boton",4]]),
(974,"m-cuero-navy","Navy Shearling",4280,"Campera, sweater y pantalón","Campera de cuero azul con cuello de shearling, sweater de cuello alto y pantalón al tono, con cinturón. Incluye campera, sweater y pantalón. Los anteojos son de styling.",[["cueroNapa",1.4],["cordero",0.25],["forro",0.9],["merino",3],["gabardina",1.5],["cierre",1]]),
(975,"m-abrigo-vino","Wine Overcoat",5480,"Abrigo, saco y pantalón","Abrigo largo bordó, saco y pantalón al tono. Incluye abrigo, saco y pantalón. La bufanda es de styling.",[["cashmerePano",2.8],["lana",1.6],["forro",2.6],["entretela",0.5],["gabardina",1.5],["boton",6]]),
(976,"m-punto-teal","Teal Cable",3180,"Sweater y pantalón","Sweater de punto trenzado teal y pantalón crudo, con cinturón. Incluye sweater y pantalón. El bolso es de styling.",[["merino",5],["gabardina",1.5]]),
(977,"m-pluma-mostaza","Mustard Puffer",3680,"Campera, sweater y pantalón","Campera de pluma mostaza, sweater chocolate y pantalón gris, con cinturón. Incluye campera, sweater y pantalón. Los anteojos y los guantes son de styling.",[["gabardina",3.0],["plumon",1],["merino",3],["cierre",1]]),
(978,"m-safari-chocolate","Chocolate Safari",4280,"Campera, sweater y pantalón","Campera safari chocolate con cinturón, sweater de cuello alto y pantalón crudo. Incluye campera, sweater y pantalón. Los anteojos son de styling.",[["gabardina",3.7],["forro",0.8],["merino",3],["boton",6]]),
(979,"m-punto-oxido","Rust Cable",3280,"Sweater y pantalón","Sweater de punto trenzado óxido y pantalón oliva, con cinturón. Incluye sweater y pantalón. El bolso es de styling.",[["merino",5],["gabardina",1.5]]),
(980,"m-tweed-avellana","Hazelnut Tweed",3980,"Blazer, sweater y pantalón","Blazer de tweed avellana, sweater chocolate y pantalón crudo. Incluye blazer, sweater y pantalón. Los anteojos son de styling.",[["lana",1.8],["forro",1.1],["entretela",0.5],["merino",3],["gabardina",1.5],["boton",2]]),
(981,"m-chaqueta-oliva","Olive Jacket",3880,"Campera, sweater y pantalón","Chaqueta de campo oliva, sweater de cuello alto y pantalón al tono, con cinturón. Incluye campera, sweater y pantalón. Los anteojos son de styling.",[["gabardina",3.9],["forro",0.9],["merino",3],["boton",4]]),
(982,"m-sobrecamisa-bordo","Burgundy Overshirt",3480,"Sobrecamisa, sweater y pantalón","Sobrecamisa bordó, sweater de cuello alto y pantalón gris. Incluye sobrecamisa, sweater y pantalón. Los anteojos son de styling.",[["gabardina",3.3],["merino",3],["boton",6]]),
(983,"m-abrigo-marfil","Ivory Coat",4980,"Abrigo, sweater y pantalón","Abrigo marfil, sweater chocolate y pantalón al tono. Incluye abrigo, sweater y pantalón. La bufanda y los anteojos son de styling.",[["cashmerePano",2.6],["forro",1.6],["merino",3],["gabardina",1.5],["boton",4]]),
(984,"m-cierre-marino","Navy Zip",2880,"Sweater y pantalón","Sweater azul marino con cierre al cuello y pantalón gris. Incluye sweater y pantalón. Los anteojos son de styling.",[["merino",4],["cierre",1],["gabardina",1.5]]),
(985,"m-cuero-cognac","Cognac Leather",4280,"Campera, camisa y pantalón","Campera de cuero cognac, camisa oliva y pantalón crudo, con cinturón. Incluye campera, camisa y pantalón. Los anteojos son de styling.",[["cueroNapa",1.4],["forro",0.9],["cierre",1],["camiseria",1.6],["gabardina",1.5],["boton",6]]),
(986,"m-traje-vino","Wine Three-Piece",5880,"Abrigo, saco, chaleco y pantalón","Abrigo bordó sobre traje de tres piezas gris. Incluye abrigo, saco, chaleco y pantalón. La corbata y los anteojos son de styling.",[["cashmerePano",2.6],["lana",3.2],["forro",3.4],["entretela",0.8],["gabardina",1.5],["boton",8]]),
(987,"m-blazer-principe","Prince Blazer",3980,"Blazer, sweater y pantalón","Blazer príncipe de gales, sweater verde y pantalón chocolate. Incluye blazer, sweater y pantalón. Los anteojos son de styling.",[["lana",1.8],["forro",1.1],["entretela",0.5],["merino",3],["gabardina",1.5],["boton",2]]),
(988,"m-sobrecamisa-oliva","Olive Overshirt",3480,"Sobrecamisa, sweater y pantalón","Sobrecamisa oliva, sweater de cuello alto y pantalón crudo. Incluye sobrecamisa, sweater y pantalón. Los anteojos son de styling.",[["gabardina",3.3],["merino",3],["boton",4]]),
(989,"m-punto-vino","Wine Cable",3280,"Sweater y pantalón","Sweater de punto trenzado bordó y pantalón crudo. Incluye sweater y pantalón. El bolso es de styling.",[["merino",5],["gabardina",1.5]]),
(990,"m-abrigo-camel","Camel Coat",4980,"Abrigo, sweater y pantalón","Abrigo camel, sweater de cuello alto y pantalón gris. Incluye abrigo, sweater y pantalón. Los anteojos son de styling.",[["cashmerePano",2.6],["forro",1.6],["merino",3],["gabardina",1.5],["boton",4]]),
(991,"m-punto-oliva","Olive Seat",3180,"Sweater y pantalón","Sweater de punto trenzado oliva y pantalón chocolate. Incluye sweater y pantalón. Los anteojos son de styling.",[["merino",5],["gabardina",1.5]]),
(992,"m-capa-navy","Navy Layer",4680,"Abrigo, chaleco, camisa y pantalón","Abrigo azul, chaleco, camisa blanca y pantalón al tono. Incluye abrigo, chaleco, camisa y pantalón. Los anteojos son de styling.",[["lana",3.2],["forro",2.1],["entretela",0.4],["camiseria",1.6],["gabardina",1.5],["boton",8]]),
(993,"m-punto-marfil","Ivory Knit",3280,"Sweater y pantalón","Sweater de punto marfil y pantalón al tono. Incluye sweater y pantalón. La bufanda y los anteojos son de styling.",[["merino",5],["gabardina",1.5]]),
(994,"m-pana-oxido","Rust Cord",3480,"Sobrecamisa, camisa y pantalón","Sobrecamisa de pana óxido, camisa azul y pantalón gris, con cinturón. Incluye sobrecamisa, camisa y pantalón. Los anteojos son de styling.",[["gabardina",3.3],["camiseria",1.6],["boton",8]]),
(995,"m-tweed-gris","Grey Tweed",3980,"Blazer, sweater y pantalón","Blazer de tweed gris, sweater bordó y pantalón crudo. Incluye blazer, sweater y pantalón. Los anteojos son de styling.",[["lana",1.8],["forro",1.1],["entretela",0.5],["merino",3],["gabardina",1.5],["boton",2]]),
(996,"m-abrigo-bosque","Forest Coat",4980,"Abrigo, sweater y pantalón","Abrigo verde bosque, sweater de cuello alto y pantalón chocolate. Incluye abrigo, sweater y pantalón. Los guantes son de styling.",[["cashmerePano",2.6],["forro",1.6],["merino",3],["gabardina",1.5],["boton",2]]),
(997,"m-cuero-chocolate","Chocolate Leather",4280,"Campera, camisa y pantalón","Campera de cuero chocolate, camisa cruda y pantalón oliva, con cinturón. Incluye campera, camisa y pantalón. El portafolio es de styling.",[["cueroNapa",1.4],["forro",0.9],["cierre",1],["camiseria",1.6],["gabardina",1.5],["boton",4]]),
(998,"m-traje-escarlata","Scarlet Suit",4680,"Saco, camisa y pantalón","Traje cruzado escarlata y camisa al tono. Incluye saco, camisa y pantalón. El pañuelo es de styling.",[["lana",3.2],["forro",2.2],["entretela",0.7],["camiseria",1.8],["gabardina",1.5],["boton",8]]),
(999,"m-ante-camel","Camel Suede",3880,"Sobrecamisa, sweater y pantalón","Sobrecamisa de ante camel, sweater de punto y pantalón crudo, con cinturón. Incluye sobrecamisa, sweater y pantalón. El bolso es de styling.",[["cueroNapa",1.3],["forro",0.7],["merino",3],["gabardina",1.5],["boton",4]]),
(1000,"m-traje-salvia","Sage Suit",4480,"Saco, camisa y pantalón","Traje cruzado salvia y camisa cruda. Incluye saco, camisa y pantalón. El pañuelo es de styling.",[["lana",3.2],["forro",2.2],["entretela",0.7],["camiseria",1.8],["gabardina",1.5],["boton",6]]),
(1001,"m-conjunto-marfil","Ivory Set",3480,"Camisa y pantalón","Camisa y pantalón de lino marfil. Incluye camisa y pantalón. La bufanda es de styling.",[["lino",3.4],["boton",6]]),
(1002,"m-camisa-navy","Navy Shirt",3480,"Sobrecamisa, polo y pantalón","Sobrecamisa azul, polo de punto y pantalón crudo. Incluye sobrecamisa, polo y pantalón. Los anteojos son de styling.",[["gabardina",3.1],["merino",2.5],["boton",4]]),
(1003,"m-cruzado-gris","Grey Double",4480,"Saco, sweater y pantalón","Saco cruzado gris, sweater de cuello alto y pantalón al tono. Incluye saco, sweater y pantalón. El portafolio es de styling.",[["lana",2.4],["forro",1.6],["entretela",0.6],["merino",3],["gabardina",1.5],["boton",6]]),
(1004,"m-cuero-habano","Havana Leather",4280,"Campera, camisa y pantalón","Campera de cuero habano, camisa cruda y pantalón al tono, con cinturón. Incluye campera, camisa y pantalón.",[["cueroNapa",1.5],["forro",0.9],["camiseria",1.6],["gabardina",1.5],["boton",4]]),
(1005,"m-polo-carmesi","Crimson Polo",3180,"Polo y pantalón","Polo de punto carmesí y pantalón al tono. Incluye polo y pantalón. El bolso es de styling.",[["merino",3.5],["gabardina",1.5]]),
(1006,"m-safari-salvia","Sage Safari",3680,"Campera y pantalón","Campera safari salvia con cinturón y pantalón crudo. Incluye campera y pantalón. Los anteojos son de styling.",[["gabardina",4.0],["forro",0.6],["boton",6]]),
(1007,"m-trench-camel","Camel Trench",4680,"Trench, camisa y pantalón","Trench camel, camisa blanca y pantalón de lino, con cinturón. Incluye trench, camisa y pantalón. El pañuelo es de styling.",[["gabardina",3.4],["forro",1.6],["camiseria",1.6],["lino",1.5],["boton",8]]),
]

TARGET_W = 2000

def upscale(im):
    w, h = im.size
    while w * 2 < TARGET_W:
        im = im.resize((w * 2, h * 2), Image.Resampling.LANCZOS)
        w, h = im.size
    scale = TARGET_W / w
    im = im.resize((TARGET_W, max(1, round(h * scale))), Image.Resampling.LANCZOS)
    im = ImageEnhance.Contrast(im).enhance(1.04)
    im = ImageEnhance.Color(im).enhance(1.05)
    im = im.filter(ImageFilter.UnsharpMask(radius=1.8, percent=70, threshold=2))
    return im

def crop_all():
    boxes = []
    for path, cols, rows in BOARDS:
        im = Image.open(path).convert("RGB")
        for y0, y1 in rows:
            for x0, x1 in cols:
                boxes.append((im, x0, y0, x1, y1))
    # The seated look's ledge sits above the next row; keep his shoe, drop the head below.
    tighter = {"m-punto-oliva": 496}
    if len(boxes) != len(LOOKS):
        raise SystemExit(f"crops {len(boxes)} looks {len(LOOKS)}")
    cropped = []
    for look, (im, x0, y0, x1, y1) in zip(LOOKS, boxes):
        if look[1] in tighter:
            y1 = tighter[look[1]]
        cropped.append(im.crop((x0, y0, x1, y1)))
    boxes = cropped
    if len(boxes) != len(LOOKS):
        raise SystemExit(f"crops {len(boxes)} looks {len(LOOKS)}")
    for look, im in zip(LOOKS, boxes):
        up = upscale(im)
        up.save(OUT / f"{look[1]}.webp", "WEBP", quality=90, method=6)
        print(look[0], look[1], im.size, "->", up.size)

def js(s):
    return "'" + s.replace("\\", "\\\\").replace("'", "\\'") + "'"

def money(n):
    return f"{n:,}".replace(",", ".")

def patch_index():
    p = ROOT / "index.html"
    text = p.read_text()
    if "colors/m-abrigo-teal" in text:
        raise SystemExit("index already")
    lines = []
    for i, slug, name, price, inc, desc, bom in LOOKS:
        lines.append("{id:%d,g:'M',name:%s,cat:'COLORS',price:%d,img:%s,pos:'center 12%%',desc:%s}," % (
            i, js(name), price, js(f"colors/{slug}.webp?v=1"), js(desc)))
    needle = "\n];let gender"
    if text.count(needle) != 1:
        raise SystemExit("index anchor")
    text = text.replace(needle, "\n" + "\n".join(lines) + needle, 1)
    old = '<article class="collection-card" onclick="filter(\'DAY\')"><img src="assets/men/day_01.webp" alt="Colección Day Men">'
    card = '<article class="collection-card" onclick="filter(\'COLORS\')"><img src="assets/colors/m-abrigo-teal.webp?v=1" alt="Colors 2027 Men" style="object-position:center 12%"><div><h3>Colors 2027</h3><p>Cuarenta looks de hombre.</p><span>DESCUBRIR →</span></div></article>'
    if text.count(old) != 1:
        raise SystemExit("men card")
    text = text.replace(old, card + old, 1)
    p.write_text(text)
    print("index")

def patch_costos():
    p = ROOT / "costos.html"
    text = p.read_text()
    if "colors/m-abrigo-teal" in text:
        raise SystemExit("costos already")
    rows = []
    for i, slug, name, price, inc, desc, bom in LOOKS:
        bom_js = ",".join('["%s", %s]' % (k, q if isinstance(q, int) else q) for k, q in bom)
        rows.append('[%d,%s,%s,%d,%s,%s,[%s],\'M\'],' % (
            i, json.dumps(name, ensure_ascii=False), json.dumps("COLORS"), price,
            json.dumps(f"colors/{slug}.webp?v=1"), json.dumps(inc, ensure_ascii=False), bom_js))
    needle = "].map(([id,name,cat,price,img,includes,bom,g='W'])"
    if text.count(needle) != 1:
        raise SystemExit("costos anchor")
    text = text.replace(needle, "\n" + "\n".join(rows) + "\n" + needle, 1)
    p.write_text(text)
    print("costos")

def patch_moldes():
    p = ROOT / "moldes.html"
    text = p.read_text()
    if "colors/m-abrigo-teal" in text:
        raise SystemExit("moldes already")
    objs, boms = [], []
    for i, slug, name, price, inc, desc, bom in LOOKS:
        objs.append(json.dumps({
            "id": i, "name": name, "cat": "COLORS", "g": "M",
            "img": f"colors/{slug}.webp?v=1", "desc": desc, "accessory": False,
        }, ensure_ascii=False))
        boms.append("  %d:[%s]," % (i, ", ".join('["%s", %s]' % (k, q) for k, q in bom)))
    anchor = '"accessory": false}];'
    if text.count(anchor) != 1:
        raise SystemExit("products anchor " + str(text.count(anchor)))
    text = text.replace(anchor, '"accessory": false},' + ",".join(objs) + "];", 1)
    bom_anchor = "  967:[[\"viscosa\", 2.8]],\n};"
    if bom_anchor not in text:
        raise SystemExit("bom anchor")
    text = text.replace(bom_anchor, "  967:[[\"viscosa\", 2.8]],\n" + "\n".join(boms) + "\n};", 1)
    p.write_text(text)
    print("moldes")

PAGE_CSS = """*{box-sizing:border-box}body{margin:0;background:#f6f3ed;color:#1f1b16;font-family:'DM Sans',system-ui,sans-serif;font-weight:300;line-height:1.6}
a{color:inherit}header,main,footer{max-width:1180px;margin:0 auto;padding:24px}header{display:flex;justify-content:space-between;align-items:center;border-bottom:1px solid #e2dbcf}
.logo{font-family:Italiana,serif;font-size:30px;letter-spacing:.18em;text-decoration:none}.logo small{display:block;font-family:'DM Sans';font-size:9px;letter-spacing:.4em}
h1,h2{font-family:Italiana,serif;font-weight:400;letter-spacing:.04em}h1{font-size:clamp(36px,6vw,64px);margin:.2em 0}.eyebrow{font-size:11px;letter-spacing:.25em;text-transform:uppercase;color:#8a8175}
nav.crumbs{font-size:12px;letter-spacing:.08em;color:#8a8175}nav.crumbs a{text-decoration:none}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(200px,1fr));gap:28px;list-style:none;padding:0}.grid a{text-decoration:none}
.grid img{width:100%;aspect-ratio:3/4;object-fit:contain;background:#efe8dc}.grid h3{font-weight:400;margin:10px 0 0;font-size:16px}.grid span{font-size:13px;color:#8a8175}
.product{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:48px;align-items:start}.product img{width:100%;background:#efe8dc}
.price{font-size:20px;letter-spacing:.06em}.btn{display:inline-block;margin-top:18px;padding:14px 26px;background:#1f1b16;color:#f6f3ed;text-decoration:none;font-size:12px;letter-spacing:.2em}
footer{border-top:1px solid #e2dbcf;font-size:12px;letter-spacing:.12em;color:#8a8175}@media(max-width:760px){.product{grid-template-columns:1fr}}"""

def write_pages():
    items, cards = [], []
    for i, slug, name, price, inc, desc, bom in LOOKS:
        url = f"https://rodrigomeriggi.github.io/grut/productos/{i}-{slug}.html"
        img = f"https://rodrigomeriggi.github.io/grut/assets/colors/{slug}.webp?v=1"
        meta = f"{name}, colección Colors 2027 de GRUT Buenos Aires (Hombre). {desc}"
        im = Image.open(OUT / f"{slug}.webp")
        w, h = im.size
        graph = {"@context": "https://schema.org", "@graph": [
            {"@type": "Organization", "@id": "https://rodrigomeriggi.github.io/grut/#organization", "name": "GRUT", "url": "https://rodrigomeriggi.github.io/grut/"},
            {"@type": "Product", "name": name, "description": desc, "image": img, "sku": f"GRUT-{i}", "category": "Colors 2027", "url": url,
             "brand": {"@type": "Brand", "name": "GRUT"}, "manufacturer": {"@id": "https://rodrigomeriggi.github.io/grut/#organization"},
             "offers": {"@type": "Offer", "price": price, "priceCurrency": "USD", "availability": "https://schema.org/MadeToOrder", "url": url, "seller": {"@id": "https://rodrigomeriggi.github.io/grut/#organization"}},
             "audience": {"@type": "PeopleAudience", "suggestedGender": "male"}},
            {"@type": "BreadcrumbList", "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": "GRUT", "item": "https://rodrigomeriggi.github.io/grut/"},
                {"@type": "ListItem", "position": 2, "name": "Colors 2027 Men", "item": "https://rodrigomeriggi.github.io/grut/colecciones/colors-2027-men.html"},
                {"@type": "ListItem", "position": 3, "name": name, "item": url}]}]}
        ld = json.dumps(graph, ensure_ascii=False, separators=(", ", ": "))
        (ROOT / "productos" / f"{i}-{slug}.html").write_text(f"""<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(name)} — Colors 2027 Men | GRUT Buenos Aires</title>
<meta name="description" content="{html.escape(meta)}">
<link rel="canonical" href="{url}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="GRUT Buenos Aires">
<meta property="og:title" content="{html.escape(name)} — Colors 2027 Men | GRUT Buenos Aires">
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
<nav class="crumbs"><a href="../">GRUT</a> / <a href="../colecciones/colors-2027-men.html">Colors 2027 Men</a> / {html.escape(name)}</nav>
<article class="product">
<img src="../assets/colors/{slug}.webp?v=1" alt="{html.escape(name)} — GRUT Colors 2027 Men" width="{w}" height="{h}">
<div>
<p class="eyebrow">GRUT · Colors 2027 · Hombre</p>
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
        items.append({"@type": "ListItem", "url": url, "name": name})
        cards.append(f'<li><a href="../productos/{i}-{slug}.html"><img loading="lazy" src="../assets/colors/{slug}.webp?v=1" alt="{html.escape(name)}"><h3>{html.escape(name)}</h3><span>Hombre · USD {money(price)}</span></a></li>')
    blurb = "Colors 2027 Men: cuarenta looks de invierno y otoño. Abrigo, sastrería, punto y cuero, con la confección de la maison."
    desc = "Colección Colors 2027 de GRUT Buenos Aires, moda de lujo prêt-à-porter. 40 piezas (Hombre). " + blurb
    for n, it in enumerate(items, 1):
        it["position"] = n
    graph = {"@context": "https://schema.org", "@graph": [
        {"@type": "Organization", "@id": "https://rodrigomeriggi.github.io/grut/#organization", "name": "GRUT", "url": "https://rodrigomeriggi.github.io/grut/"},
        {"@type": "CollectionPage", "name": "GRUT Colors 2027 Men", "url": "https://rodrigomeriggi.github.io/grut/colecciones/colors-2027-men.html", "description": desc,
         "isPartOf": {"@type": "WebSite", "url": "https://rodrigomeriggi.github.io/grut/", "name": "GRUT Buenos Aires"},
         "mainEntity": {"@type": "ItemList", "numberOfItems": 40, "itemListElement": items}},
        {"@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "GRUT", "item": "https://rodrigomeriggi.github.io/grut/"},
            {"@type": "ListItem", "position": 2, "name": "Colors 2027 Men", "item": "https://rodrigomeriggi.github.io/grut/colecciones/colors-2027-men.html"}]}]}
    ld = json.dumps(graph, ensure_ascii=False, separators=(", ", ": "))
    (ROOT / "colecciones" / "colors-2027-men.html").write_text(f"""<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Colors 2027 Men — Colección | GRUT Buenos Aires</title>
<meta name="description" content="{html.escape(desc)}">
<link rel="canonical" href="https://rodrigomeriggi.github.io/grut/colecciones/colors-2027-men.html">
<meta property="og:type" content="website">
<meta property="og:site_name" content="GRUT Buenos Aires">
<meta property="og:title" content="Colors 2027 Men — Colección | GRUT Buenos Aires">
<meta property="og:description" content="{html.escape(desc)}">
<meta property="og:url" content="https://rodrigomeriggi.github.io/grut/colecciones/colors-2027-men.html">
<meta property="og:image" content="https://rodrigomeriggi.github.io/grut/assets/colors/m-abrigo-teal.webp?v=1">
<meta name="twitter:card" content="summary_large_image">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@300;400&family=Italiana&display=swap">
<style>{PAGE_CSS}</style>
<script type="application/ld+json">{ld}</script>
</head>
<body>
<header><a class="logo" href="../">GRUT<small>BUENOS AIRES</small></a><a href="../catalogo.html">Colecciones</a></header>
<main>
<nav class="crumbs"><a href="../">GRUT</a> / <a href="../catalogo.html">Colecciones</a> / Colors 2027 Men</nav>
<p class="eyebrow">GRUT Buenos Aires · Colección · Hombre</p>
<h1>Colors 2027 Men</h1>
<p>{html.escape(blurb)}</p>
<p><a class="btn" href="../?c=COLORS#men">VER LA COLECCIÓN EN LA TIENDA</a></p>
<ul class="grid">
{''.join(cards)}
</ul>
</main>
<footer>GRUT BUENOS AIRES · MODA DE LUJO PRÊT-À-PORTER · PRESENTACIÓN PRIVADA · FABRICACIÓN BAJO PEDIDO · <a href="mailto:atelier@grut.com">atelier@grut.com</a></footer>
</body>
</html>
""")
    cat = (ROOT / "catalogo.html").read_text()
    li = '<li><a href="colecciones/colors-2027.html"><img loading="lazy" src="assets/colors/cape-teal.webp?v=1" alt="GRUT Colors 2027"><h3>Colors 2027</h3><span>50 piezas</span></a></li>'
    add = li + '\n<li><a href="colecciones/colors-2027-men.html"><img loading="lazy" src="assets/colors/m-abrigo-teal.webp?v=1" alt="GRUT Colors 2027 Men"><h3>Colors 2027 Men</h3><span>40 piezas</span></a></li>'
    if "colors-2027-men.html" in cat:
        raise SystemExit("catalog already")
    if li not in cat:
        raise SystemExit("catalog colors")
    cat = cat.replace(li, add, 1)
    cat = cat.replace("Urban Youth, Colors 2027.", "Urban Youth, Colors 2027, Colors 2027 Men.")
    old = '"name": "Colors 2027"}]}'
    new = '"name": "Colors 2027"}, {"@type": "ListItem", "position": 47, "url": "https://rodrigomeriggi.github.io/grut/colecciones/colors-2027-men.html", "name": "Colors 2027 Men"}]}'
    if cat.count(old) != 1:
        raise SystemExit("catalog schema " + str(cat.count(old)))
    cat = cat.replace(old, new, 1)
    (ROOT / "catalogo.html").write_text(cat)
    sm = (ROOT / "sitemap.xml").read_text()
    if "colors-2027-men.html" in sm:
        raise SystemExit("sitemap already")
    urls = ["https://rodrigomeriggi.github.io/grut/colecciones/colors-2027-men.html"]
    urls += [f"https://rodrigomeriggi.github.io/grut/productos/{i}-{slug}.html" for i, slug, *_ in LOOKS]
    block = "\n".join(f"  <url><loc>{u}</loc><lastmod>2026-11-24</lastmod></url>" for u in urls)
    sm = sm.replace("</urlset>", block + "\n</urlset>")
    (ROOT / "sitemap.xml").write_text(sm)
    print("pages", len(LOOKS))

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == "crop":
        crop_all()
    else:
        crop_all()
        patch_index()
        patch_costos()
        patch_moldes()
        write_pages()
