#!/usr/bin/env python3
"""Colors 2027: crop each look, upscale, shop, costs, patterns, pages."""
import html
import json
from pathlib import Path
from PIL import Image, ImageFilter, ImageEnhance

ROOT = Path("/Users/rodrigomeriggi/Desktop/GRUT")
SRC = Path("/Users/rodrigomeriggi/.cursor/projects/Users-rodrigomeriggi-Desktop-GRUT/assets")
OUT = ROOT / "assets" / "colors"
OUT.mkdir(parents=True, exist_ok=True)

# (file, column boxes, row boxes) left-to-right, top-to-bottom
BOARDS = [
    (SRC / "Collage_de_moda_GRUT_2027-5dcd64d5-d9f8-4e65-bbcf-5edb482674db.jpg",
     [(2, 196), (200, 375), (379, 559), (563, 749), (753, 933)],
     [(108, 534), (556, 1006)]),
    (SRC / "Lookbook_mediterra_neo_GRUT_2027-819caaf5-cced-4aae-9d50-05a8b31de2b7.jpg",
     [(0, 187), (187, 374), (374, 561), (561, 748), (748, 935)],
     [(130, 558), (562, 1014)]),
    (SRC / "Lookbook_GRUT__Colores_2027-42f2d702-40d7-4ba7-a972-e370a5f91ef7.jpg",
     [(0, 196), (196, 374), (374, 561), (561, 748), (748, 935)],
     [(108, 530), (536, 1006)]),
    (SRC / "GRUT__Colores_2027_en_diez_looks-a24809be-2900-4d3b-a7c5-40722e0eb7bc.jpg",
     [(8, 170), (176, 324), (338, 488), (496, 646), (654, 812)],
     [(156, 586), (598, 1022)]),
    (SRC / "Lookbook_GRUT__Colores_2027__1_-82b26035-3c9b-418a-a12e-d6d0661f4fa9.jpg",
     [(6, 170), (180, 324), (340, 486), (496, 644), (660, 814)],
     [(160, 592), (600, 1022)]),
]

