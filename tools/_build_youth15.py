#!/usr/bin/env python3
"""Crops the Youth 15 Years boards and registers the looks in shop, costs and patterns."""
import json
from pathlib import Path
from PIL import Image, ImageFilter

ROOT = Path("/Users/rodrigomeriggi/Desktop/GRUT")
SRC = Path("/Users/rodrigomeriggi/.cursor/projects/Users-rodrigomeriggi-Desktop-GRUT/assets")
OUT = ROOT / "assets" / "youth15"
OUT.mkdir(parents=True, exist_ok=True)

BOARDS = [
    (SRC / "Cata_logo_juvenil_GRUT__estilo_y_aventura-2f81e330-690b-4482-9805-f99d88b8dff8.jpg",
     [(0, 204), (206, 409), (411, 616), (618, 821), (823, 1024)],
     [(2, 250), (390, 616)]),
    (SRC / "Coleccio_n_juvenil_GRUT__Estilo_y_actitud-ef5fab13-765b-4568-b031-cb4b4cffb099.jpg",
     [(0, 203), (206, 408), (410, 615), (617, 821), (824, 1024)],
     [(112, 342), (392, 608)]),
    (SRC / "Cata_logo_GRUT__Estilo_juvenil_cinematogra_fico-de0729b2-406b-4533-a3e1-724f0fe5c004.jpg",
     [(0, 204), (206, 409), (411, 614), (616, 819), (821, 1024)],
     [(108, 342), (388, 626)]),
    (SRC / "Lookbook_GRUT__Di_a_y_Noche-e4d5db95-433a-4760-9573-60b66752b1cf.jpg",
     [(6, 206), (214, 410), (418, 612), (619, 816), (823, 1018)],
     [(64, 326), (404, 690)]),
]

# id, slug, name, price, incluye (costos), desc, bom
LOOKS = [
(838,"campus-club","Campus Club",2880,"Campera, remera y pantalón",
 "Campera varsity navy y crudo con letra G, remera blanca y pantalón beige. Incluye campera, remera y pantalón.",
 [["lana",1.5],["cueroNapa",0.7],["jersey",0.7],["gabardina",1.4],["boton",6],["cierre",1]]),
(839,"urban-tech","Urban Tech",1980,"Hoodie y pantalón",
 "Hoodie gris oversized con logo GRUT y pantalón claro. Incluye hoodie y pantalón. Los auriculares son de styling.",
 [["felpa",2.2],["jersey",0.5],["gabardina",1.5],["elastico",1.2],["cordon",1.2]]),
(840,"racing-club","Racing Club",3280,"Campera, remera y pantalón",
 "Campera racing roja y cruda con logo GRUT, remera blanca y pantalón negro. Incluye campera, remera y pantalón. Los anteojos son de styling.",
 [["gabardina",3.0],["cueroNapa",0.3],["forro",1.2],["jersey",0.6],["cierre",1]]),
(841,"resort-day","Resort Day",1780,"Camisa y pantalón",
 "Camisa de lino beige con mangas arremangadas y pantalón claro. Incluye camisa y pantalón. Los anteojos son de styling.",
 [["lino",2.8],["boton",8]]),
(842,"sport-luxe","Sport Luxe",1680,"Remera y short",
 "Remera deportiva negra con vivo blanco y letra G, y short negro. Incluye remera y short. La gorra y la raqueta son de styling.",
 [["jersey",1.3],["elastico",0.6]]),
(843,"outdoor-explorer","Outdoor Explorer",2680,"Campera y pantalón",
 "Campera técnica oliva con capucha y pantalón beige. Incluye campera y pantalón. La mochila es de styling.",
 [["gabardina",3.4],["forro",1.2],["cierre",1],["cordon",1]]),
(844,"crudo-set","Crudo Set",2180,"Hoodie y pantalón",
 "Sweatshirt oversized crudo con logo GRUT y pantalón relajado al tono. Incluye hoodie y pantalón.",
 [["felpa",3.4],["elastico",1.5],["cordon",1.2]]),
(845,"denim-icon","Denim Icon",2480,"Campera, remera y jean",
 "Campera de denim, remera blanca y jean. Incluye campera, remera y jean.",
 [["denim",2.8],["jersey",0.6],["boton",6]]),
(846,"night-club","Night Club",1980,"Camisa y pantalón",
 "Camisa navy con logo G y pantalón negro. Incluye camisa y pantalón. Los anteojos son de styling.",
 [["camiseria",2.2],["gabardina",1.4],["boton",8]]),
(847,"weekend-travel","Weekend Travel",2580,"Chaleco y sweater",
 "Chaleco puffer crudo con letra G y sweater navy. Incluye chaleco y sweater. La mochila es de styling.",
 [["gabardina",1.1],["plumon",0.45],["forro",0.8],["merino",5],["cierre",1]]),
(848,"varsity-heritage","Varsity Heritage",2980,"Campera, remera y pantalón",
 "Campera varsity crudo y bordó con letra G, remera y pantalón beige. Incluye campera, remera y pantalón. La mochila es de styling.",
 [["lana",1.5],["cueroNapa",0.75],["jersey",0.6],["gabardina",1.4],["boton",6]]),
(849,"street-core","Street Core",1780,"Hoodie y pantalón",
 "Hoodie negro con logo GRUT y pantalón negro. Incluye hoodie y pantalón. La gorra es de styling.",
 [["felpa",2.2],["gabardina",1.5],["elastico",1],["cordon",1.2]]),
(850,"f1-garage","F1 Garage",3480,"Campera, remera y pantalón",
 "Campera racing cruda y roja con logo GRUT, remera negra y pantalón negro. Incluye campera, remera y pantalón. Los anteojos son de styling.",
 [["gabardina",2.2],["cueroNapa",0.35],["forro",1.2],["jersey",0.6],["cierre",1]]),
(851,"tennis-club","Tennis Club",2280,"Sweater y pantalón",
 "Sweater de punto crudo con vivo navy y letra G, y pantalón claro. Incluye sweater y pantalón. El bolso es de styling.",
 [["merino",7],["gabardina",1.4]]),
(852,"sailing-crew","Sailing Crew",2480,"Campera y remera",
 "Rompevientos navy con logo GRUT y remera blanca. Incluye campera y remera.",
 [["gabardina",2.2],["forro",1.0],["jersey",0.6],["cierre",1],["cordon",0.8]]),
(853,"alpine-season","Alpine Season",3380,"Campera y sweater",
 "Campera puffer cruda y sweater navy. Incluye campera y sweater. Los anteojos son de styling.",
 [["gabardina",2.2],["plumon",1],["forro",1.6],["merino",4],["cierre",2]]),
(854,"city-tailor","City Tailor",2880,"Blazer, camisa y pantalón",
 "Blazer navy con letra G, camisa celeste y pantalón beige. Incluye blazer, camisa y pantalón.",
 [["lana",2.2],["forro",1.4],["entretela",0.6],["camiseria",1.8],["gabardina",1.4],["boton",8]]),
(855,"resort-linen","Resort Linen",1880,"Camisa y pantalón",
 "Camisa de lino verde oliva y pantalón claro. Incluye camisa y pantalón. Los anteojos son de styling.",
 [["lino",2.6],["boton",7]]),
(856,"night-out","Night Out",3480,"Blazer, camisa y pantalón",
 "Traje negro: blazer, camisa negra y pantalón. Incluye blazer, camisa y pantalón.",
 [["lana",2.8],["forro",1.6],["entretela",0.7],["camiseria",1.6],["boton",6]]),
(857,"active-training","Active Training",1980,"Remera y pantalón",
 "Conjunto deportivo gris con cierre y logo GRUT. Incluye remera y pantalón.",
 [["jersey",1.6],["gabardina",1.6],["elastico",1.2],["cierre",1]]),
(858,"beach-club","Beach Club",1880,"Camisa y short",
 "Camisa calada cruda y short de baño estampado. Incluye camisa y short. Los anteojos son de styling.",
 [["redRustica",1.6],["bano",0.5]]),
(859,"winter-lodge","Winter Lodge",3680,"Campera",
 "Campera de ski cruda y navy, con capucha. Incluye la campera. Los anteojos son de styling.",
 [["gabardina",2.6],["plumon",1],["forro",2.0],["cierre",2]]),
(860,"music-festival","Music Festival",1680,"Remera y pantalón",
 "Remera oversized negra con estampa y pantalón gris. Incluye remera y pantalón. La cadena es de styling.",
 [["jersey",1.2],["gabardina",1.4]]),
(861,"creative-lab","Creative Lab",2780,"Campera, remera y pantalón",
 "Campera de lona pintada, remera blanca y pantalón beige. Incluye campera, remera y pantalón. Los auriculares son de styling.",
 [["gabardina",3.2],["jersey",0.6],["boton",6]]),
(862,"road-trip","Road Trip",3280,"Campera, remera y pantalón",
 "Campera de ante chocolate, remera blanca y pantalón beige. Incluye campera, remera y pantalón. Los anteojos son de styling.",
 [["cueroNapa",1.6],["forro",1.2],["jersey",0.6],["gabardina",1.4],["cierre",1]]),
(863,"yacht-club","Yacht Club",2980,"Blazer, remera y pantalón",
 "Blazer navy con botones dorados y ancla, remera a rayas y pantalón blanco. Incluye blazer, remera y pantalón.",
 [["lana",2.0],["forro",1.3],["entretela",0.5],["botonOro",6],["jersey",0.8],["gabardina",1.3]]),
(864,"golf-elite","Golf Elite",1780,"Polo y pantalón",
 "Polo beige con letra G y pantalón claro. Incluye polo y pantalón. La gorra y el guante son de styling.",
 [["jersey",1.1],["gabardina",1.3],["boton",3]]),
(865,"night-dinner","Night Dinner",2280,"Camisa y pantalón",
 "Camisa oscura estampada y pantalón negro. Incluye camisa y pantalón.",
 [["viscosa",2.0],["gabardina",1.4],["boton",7]]),
(866,"art-gallery","Art Gallery",3180,"Blazer y sweater",
 "Blazer crudo y sweater negro de cuello alto. Incluye blazer y sweater.",
 [["lana",2.2],["forro",1.4],["entretela",0.6],["merino",4],["boton",2]]),
(867,"private-event","Private Event",4480,"Smoking, camisa y pantalón",
 "Smoking de terciopelo bordó con solapa satinada, camisa blanca y moño. Incluye smoking, camisa y pantalón.",
 [["terciopelo",2.4],["forro",1.6],["entretela",0.8],["camiseria",1.8],["saten",0.3],["boton",4],["cinta",0.4]]),
(868,"city-hang","City Hang",2080,"Sweater y jean",
 "Sweater a rayas navy y crudo, y jean wide leg. Incluye sweater y jean. La skate es de styling.",
 [["algodon",6],["denim",1.8]]),
(869,"skate-cargo","Skate Cargo",1980,"Hoodie y cargo",
 "Hoodie verde oversized con logo GRUT y pantalón cargo beige. Incluye hoodie y cargo.",
 [["felpa",2.4],["gabardina",2.0],["elastico",1.2],["cordon",1.2]]),
(870,"creative-cafe","Creative Cafe",1880,"Camisa y pantalón",
 "Sobrecamisa beige y pantalón amplio marrón. Incluye camisa y pantalón. Los auriculares son de styling.",
 [["lino",1.8],["gabardina",1.6],["boton",6]]),
(871,"weekend-walk","Weekend Walk",2480,"Campera, remera y jean",
 "Bomber navy, remera blanca y jean baggy. Incluye campera, remera y jean.",
 [["gabardina",1.6],["forro",1.0],["denim",1.8],["jersey",0.4],["cierre",1]]),
(872,"arcade-shift","Arcade Shift",1580,"Remera y short",
 "Remera gris en capas y short cargo. Incluye remera y short. Los auriculares son de styling.",
 [["jersey",1.4],["gabardina",0.8],["elastico",0.5]]),
(873,"beat-drop","Beat Drop",1880,"Camisa y pantalón",
 "Camisa negra oversized y pantalón sastre amplio. Incluye camisa y pantalón. La cadena es de styling.",
 [["camiseria",2.2],["gabardina",1.6],["boton",6]]),
(874,"house-party","House Party",2280,"Sweater y jean",
 "Sweater bordó con llamas y jean oscuro. Incluye sweater y jean.",
 [["merino",6],["denim",1.6]]),
(875,"dance-floor","Dance Floor",2380,"Campera y pantalón",
 "Campera corta gris y pantalón cargo amplio. Incluye campera y pantalón.",
 [["gabardina",3.2],["forro",0.8],["jersey",0.4],["cierre",1]]),
(876,"late-city","Late City",2680,"Campera, remera y pantalón",
 "Campera oversized negra sobre hoodie gris y pantalón amplio. Incluye campera, remera y pantalón.",
 [["gabardina",3.6],["forro",1.2],["felpa",1.4],["cierre",1],["elastico",0.8]]),
(877,"after-midnight","After Midnight",1980,"Remera y pantalón",
 "Remera roja GRUT 15 y pantalón cargo verde. Incluye remera y pantalón.",
 [["jersey",1.3],["gabardina",2.0],["elastico",0.8]]),
]