# id, slug, name, price, incluye, desc, bom
LOOKS = [
(918,"cape-teal","Teal Cape",4680,"Abrigo, sweater y pantalón","Abrigo capa verde petróleo sobre sweater de cuello alto crudo y pantalón amplio al tono, con cinturón. Incluye abrigo, sweater y pantalón. Los anteojos y el bolso son de styling.",[["cashmerePano",2.8],["forro",1.8],["merino",4],["gabardina",1.5]]),
(919,"mustard-leather","Mustard Leather",3580,"Campera y pantalón","Campera de cuero mostaza con cierre y cuello alto, y pantalón amplio bordó. Incluye campera y pantalón.",[["cueroNapa",1.3],["forro",0.9],["cierre",1],["gabardina",1.6]]),
(920,"poncho-bordo","Burgundy Poncho",3280,"Poncho y falda","Poncho de punto bordó y falda plisada rosa. Incluye poncho y falda. El bolso es de styling.",[["merino",6],["sedaLisa",2.4]]),
(921,"safari-oliva","Olive Safari",2880,"Camisa y pantalón","Camisa safari oliva con cinturón y pantalón amplio al tono. Incluye camisa y pantalón. Los anteojos son de styling.",[["gabardina",3.2],["boton",8]]),
(922,"trench-navy","Navy Trench",4980,"Trench y sweater","Trench largo de cuero azul, sweater lila y falda blanca. Incluye trench, sweater y falda. Los anteojos y el bolso son de styling.",[["cueroNapa",2.3],["forro",1.6],["jersey",0.5],["gabardina",1.2],["boton",6]]),
(923,"traje-escarlata","Scarlet Suit",4280,"Blazer y pantalón","Traje escarlata de sastrería, blazer y pantalón amplio. Incluye blazer y pantalón. El pañuelo es de styling.",[["lana",3.2],["forro",2.2],["entretela",0.7],["boton",4]]),
(924,"chaqueta-marfil","Ivory Jacket",3680,"Chaqueta, sweater y falda","Chaqueta corta marfil, sweater negro y falda midi de satén teal. Incluye chaqueta, sweater y falda. Los guantes y el bolso son de styling.",[["lana",1.2],["forro",0.8],["boton",4],["jersey",0.4],["saten",1.8]]),
(925,"bomber-teddy","Teddy Bomber",3180,"Campera y pantalón","Bomber de pelo chocolate y pantalón crudo. Incluye campera y pantalón. Los anteojos son de styling.",[["cordero",1.4],["forro",0.9],["cierre",1],["gabardina",1.4]]),
(926,"blusa-violeta","Violet Blouse",2680,"Blusa y pantalón","Blusa de satén violeta con manga globo y pantalón amplio gris, con cinturón. Incluye blusa y pantalón.",[["saten",1.6],["gabardina",1.5]]),
(927,"vestido-chartreuse","Chartreuse Dress",3480,"Vestido","Vestido envolvente verde chartreuse, con tajo y cinturón. Incluye el vestido. El bolso es de styling.",[["saten",2.8],["forro",1.2]]),
(928,"halter-lima","Lime Halter",3280,"Vestido","Vestido halter lima con nudo y tajo. Incluye el vestido. El clutch es de styling.",[["saten",2.6]]),
(929,"camisa-teal","Teal Shirt",2680,"Camisa y pantalón","Camisa de satén teal y pantalón amplio crudo, con cinturón. Incluye camisa y pantalón. Los anteojos y el bolso son de styling.",[["saten",1.6],["gabardina",1.5],["boton",6]]),
(930,"chaleco-floral","Floral Waistcoat",2980,"Chaleco y falda","Chaleco marfil y falda midi con flores rojas. Incluye chaleco y falda.",[["lana",1.0],["forro",0.7],["boton",5],["viscosa",2.4]]),
(931,"camisero-azafran","Saffron Shirtdress",2480,"Vestido","Vestido camisero azafrán con cinturón. Incluye el vestido. El bolso es de styling.",[["camiseria",3.0],["boton",8]]),
(932,"hombro-bordo","Burgundy Shoulder",2480,"Top y pantalón","Top de un hombro bordó y pantalón amplio crudo. Incluye top y pantalón. Los anteojos y el bolso son de styling.",[["saten",1.2],["gabardina",1.5]]),
(933,"blazer-short","Ivory Short",3280,"Blazer, top y short","Blazer marfil, top de punto y short al tono, con cinturón. Incluye blazer, top y short. Los anteojos y el bolso son de styling.",[["lana",1.6],["forro",1.1],["entretela",0.4],["jersey",0.4],["gabardina",0.7],["boton",2]]),
(934,"estampado-turquesa","Turquoise Print",2980,"Vestido","Vestido largo turquesa estampado, con escote en V y manga larga. Incluye el vestido.",[["viscosa",3.2]]),
(935,"slip-coral","Coral Slip",2880,"Top y pantalón","Top slip coral y pantalón palazzo al tono, con lazo. Incluye top y pantalón.",[["saten",2.4]]),
(936,"falda-teal","Teal Wrap",2780,"Top y falda","Top slip marfil y falda envolvente de satén teal, con tajo. Incluye top y falda. El clutch es de styling.",[["saten",2.2]]),
(937,"kimono-palma","Palm Kimono",2680,"Kimono, top y short","Kimono estampado de palmas, top marfil y short al tono, con cinturón. Incluye kimono, top y short. El bolso es de styling.",[["viscosa",2.2],["saten",0.6],["gabardina",0.7]]),
(938,"set-cuero-teal","Teal Leather",5880,"Campera, sweater y pantalón","Campera larga de cuero verde petróleo y pantalón al tono, con sweater. Incluye campera, sweater y pantalón. Los anteojos y el bolso son de styling.",[["cueroNapa",3.2],["forro",2.2],["jersey",0.5],["cierre",1]]),
(939,"trench-mostaza","Mustard Trench",4280,"Trench, sweater y pantalón","Trench mostaza, sweater bordó y pantalón al tono. Incluye trench, sweater y pantalón.",[["gabardina",4.2],["forro",1.8],["merino",3],["boton",8]]),
(940,"tailleur-rojo","Scarlet Tailleur",3980,"Chaqueta y falda","Chaqueta corta roja y falda midi al tono, con tajo. Incluye chaqueta y falda. El bolso es de styling.",[["lana",2.4],["forro",1.6],["entretela",0.5],["boton",4]]),
(941,"vestido-oliva","Olive Gown",3680,"Blusa y falda","Blusa de cuello alto y falda larga oliva, con cinturón. Incluye blusa y falda.",[["saten",3.4]]),
(942,"blusa-lazo","Violet Tie",2680,"Blusa y pantalón","Blusa de satén violeta con lazo y pantalón amplio crudo. Incluye blusa y pantalón. Los anteojos y el bolso son de styling.",[["saten",1.6],["gabardina",1.5]]),
(943,"abrigo-rosa","Blush Coat",5480,"Abrigo, sweater y pantalón","Abrigo largo rosa, sweater bordó y pantalón al tono. Incluye abrigo, sweater y pantalón. Los anteojos son de styling.",[["cashmerePano",2.6],["forro",1.6],["merino",3],["gabardina",1.4],["boton",6]]),
(944,"bomber-cobalto","Cobalt Bomber",3680,"Campera, sweater y falda","Bomber de cuero cobalto, sweater crudo y falda al tono. Incluye campera, sweater y falda. El bolso es de styling.",[["cueroNapa",1.2],["forro",0.8],["cierre",1],["jersey",0.5],["gabardina",1.4]]),
(945,"capa-marfil","Ivory Cape",4280,"Capa, sweater y pantalón","Capa marfil, sweater crudo y pantalón amplio teal. Incluye capa, sweater y pantalón.",[["lanaDobleFaz",2.2],["merino",3],["saten",1.8]]),
(946,"abrigo-lima","Lime Coat",4980,"Abrigo, sweater y pantalón","Abrigo largo lima, sweater violeta y pantalón de cuero. Incluye abrigo, sweater y pantalón. Los anteojos y el bolso son de styling.",[["lana",2.4],["forro",1.6],["merino",3],["cueroNapa",1.5],["boton",4]]),
(947,"mono-camel","Camel Jumpsuit",3880,"Mono","Mono camisero de ante camel, con cinturón. Incluye el mono.",[["cueroNapa",2.6],["forro",1.2],["boton",8]]),
(948,"escultura-roja","Crimson Sculpt",4680,"Chaqueta y pantalón","Chaqueta estructurada roja, de hombros marcados, y pantalón amplio al tono. Incluye chaqueta y pantalón. El bolso es de styling.",[["lana",3.2],["forro",2.0],["entretela",0.8],["boton",2]]),
(949,"plisado-pistacho","Pistachio Pleats",2980,"Blusa y falda","Blusa pistacho y falda midi plisada al tono. Incluye blusa y falda. Los guantes y el bolso son de styling.",[["saten",1.4],["viscosa",2.0],["boton",6]]),
(950,"conjunto-camel","Camel Set",5280,"Abrigo, sweater y falda","Abrigo camel, sweater bordó y falda al tono. Incluye abrigo, sweater y falda. Los anteojos son de styling.",[["cashmerePano",2.6],["forro",1.6],["merino",3],["gabardina",1.3]]),
(951,"mono-marfil","Ivory Wrap",3480,"Mono","Mono marfil de hombros descubiertos, con faja bordó. Incluye el mono. El bolso es de styling.",[["gabardina",3.4]]),
(952,"cargo-oliva","Olive Cargo",2980,"Campera, sweater y pantalón","Campera cargo oliva y pantalón amplio al tono, con sweater bordó. Incluye campera, sweater y pantalón.",[["gabardina",3.4],["jersey",0.5],["boton",6]]),
(953,"drapeado-vino","Wine Drape",3980,"Vestido","Vestido drapeado bordó, de un hombro, con cinturón. Incluye el vestido.",[["sedaLisa",3.2],["forro",1.4]]),
(954,"escultura-menta","Mint Sculpt",3680,"Vestido","Vestido midi menta, de hombros arquitectónicos. Incluye el vestido.",[["gabardina",2.4],["forro",1.4]]),
(955,"abrigo-bufanda","Camel Scarf",4980,"Abrigo, sweater y pantalón","Abrigo camel, sweater con bufanda bordó y pantalón al tono. Incluye abrigo, sweater y pantalón. El bolso es de styling.",[["cashmerePano",2.4],["forro",1.5],["merino",5],["gabardina",1.5]]),
(956,"traje-lila","Lilac Suit",4280,"Blazer, sweater y pantalón","Blazer lila oversized, sweater gris y pantalón amplio al tono, con cinturón. Incluye blazer, sweater y pantalón.",[["lana",3.2],["forro",2.0],["entretela",0.6],["jersey",0.5],["boton",2]]),
(957,"capa-bordo","Burgundy Cape",5480,"Abrigo y sweater","Abrigo capa bordó y sweater de cuello alto al tono, con cinturón. Incluye abrigo y sweater. El bolso es de styling.",[["cashmerePano",2.8],["forro",1.8],["merino",3],["boton",2]]),
(958,"halter-rojo","Scarlet Halter",3880,"Vestido","Vestido halter rojo con panel fluido y cinturón. Incluye el vestido.",[["sedaLisa",3.4],["forro",1.2]]),
(959,"conjunto-mostaza","Mustard Set",3180,"Chaqueta, top y falda","Chaqueta corta mostaza, top blanco y falda plisada al tono. Incluye chaqueta, top y falda. El bolso es de styling.",[["gabardina",1.2],["forro",0.8],["jersey",0.4],["viscosa",1.8],["boton",4]]),
(960,"columna-lima","Lime Column",2980,"Vestido","Vestido columna lima, sin mangas, con drapeado en la cadera. Incluye el vestido.",[["saten",2.4]]),
(961,"lazo-marfil","Ivory Sash",3980,"Blazer, top y pantalón","Blazer marfil, top bordó y pantalón amplio crudo, con lazo. Incluye blazer, top y pantalón.",[["lana",1.8],["forro",1.2],["entretela",0.5],["saten",0.6],["gabardina",1.5],["boton",2]]),
(962,"conjunto-aqua","Aqua Set",3280,"Blusa y pantalón","Blusa de satén aqua y pantalón amplio al tono, con cinturón. Incluye blusa y pantalón. El bolso es de styling.",[["saten",3.0],["boton",6]]),
(963,"cargo-camel","Camel Cargo",2780,"Camisa y pantalón","Camisa cargo de manga corta camel y pantalón amplio al tono. Incluye camisa y pantalón.",[["gabardina",3.2],["boton",6]]),
(964,"chaleco-rosa","Blush Vest",3680,"Chaleco y pantalón","Chaleco rosa y pantalón al tono, con cinturón. Incluye chaleco y pantalón. El bolso es de styling.",[["lana",2.6],["forro",1.6],["entretela",0.4],["boton",4]]),
(965,"camisa-cruda","Cream Layer",2980,"Camisa, sweater y pantalón","Camisa cruda, sweater pistacho sobre los hombros y pantalón amplio al tono. Incluye camisa, sweater y pantalón. El bolso es de styling.",[["camiseria",1.8],["merino",4],["gabardina",1.5],["boton",7]]),
(966,"drapeado-lila","Lilac Drape",2680,"Top y pantalón","Top drapeado lila, de un hombro, y pantalón amplio ciruela, con cinturón. Incluye top y pantalón.",[["saten",1.4],["gabardina",1.6]]),
(967,"halter-hoja","Leaf Halter",3180,"Vestido","Vestido halter crudo con estampado de hojas y drapeado. Incluye el vestido. El bolso es de styling.",[["viscosa",2.8]]),
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

def crop_all(contact=False):
    boxes = []
    for path, cols, rows in BOARDS:
        im = Image.open(path).convert("RGB")
        for y0, y1 in rows:
            for x0, x1 in cols:
                boxes.append(im.crop((x0, y0, x1, y1)))
    if len(boxes) != len(LOOKS):
        raise SystemExit(f"crops {len(boxes)} looks {len(LOOKS)}")
    thumbs = []
    for look, im in zip(LOOKS, boxes):
        up = upscale(im)
        up.save(OUT / f"{look[1]}.webp", "WEBP", quality=90, method=6)
        print(look[0], look[1], im.size, "->", up.size)
        if contact:
            thumbs.append(up.resize((180, round(180 * up.height / up.width)), Image.Resampling.LANCZOS))
    if contact:
        cols_n = 10
        tw, th = thumbs[0].size
        sheet = Image.new("RGB", (cols_n * tw, 5 * th), (246, 243, 237))
        for i, t in enumerate(thumbs):
            sheet.paste(t, ((i % cols_n) * tw, (i // cols_n) * th))
        prev = ROOT / "tools" / "_colors_preview"
        prev.mkdir(exist_ok=True)
        sheet.save(prev / "contact.jpg", quality=85)
        print("contact", sheet.size)

def js(s):
    return "'" + s.replace("\\", "\\\\").replace("'", "\\'") + "'"

def money(n):
    return f"{n:,}".replace(",", ".")

def patch_index():
    p = ROOT / "index.html"
    text = p.read_text()
    if "colors/cape-teal" in text:
        raise SystemExit("index already")
    lines = []
    for i, slug, name, price, inc, desc, bom in LOOKS:
        lines.append("{id:%d,g:'W',name:%s,cat:'COLORS',price:%d,img:%s,pos:'center 12%%',desc:%s}," % (
            i, js(name), price, js(f"colors/{slug}.webp?v=1"), js(desc)))
    needle = "\n];let gender"
    if text.count(needle) != 1:
        raise SystemExit("index anchor")
    text = text.replace(needle, "\n" + "\n".join(lines) + needle, 1)
    old = "<article class=\"collection-card\" onclick=\"filter('WDAY')\">"
    new = "<article class=\"collection-card\" onclick=\"filter('COLORS')\"><img src=\"assets/colors/cape-teal.webp?v=1\" alt=\"Colors 2027\" style=\"object-position:center 12%\"><div><h3>Colors 2027</h3><p>Cincuenta looks de color.</p><span>DESCUBRIR →</span></div></article>" + old
    if text.count(old) != 1:
        raise SystemExit("card")
    text = text.replace(old, new, 1)
    reps = [
        ("<button role=\"menuitem\" onclick=\"filter('WDAY')\">Women's Day</button>",
         "<button role=\"menuitem\" onclick=\"filter('COLORS')\">Colors 2027</button><button role=\"menuitem\" onclick=\"filter('WDAY')\">Women's Day</button>"),
        ("<button onclick=\"toggleMenu();filter('WDAY')\">Women's Day</button>",
         "<button onclick=\"toggleMenu();filter('COLORS')\">Colors 2027</button><button onclick=\"toggleMenu();filter('WDAY')\">Women's Day</button>"),
        ("<button data-cat=\"WDAY\" onclick=\"filter('WDAY')\">Women's Day</button>",
         "<button data-cat=\"COLORS\" onclick=\"filter('COLORS')\">Colors 2027</button><button data-cat=\"WDAY\" onclick=\"filter('WDAY')\">Women's Day</button>"),
    ]
    for a, b in reps:
        if text.count(a) != 1:
            raise SystemExit("nav miss " + a[:50])
        text = text.replace(a, b, 1)
    a = "if(title)title.textContent=c==='WDAY'?'Women\\'s Day':"
    b = "if(title)title.textContent=c==='COLORS'?'Colors 2027':c==='WDAY'?'Women\\'s Day':"
    if text.count(a) != 1:
        raise SystemExit("title fn")
    text = text.replace(a, b, 1)
    a = "if(current==='WDAY'){const n=products.filter(p=>own(p)&&p.cat==='WDAY').length;return 'Women\\'s Day · '+n+' looks'}"
    b = a + "if(current==='COLORS'){const n=products.filter(p=>own(p)&&p.cat==='COLORS').length;return 'Colors 2027 · '+n+' looks'}"
    if text.count(a) != 1:
        raise SystemExit("eyebrow")
    text = text.replace(a, b, 1)
    a = "p.cat==='WDAY'?'Women\\'s Day':"
    if text.count(a) != 2:
        raise SystemExit("cat labels " + str(text.count(a)))
    text = text.replace(a, "p.cat==='COLORS'?'Colors 2027':" + a)
    a = "<a href=\"colecciones/womens-day.html\" onclick=\"event.preventDefault();filter('WDAY');location.hash='shop'\">Women's Day</a>"
    b = "<a href=\"colecciones/colors-2027.html\" onclick=\"event.preventDefault();filter('COLORS');location.hash='shop'\">Colors 2027</a>" + a
    if text.count(a) != 1:
        raise SystemExit("footer")
    text = text.replace(a, b, 1)
    css = ".product-img img[src*=\"colors/\"],.modal>img[src*=\"colors/\"],.cart-item img[src*=\"colors/\"]{object-fit:contain;object-position:center top;width:100%;height:100%;background:#f3efe8}.product:hover .product-img img[src*=\"colors/\"]{transform:none}"
    if "colors/" not in text[text.find("<style>"):text.find("</style>")+20]:
        text = text.replace("</style>", css + "</style>", 1)
    p.write_text(text)
    print("index")

def patch_costos():
    p = ROOT / "costos.html"
    text = p.read_text()
    if "colors/cape-teal" in text:
        raise SystemExit("costos already")
    rows = []
    for i, slug, name, price, inc, desc, bom in LOOKS:
        bom_js = ",".join('["%s", %s]' % (k, q if isinstance(q, int) else q) for k, q in bom)
        rows.append('[%d,%s,%s,%d,%s,%s,[%s],\'W\'],' % (
            i, json.dumps(name, ensure_ascii=False), json.dumps("COLORS"), price,
            json.dumps(f"colors/{slug}.webp?v=1"), json.dumps(inc, ensure_ascii=False), bom_js))
    needle = "].map(([id,name,cat,price,img,includes,bom,g='W'])"
    if text.count(needle) != 1:
        raise SystemExit("costos anchor")
    text = text.replace(needle, "\n" + "\n".join(rows) + "\n" + needle, 1)
    a = "'URBAN','YOUTH','WDAY'"
    if text.count(a) != 1:
        raise SystemExit("costos cats")
    text = text.replace(a, "'URBAN','YOUTH','WDAY','COLORS'", 1)
    a = "c==='WDAY'?'Women\\'s Day':"
    if text.count(a) != 1:
        raise SystemExit("costos label")
    text = text.replace(a, "c==='COLORS'?'Colors 2027':" + a, 1)
    css = ".prod img[src*=\"colors/\"]{object-fit:contain;object-position:center top;background:#f3efe8}"
    text = text.replace(".prod img{width:42px;height:56px;object-fit:cover}",
                        ".prod img{width:42px;height:56px;object-fit:cover}" + css, 1)
    p.write_text(text)
    print("costos")

def patch_moldes():
    p = ROOT / "moldes.html"
    text = p.read_text()
    if "colors/cape-teal" in text:
        raise SystemExit("moldes already")
    objs, boms = [], []
    for i, slug, name, price, inc, desc, bom in LOOKS:
        objs.append(json.dumps({
            "id": i, "name": name, "cat": "COLORS", "g": "W",
            "img": f"colors/{slug}.webp?v=1", "desc": desc, "accessory": False,
        }, ensure_ascii=False))
        boms.append("  %d:[%s]," % (i, ", ".join('["%s", %s]' % (k, q) for k, q in bom)))
    anchor = '"accessory": false}];'
    if text.count(anchor) != 1:
        raise SystemExit("products anchor")
    text = text.replace(anchor, '"accessory": false},' + ",".join(objs) + "];", 1)
    bom_anchor = '  917:[["merino", 5], ["algodon", 1.2], ["gabardina", 1.6]],\n};'
    if bom_anchor not in text:
        raise SystemExit("bom anchor")
    text = text.replace(bom_anchor, '  917:[["merino", 5], ["algodon", 1.2], ["gabardina", 1.6]],\n' + "\n".join(boms) + "\n};", 1)
    a = "'URBAN','YOUTH','WDAY'"
    if text.count(a) < 1:
        raise SystemExit("moldes cats")
    text = text.replace(a, "'URBAN','YOUTH','WDAY','COLORS'")
    text = text.replace("WDAY:'Women\\'s Day'", "WDAY:'Women\\'s Day',COLORS:'Colors 2027'")
    a = "p.cat==='WDAY'?'Women\\'s Day':"
    if text.count(a) != 1:
        raise SystemExit("moldes label " + str(text.count(a)))
    text = text.replace(a, "p.cat==='COLORS'?'Colors 2027':" + a)
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
        meta = f"{name}, colección Colors 2027 de GRUT Buenos Aires (Mujer). {desc}"
        im = Image.open(OUT / f"{slug}.webp")
        w, h = im.size
        graph = {"@context": "https://schema.org", "@graph": [
            {"@type": "Organization", "@id": "https://rodrigomeriggi.github.io/grut/#organization", "name": "GRUT", "url": "https://rodrigomeriggi.github.io/grut/"},
            {"@type": "Product", "name": name, "description": desc, "image": img, "sku": f"GRUT-{i}", "category": "Colors 2027", "url": url,
             "brand": {"@type": "Brand", "name": "GRUT"}, "manufacturer": {"@id": "https://rodrigomeriggi.github.io/grut/#organization"},
             "offers": {"@type": "Offer", "price": price, "priceCurrency": "USD", "availability": "https://schema.org/MadeToOrder", "url": url, "seller": {"@id": "https://rodrigomeriggi.github.io/grut/#organization"}},
             "audience": {"@type": "PeopleAudience", "suggestedGender": "female"}},
            {"@type": "BreadcrumbList", "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": "GRUT", "item": "https://rodrigomeriggi.github.io/grut/"},
                {"@type": "ListItem", "position": 2, "name": "Colors 2027", "item": "https://rodrigomeriggi.github.io/grut/colecciones/colors-2027.html"},
                {"@type": "ListItem", "position": 3, "name": name, "item": url}]}]}
        ld = json.dumps(graph, ensure_ascii=False, separators=(", ", ": "))
        (ROOT / "productos" / f"{i}-{slug}.html").write_text(f"""<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(name)} — Colors 2027 | GRUT Buenos Aires</title>
<meta name="description" content="{html.escape(meta)}">
<link rel="canonical" href="{url}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="GRUT Buenos Aires">
<meta property="og:title" content="{html.escape(name)} — Colors 2027 | GRUT Buenos Aires">
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
<nav class="crumbs"><a href="../">GRUT</a> / <a href="../colecciones/colors-2027.html">Colors 2027</a> / {html.escape(name)}</nav>
<article class="product">
<img src="../assets/colors/{slug}.webp?v=1" alt="{html.escape(name)} — GRUT Colors 2027" width="{w}" height="{h}">
<div>
<p class="eyebrow">GRUT · Colors 2027 · Mujer</p>
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
        cards.append(f'<li><a href="../productos/{i}-{slug}.html"><img loading="lazy" src="../assets/colors/{slug}.webp?v=1" alt="{html.escape(name)}"><h3>{html.escape(name)}</h3><span>Mujer · USD {money(price)}</span></a></li>')
    blurb = "Colors 2027: cincuenta looks de color, de la sastrería al satén y al cuero. Primavera, verano y la paleta de abrigo, con la confección de la maison."
    desc = "Colección Colors 2027 de GRUT Buenos Aires, moda de lujo prêt-à-porter. 50 piezas (Mujer). " + blurb
    for n, it in enumerate(items, 1):
        it["position"] = n
    graph = {"@context": "https://schema.org", "@graph": [
        {"@type": "Organization", "@id": "https://rodrigomeriggi.github.io/grut/#organization", "name": "GRUT", "url": "https://rodrigomeriggi.github.io/grut/"},
        {"@type": "CollectionPage", "name": "GRUT Colors 2027", "url": "https://rodrigomeriggi.github.io/grut/colecciones/colors-2027.html", "description": desc,
         "isPartOf": {"@type": "WebSite", "url": "https://rodrigomeriggi.github.io/grut/", "name": "GRUT Buenos Aires"},
         "mainEntity": {"@type": "ItemList", "numberOfItems": 50, "itemListElement": items}},
        {"@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "GRUT", "item": "https://rodrigomeriggi.github.io/grut/"},
            {"@type": "ListItem", "position": 2, "name": "Colors 2027", "item": "https://rodrigomeriggi.github.io/grut/colecciones/colors-2027.html"}]}]}
    ld = json.dumps(graph, ensure_ascii=False, separators=(", ", ": "))
    (ROOT / "colecciones" / "colors-2027.html").write_text(f"""<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Colors 2027 — Colección | GRUT Buenos Aires</title>
<meta name="description" content="{html.escape(desc)}">
<link rel="canonical" href="https://rodrigomeriggi.github.io/grut/colecciones/colors-2027.html">
<meta property="og:type" content="website">
<meta property="og:site_name" content="GRUT Buenos Aires">
<meta property="og:title" content="Colors 2027 — Colección | GRUT Buenos Aires">
<meta property="og:description" content="{html.escape(desc)}">
<meta property="og:url" content="https://rodrigomeriggi.github.io/grut/colecciones/colors-2027.html">
<meta property="og:image" content="https://rodrigomeriggi.github.io/grut/assets/colors/cape-teal.webp?v=1">
<meta name="twitter:card" content="summary_large_image">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@300;400&family=Italiana&display=swap">
<style>{PAGE_CSS}</style>
<script type="application/ld+json">{ld}</script>
</head>
<body>
<header><a class="logo" href="../">GRUT<small>BUENOS AIRES</small></a><a href="../catalogo.html">Colecciones</a></header>
<main>
<nav class="crumbs"><a href="../">GRUT</a> / <a href="../catalogo.html">Colecciones</a> / Colors 2027</nav>
<p class="eyebrow">GRUT Buenos Aires · Colección</p>
<h1>Colors 2027</h1>
<p>{html.escape(blurb)}</p>
<p><a class="btn" href="../?c=COLORS">VER LA COLECCIÓN EN LA TIENDA</a></p>
<ul class="grid">
{''.join(cards)}
</ul>
</main>
<footer>GRUT BUENOS AIRES · MODA DE LUJO PRÊT-À-PORTER · PRESENTACIÓN PRIVADA · FABRICACIÓN BAJO PEDIDO · <a href="mailto:atelier@grut.com">atelier@grut.com</a></footer>
</body>
</html>
""")
    cat = (ROOT / "catalogo.html").read_text()
    li = '<li><a href="colecciones/womens-day.html"><img loading="lazy" src="assets/wday/city-chic.webp?v=1" alt="GRUT Women\'s Day"><h3>Women\'s Day</h3><span>30 piezas</span></a></li>'
    add = li + '\n<li><a href="colecciones/colors-2027.html"><img loading="lazy" src="assets/colors/cape-teal.webp?v=1" alt="GRUT Colors 2027"><h3>Colors 2027</h3><span>50 piezas</span></a></li>'
    if "colors-2027.html" in cat:
        raise SystemExit("catalog already")
    if li not in cat:
        raise SystemExit("catalog wday")
    cat = cat.replace(li, add, 1)
    cat = cat.replace("Urban, Urban Youth.", "Urban, Urban Youth, Colors 2027.")
    old = '"name": "Urban Youth"}]}'
    new = '"name": "Urban Youth"}, {"@type": "ListItem", "position": 46, "url": "https://rodrigomeriggi.github.io/grut/colecciones/colors-2027.html", "name": "Colors 2027"}]}'
    if cat.count(old) != 1:
        raise SystemExit("catalog schema")
    cat = cat.replace(old, new, 1)
    (ROOT / "catalogo.html").write_text(cat)
    sm = (ROOT / "sitemap.xml").read_text()
    if "colors-2027.html" in sm:
        raise SystemExit("sitemap already")
    urls = ["https://rodrigomeriggi.github.io/grut/colecciones/colors-2027.html"]
    urls += [f"https://rodrigomeriggi.github.io/grut/productos/{i}-{slug}.html" for i, slug, *_ in LOOKS]
    block = "\n".join(f"  <url><loc>{u}</loc><lastmod>2026-11-24</lastmod></url>" for u in urls)
    sm = sm.replace("</urlset>", block + "\n</urlset>")
    (ROOT / "sitemap.xml").write_text(sm)
    print("pages", len(LOOKS))

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == "crop":
        crop_all(contact=True)
    else:
        crop_all(contact=True)
        patch_index()
        patch_costos()
        patch_moldes()
        write_pages()