def crop_all():
    boxes = []
    for path, cols, rows in BOARDS:
        im = Image.open(path).convert("RGB")
        for y0, y1 in rows:
            for x0, x1 in cols:
                boxes.append(im.crop((x0 + 1, y0, x1 - 1, y1)))
    assert len(boxes) == len(LOOKS)
    for look, im in zip(LOOKS, boxes):
        w, h = im.size
        scale = 1000 / w
        up = im.resize((1000, max(1, round(h * scale))), Image.Resampling.LANCZOS)
        up = up.filter(ImageFilter.UnsharpMask(radius=1.3, percent=70, threshold=3))
        dest = OUT / f"{look[1]}.webp"
        up.save(dest, "WEBP", quality=86, method=6)
        print(f"{look[0]} {look[1]} {w}x{h} -> {up.size}")

def js_str(s):
    return "'" + s.replace("\\", "\\\\").replace("'", "\\'") + "'"

def patch_index():
    p = ROOT / "index.html"
    text = p.read_text()
    lines = []
    for i, slug, name, price, inc, desc, bom in LOOKS:
        img = f"youth15/{slug}.webp?v=1"
        lines.append(
            "{id:%d,g:'M',name:%s,cat:'YOUTH',price:%d,img:%s,pos:'center 15%%',desc:%s},"
            % (i, js_str(name), price, js_str(img), js_str(desc))
        )
    block = "\n" + "\n".join(lines) + "\n"
    needle = "\n];let gender"
    if text.count(needle) != 1:
        raise SystemExit("index anchor count " + str(text.count(needle)))
    if "youth15/campus-club" in text:
        raise SystemExit("index already patched")
    text = text.replace(needle, block + "];let gender", 1)
    old = "Segunda cápsula de GRUT Urban, para jóvenes de 17 a 22 años, con una estética más deportiva, relajada y juvenil. Algodón Supima, denim japonés, cuero napa liviano, punto técnico y tejidos deportivos premium. La calidad y la exclusividad de GRUT, en clave de streetwear. Tocá la imagen para ver la campaña."
    new = "Cápsula 2027 y Youth Collection 15 Years: cuarenta looks de hombre en cuatro volúmenes, de campus, cancha y viaje a la noche y al streetwear. Algodón Supima, denim, napa, punto y pluma, con la misma confección de la maison. Tocá la imagen para ver la campaña."
    if old not in text:
        raise SystemExit("intro not found")
    text = text.replace(old, new, 1)
    text = text.replace(
        'alt="GRUT Urban Youth Collection 2027, diez looks"',
        'alt="GRUT Youth Collection, cápsula 2027 y 15 Years"',
        1,
    )
    text = text.replace(
        'src="assets/youth/street.webp?v=1" alt="Urban Youth" style="object-position:center top"><div><h3>Urban Youth</h3><p>Next Generation 2027.</p>',
        'src="assets/youth15/campus-club.webp?v=1" alt="Youth 15 Years" style="object-position:center 15%"><div><h3>Urban Youth</h3><p>15 Years · Vol. I–IV.</p>',
        1,
    )
    p.write_text(text)
    print("index patched")

def patch_costos():
    p = ROOT / "costos.html"
    text = p.read_text()
    rows = []
    for i, slug, name, price, inc, desc, bom in LOOKS:
        img = f"youth15/{slug}.webp?v=1"
        bom_js = ",".join('["%s", %s]' % (k, q if isinstance(q, int) else q) for k, q in bom)
        rows.append('[%d,%s,\'YOUTH\',%d,%s,%s,[%s],\'M\'],' % (i, json.dumps(name, ensure_ascii=False), price, json.dumps(img), json.dumps(inc, ensure_ascii=False), bom_js))
    needle = "].map(([id,name,cat,price,img,includes,bom,g='W'])"
    if text.count(needle) != 1:
        raise SystemExit("costos anchor")
    if "youth15/campus-club" in text:
        raise SystemExit("costos already")
    text = text.replace(needle, "\n" + "\n".join(rows) + "\n" + needle, 1)
    p.write_text(text)
    print("costos patched")

def patch_moldes():
    p = ROOT / "moldes.html"
    text = p.read_text()
    if "youth15/campus-club" in text:
        raise SystemExit("moldes already")
    objs = []
    boms = []
    for i, slug, name, price, inc, desc, bom in LOOKS:
        obj = {
            "id": i, "name": name, "cat": "YOUTH", "g": "M",
            "img": f"youth15/{slug}.webp?v=1", "desc": desc, "accessory": False,
        }
        objs.append(json.dumps(obj, ensure_ascii=False))
        bom_js = ", ".join('["%s", %s]' % (k, q) for k, q in bom)
        boms.append("  %d:[%s]," % (i, bom_js))
    # PRODUCTS closes on the Saint-Germain object
    anchor = '{"id": 836, "name": "Saint-Germain"'
    i = text.find(anchor)
    if i < 0:
        raise SystemExit("products anchor missing")
    j = text.find("}];", i)
    if j < 0:
        raise SystemExit("products end missing")
    text = text[:j] + "}," + ",".join(objs) + text[j+1:]
    # BOM: add comma to 786 if needed and insert before closing
    bom_anchor = '  786:[["cuero", 2.2], ["forro", 1.4], ["saten", 2.2], ["lana", 1.6], ["cierre", 1], ["boton", 8]]\n};'
    if bom_anchor not in text:
        raise SystemExit("bom anchor missing")
    repl = '  786:[["cuero", 2.2], ["forro", 1.4], ["saten", 2.2], ["lana", 1.6], ["cierre", 1], ["boton", 8]],\n' + "\n".join(boms) + "\n};"
    text = text.replace(bom_anchor, repl, 1)
    p.write_text(text)
    print("moldes patched")

if __name__ == "__main__":
    crop_all()
    patch_index()
    patch_costos()
    patch_moldes()
