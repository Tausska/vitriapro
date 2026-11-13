"""Génère deux démos complètes : Atelier Camille (coiffeur) et Plomberie Delmas (plombier).
Réutilise le style, les animations et le JS de la démo restaurant (tools/demo_resto.py).
Lancer depuis la racine du dépôt : python3 -I tools/demo_sites.py
"""
import os

here = os.path.dirname(os.path.abspath(__file__))
src = open(os.path.join(here, "demo_resto.py"), encoding="utf-8").read().split("pages = {}")[0]
ns = {}
exec(src, ns)
BASE_CSS, BASE_JS, U, words = ns["CSS"], ns["JS"], ns["U"], ns["words"]

THEMES = {
    "coiffeur": dict(ink="#1f1a1c", cream="#faf5f2", clay="#b5586a", moss="#2b2226", sand="#f1e3df", gold="#e7b4bd", line="#e6d3cf", shadow="rgba(181,88,106,.8)"),
    "plombier": dict(ink="#14202b", cream="#f3f6fa", clay="#e8590c", moss="#12324f", sand="#e1eaf3", gold="#ffb27a", line="#d3dde8", shadow="rgba(232,89,12,.8)"),
}


def theme_css(t):
    th = THEMES[t]
    css = BASE_CSS
    css = css.replace("--ink:#241a16;--cream:#f7f0e6;--clay:#b4532a;--moss:#2f3a2c;--sand:#efe3cf;",
                      f"--ink:{th['ink']};--cream:{th['cream']};--clay:{th['clay']};--moss:{th['moss']};--sand:{th['sand']};")
    css = css.replace("#f0c27a", th["gold"]).replace("rgba(180,83,42,.8)", th["shadow"]).replace("rgba(180,83,42,.18)", th["shadow"].replace(".8)", ".2)"))
    for old in ("#e3d5bd", "#d9c9ad", "#e6d8c0", "#e0d2ba", "#eadfcc", "#e8dcc6"):
        css = css.replace(old, th["line"])
    css = css.replace("#7a5a46", th["moss"]).replace("#3a2a22", th["moss"])
    css = css.replace("repeat(4,1fr);gap:12px", "repeat(3,1fr);gap:12px")
    css = css.replace("../fonts/playfair-display-latin-700-normal.woff2", "../fonts/playfair-display-latin-700-normal.woff2")
    return css


def make_js(cfg):
    js = BASE_JS
    old_slots = "['12:00','12:30','13:00','13:30','19:00','19:30','20:00','20:30','21:00','21:30']"
    assert old_slots in js
    js = js.replace(old_slots, str(cfg["slots"]))
    old_msg = "'Merci '+nm+', votre table pour '+document.getElementById('n').value+' personne(s) est réservée le '+dt+' à '+sel+'. (Démonstration : aucune réservation réelle.)'"
    assert old_msg in js
    js = js.replace(old_msg, cfg["confirm_js"])
    return js


def build(key, cfg):
    out = cfg["dir"]
    os.makedirs(out, exist_ok=True)
    css, js = theme_css(key), make_js(cfg)
    IMG = cfg["img"]
    img = lambda k, w=900: U(IMG[k], w)
    nav = cfg["nav"]

    def hero(im, small, h1, p="", acts="", em=None, s=False):
        cls = "hero s" if s else "hero"
        return (f'<header class="{cls}"><div class="bg" id="bg" style="--im:url({img(im, 1800)})"></div><div class="in"><small>{small}</small>'
                f'<h1>{words(h1, em)}</h1>{f"<p>{p}</p>" if p else ""}{f"<div class=acts>{acts}</div>" if acts else ""}</div></header>')

    def page(fn, title, body, active, desc):
        links = "".join(f'<a href="{h}"{" class=on" if h == active else ""}>{t}</a>' for h, t in nav)
        flinks = "".join(f'<a href="{h}">{t}</a>' for h, t in nav)
        return f"""<!DOCTYPE html>
<html lang="fr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{title} · {cfg['brand']}</title><meta name="robots" content="noindex"><meta name="description" content="{desc}">
<script>document.documentElement.className='js'</script><style>{css}</style></head><body>
<div class="demo">Site de démonstration réalisé par VITRIA PRO. <a href="../index.html">Voir les offres</a></div>
<div class="nav" id="nav"><a class="logo" href="index.html">{cfg['brand']}</a>
<div class="menu-l">{links}<a class="b1 btn" href="rdv.html">{cfg['cta']}</a></div>
<button class="burger" id="bu" aria-label="Menu"><i></i><i></i><i></i></button></div>
{body}
<div class="vp"><div class="rv"><h2>{cfg['band_h']}</h2><p>Ce site est une démonstration. Le vôtre sera fait sur mesure : {cfg['band_p']}</p><a class="btn" href="../rendez-vous.html">Je veux le même site</a></div></div>
<footer class="f"><div class="g"><div><b>{cfg['brand']}</b><p>{cfg['foot_tag']}<br>{cfg['addr']} (adresse fictive)</p></div>
<div><b>Horaires</b><p>{cfg['hours']}</p></div>
<div><b>Le site</b>{flinks}<a href="rdv.html">{cfg['cta']}</a><a href="mentions.html">Mentions légales</a></div></div>
<div class="c">Site de démonstration · Les noms, adresses, numéros et photographies sont fictifs ou illustratifs · Réalisé par VITRIA PRO</div></footer>
<div class="lb" id="lb"><div></div></div>
<script>{js}</script><script src="../track.js" defer></script></body></html>"""

    cta_btn = lambda txt, href: f'<a class="cta btn" href="{href}">{txt}</a>'
    P = {}

    # ---- Accueil
    cards = "".join(
        f'<a class="card rv" href="services.html" style="text-decoration:none;--d:{i * .12}s"><div class="ph2" style="--im:url({img(c[0])})"></div><div class="t"><b>{c[1]}</b><span>{c[2]}</span></div></a>'
        for i, c in enumerate(cfg["cards"]))
    why = "".join(f'<div class="rv" style="--d:{i * .12}s"><b>{w[0]}</b><p>{w[1]}</p></div>' for i, w in enumerate(cfg["why"]))
    P["index.html"] = page("index.html", cfg["home_title"],
        hero(cfg["hero_img"], cfg["hero_small"], cfg["hero_h1"], cfg["hero_p"],
             cta_btn(cfg["cta"], "rdv.html") + f'<a class="cta alt btn" href="services.html">{cfg["services_label"]}</a>', em=cfg["hero_em"]) + f"""
<section><div class="wrap split"><div class="rv"><h2>{cfg['intro_h']}</h2><p class="lead">{cfg['intro_p']}</p><p style="margin-top:18px"><a href="histoire.html" style="color:var(--clay);font-weight:600">{cfg['about_link']} →</a></p></div>
<div class="ph rv" style="--im:url({img(cfg['intro_img'], 1100)});--d:.15s"></div></div></section>
<section class="dark"><div class="wrap"><div class="rv"><h2>{cfg['why_h']}</h2></div><div class="why">{why}</div></div></section>
<section><div class="wrap"><div class="rv tc"><h2>{cfg['cards_h']}</h2><p class="lead">{cfg['cards_p']}</p></div><div class="cards">{cards}</div></div></section>
<section style="background:var(--sand)"><div class="wrap tc"><div class="rv"><h2>{cfg['book_h']}</h2><p class="lead">{cfg['book_p']}</p><a class="cta btn" href="rdv.html" style="display:inline-block">{cfg['cta']}</a></div>
<div class="info"><div class="rv" style="text-align:left"><b>Horaires</b><p>{cfg['hours']}</p></div><div class="rv" style="--d:.12s;text-align:left"><b>Adresse</b><p>{cfg['addr']}<br>Adresse fictive de démonstration</p></div><div class="rv" style="--d:.24s;text-align:left"><b>Contact</b><p>{cfg['phone']}<br><a href="contact.html" style="color:var(--clay);font-weight:600">Nous écrire →</a></p></div></div></div></section>""",
        "index.html", cfg["desc"])

    # ---- Services
    item = lambda n, d, p: f'<div class="it rv"><div><b>{n}</b><span>{d}</span></div><em>{p}</em></div>'
    sb = "".join(f'<div class="cat rv">{c}</div>' + "".join(item(*i) for i in its) for c, its in cfg["menu"])
    P["services.html"] = page("services.html", cfg["services_title"],
        hero(cfg["serv_img"], cfg["serv_small"], cfg["serv_h1"], cfg["serv_p"], s=True) + f"""
<section><div class="wrap"><div class="rv"><h2>{cfg['serv_h2']}</h2><p class="lead">{cfg['serv_lead']}</p></div>
<div class="cols">{sb}</div><p class="note rv">{cfg['serv_note']}</p></div></section>
<section style="background:var(--sand)"><div class="wrap tc"><div class="rv"><h2>{cfg['serv_cta_h']}</h2><a class="cta btn" href="rdv.html" style="display:inline-block">{cfg['cta']}</a></div></div></section>""",
        "services.html", cfg["desc"])

    # ---- Galerie
    gl = "".join(f'<div class="rv" style="--im:url({U(IMG[k], 1000)});--d:{(n % 3) * 0.1}s"></div>' for n, k in enumerate(cfg["gallery"]))
    P["galerie.html"] = page("galerie.html", cfg["gal_title"],
        hero(cfg["gal_img"], cfg["gal_small"], cfg["gal_h1"], s=True) + f"""
<section><div class="wrap"><div class="rv"><h2>{cfg['gal_h2']}</h2><p class="lead">Touchez une photo pour l'agrandir.</p></div><div class="gal">{gl}</div></div></section>""",
        "galerie.html", cfg["desc"])

    # ---- Histoire
    team = "".join(f'<div class="rv" style="--d:{i * .12}s"><b>{m[0]}</b><span style="color:#d9cdb6">{m[1]}</span></div>' for i, m in enumerate(cfg["team"]))
    P["histoire.html"] = page("histoire.html", cfg["about_title"],
        hero(cfg["about_img"], cfg["about_small"], cfg["about_h1"], s=True) + f"""
<section><div class="wrap split"><div class="rv"><h2>{cfg['about_h2']}</h2><p class="lead">{cfg['about_p']}</p></div><div class="ph rv" style="--im:url({img(cfg['about_photo'], 1100)});--d:.15s"></div></div></section>
<section class="dark"><div class="wrap"><div class="rv"><h2>{cfg['team_h']}</h2></div><div class="team">{team}</div></div></section>
<section><div class="wrap tc"><div class="rv"><h2>{cfg['about_cta']}</h2><a class="cta btn" href="rdv.html" style="display:inline-block">{cfg['cta']}</a></div></div></section>""",
        "histoire.html", cfg["desc"])

    # ---- Rendez-vous / devis
    opts = "".join(f"<option>{o}</option>" for o in cfg["options"])
    P["rdv.html"] = page("rdv.html", cfg["rdv_title"],
        hero(cfg["rdv_img"], cfg["rdv_small"], cfg["rdv_h1"], cfg["rdv_p"], s=True) + f"""
<section style="background:var(--sand)"><div class="wrap tc"><div class="rv"><h2>{cfg['rdv_h2']}</h2><p class="lead">{cfg['rdv_lead']}</p></div>
<form class="book rv" id="f" novalidate><label for="d">Date</label><input type="date" id="d"><label for="n">{cfg['opt_label']}</label><select id="n">{opts}</select>
<label>{cfg['slot_label']}</label><div class="slots" id="sl"></div><label for="nm">Nom</label><input id="nm" placeholder="Votre nom" autocomplete="name"><label for="tl">Téléphone</label><input id="tl" type="tel" placeholder="Pour vous joindre si besoin" autocomplete="tel">
<div class="err" id="er"></div><button class="go b1 btn" type="submit">{cfg['submit']}</button><div class="ok" id="ok"></div></form></div></section>""",
        "rdv.html", cfg["desc"])

    # ---- Contact
    P["contact.html"] = page("contact.html", "Contact",
        hero(cfg["contact_img"], "CONTACT", cfg["contact_h1"], s=True) + f"""
<section><div class="wrap"><div class="info"><div class="rv"><b>Adresse</b><p>{cfg['addr']}<br>Adresse fictive de démonstration</p></div><div class="rv" style="--d:.12s"><b>Téléphone</b><p>{cfg['phone']}<br>Numéro fictif de démonstration</p></div><div class="rv" style="--d:.24s"><b>Horaires</b><p>{cfg['hours']}</p></div></div>
<div class="plan rv">{cfg['plan']}</div></div></section>
<section style="background:var(--sand)"><div class="wrap tc"><div class="rv"><h2>Nous écrire</h2><p class="lead">{cfg['contact_lead']}</p></div>
<form class="cform rv" id="cf" novalidate><label for="cn">Nom</label><input id="cn" autocomplete="name"><label for="ce">E-mail</label><input id="ce" type="email" autocomplete="email"><label for="cm">Message</label><textarea id="cm"></textarea>
<div class="err" id="er2"></div><button class="go b1 btn" type="submit">Envoyer le message</button><div class="ok" id="ok2"></div></form></div></section>""",
        "contact.html", cfg["desc"])

    # ---- Mentions
    P["mentions.html"] = page("mentions.html", "Mentions légales",
        hero(cfg["hero_img"], "MENTIONS LÉGALES", "Mentions légales", s=True) + f"""
<section><div class="wrap"><div class="rv"><h2>Site de démonstration</h2><p class="lead">Ce site est une démonstration réalisée par VITRIA PRO. {cfg['brand']} est une entreprise fictive : les noms, adresses, numéros, prestations, prix et photographies sont fictifs ou illustratifs. Sur votre site, cette page contient vos informations légales réelles (raison sociale, adresse, contact, hébergeur, données personnelles).</p></div></div></section>""",
        "", "Mentions légales (démonstration).")

    for fn, html in P.items():
        open(os.path.join(out, fn), "w", encoding="utf-8").write(html)
    print(key, len(P), "pages", sum(len(h) for h in P.values()) // 1024, "Ko")


# ======================= COIFFEUR =======================
COIFFEUR = dict(
    dir="demo-coiffeur", brand="Atelier Camille", cta="Prendre rendez-vous",
    nav=[("index.html", "Accueil"), ("services.html", "Prestations"), ("galerie.html", "Galerie"), ("histoire.html", "Le salon"), ("contact.html", "Contact")],
    img=dict(salon="1560066984-138dadb4c035", styliste="1522337360788-8b13dee7a37e", barbier="1503951914875-452162b0f3f1", s1="1521590832167-7bcbfaa6381f",
             s2="1758611974917-f7f7a58b74b0", couleur="1562322140-8baeececf3df", soin="1605497788044-5a32c7078486", barbe="1580618672591-eb180b1a973f"),
    slots=["09:00", "10:00", "11:00", "12:00", "14:00", "15:00", "16:00", "17:00", "18:00"],
    confirm_js="'Merci '+nm+', votre rendez-vous (' + document.getElementById('n').value + ') est confirmé le '+dt+' à '+sel+'. (Démonstration : aucun rendez-vous réel.)'",
    home_title="Salon de coiffure femme, homme et barbier", desc="Démonstration d'un site de salon de coiffure réalisé par VITRIA PRO.",
    hero_img="salon", hero_small="SALON DE COIFFURE · FEMME · HOMME · BARBIER", hero_h1="Une coupe qui vous ressemble, sans attendre", hero_em=["vous", "ressemble,"],
    hero_p="Coupe, couleur, barbe et soins, sur rendez-vous, dans un salon pensé pour que vous repartiez à l'aise.", services_label="Voir les prestations",
    intro_h="Un salon à taille humaine, une équipe à l'écoute", intro_p="On prend le temps de comprendre votre style, votre rythme et vos cheveux. Pas de coupe standard : une coupe qui se coiffe facilement chez vous, le matin, sans effort.",
    about_link="Découvrir le salon", intro_img="styliste",
    why_h="Pourquoi nos clients reviennent", why=[("Sur rendez-vous", "Vous réservez en ligne, vous arrivez à l'heure, on vous reçoit à l'heure."), ("Des produits choisis", "Des soins professionnels qui respectent le cheveu et le cuir chevelu."), ("Une équipe à l'écoute", "Avant de couper, on écoute. Après, on vous explique comment la coiffer chez vous.")],
    cards_h="Nos prestations phares", cards_p="Les trois que nos clients réservent le plus.",
    cards=[("s1", "Coupe et brushing", "Conseil, coupe, coiffage"), ("couleur", "Couleur et mèches", "Résultat naturel, sans cassure"), ("barbe", "Barbe et rasage", "Taille précise, finition soignée")],
    book_h="Réservez votre rendez-vous", book_p="En quelques secondes, à toute heure, depuis votre téléphone.",
    hours="Mardi au samedi<br>9h – 19h<br>Fermé dimanche et lundi", addr="8 place de la Mairie", phone="01 23 45 67 89",
    services_title="Prestations et tarifs", serv_img="couleur", serv_small="PRESTATIONS ET TARIFS", serv_h1="Nos prestations, nos prix", serv_p="Tarifs clairs, sans mauvaise surprise.",
    serv_h2="Carte des prestations", serv_lead="Chaque prestation comprend le shampoing, le conseil et le coiffage.",
    menu=[("Femme", [("Coupe femme", "Shampoing, coupe, coiffage", "38 €"), ("Brushing", "Mise en forme", "25 €"), ("Coupe et brushing", "Cheveux mi-longs", "52 €")]),
          ("Homme et barbe", [("Coupe homme", "Ciseaux ou tondeuse", "24 €"), ("Barbe", "Taille et finition à la serviette chaude", "16 €"), ("Coupe et barbe", "Formule complète", "36 €"), ("Coupe enfant", "Jusqu'à 12 ans", "15 €")]),
          ("Couleur", [("Couleur", "Racines ou longueurs", "55 €"), ("Mèches", "Balayage ou mèches classiques", "75 €"), ("Patine", "Éclat et correction de nuance", "30 €")]),
          ("Soins", [("Soin profond", "Cheveux secs ou abîmés", "18 €"), ("Soin du cuir chevelu", "Détox et apaisant", "22 €")])],
    serv_note="Tarifs indicatifs de démonstration : prestations et prix fictifs. Merci de nous prévenir en cas d'allergie.", serv_cta_h="Envie d'un nouveau look ?",
    gallery=["salon", "styliste", "barbier", "s1", "couleur", "soin"], gal_img="styliste", gal_small="GALERIE", gal_h1="Le salon, l'équipe, le travail", gal_title="Galerie", gal_h2="En images",
    about_title="Le salon", about_img="s2", about_small="LE SALON", about_h1="Une équipe, un salon, une façon de faire", about_h2="Ouvert pour coiffer autrement",
    about_p="Atelier Camille est né d'une envie : un salon où l'on prend le temps. Trois postes, une équipe qui se connaît, et des clients qui reviennent parce qu'ils savent qu'on les écoute.", about_photo="salon",
    team_h="L'équipe", team=[("Camille", "Fondatrice et coiffeuse"), ("Julien", "Barbier"), ("Inès", "Coloriste")], about_cta="Venez nous rencontrer",
    rdv_title="Rendez-vous", rdv_img="salon", rdv_small="RENDEZ-VOUS", rdv_h1="Prendre rendez-vous", rdv_p="Choisissez la prestation, le jour et l'heure.",
    rdv_h2="Votre rendez-vous en quelques secondes", rdv_lead="Confirmation immédiate. Pour un mariage ou plusieurs personnes, écrivez-nous depuis la page contact.",
    opt_label="Prestation", options=["Coupe femme", "Coupe homme", "Barbe", "Coupe et barbe", "Brushing", "Couleur", "Mèches", "Soin"], slot_label="Heure", submit="Confirmer mon rendez-vous",
    contact_img="s2", contact_h1="Une question ? Écrivez-nous", contact_lead="Mariage, groupe, conseil couleur : nous répondons sous 24 h.", plan="Plan d'accès et itinéraire en un geste<br>(carte intégrée sur votre vrai site)",
    band_h="Vous avez un salon ?", band_p="vos prestations, vos photos, votre ambiance, avec prise de rendez-vous en ligne.", foot_tag="Coiffure femme, homme et barbier.")

# ======================= PLOMBIER =======================
PLOMBIER = dict(
    dir="demo-plombier", brand="Plomberie Delmas", cta="Demander un devis",
    nav=[("index.html", "Accueil"), ("services.html", "Services"), ("galerie.html", "Réalisations"), ("histoire.html", "L'entreprise"), ("contact.html", "Contact")],
    img=dict(atelier="1607472586893-edb57bdc0e39", pro="1758876020337-2501eeb1ede5", tuyaux="1585704032915-c3400ca199e7", plombier="1621905251189-08b45d6a269e",
             sdb="1620626011761-996317b8d101", chantier="1581244277943-fe4a9c908eae"),
    slots=["8h – 10h", "10h – 12h", "14h – 16h", "16h – 18h"],
    confirm_js="'Merci '+nm+', votre demande (' + document.getElementById('n').value + ') est enregistrée pour le '+dt+', créneau '+sel+'. Nous vous rappelons pour confirmer. (Démonstration : aucune demande réelle.)'",
    home_title="Plombier, dépannage et installation", desc="Démonstration d'un site de plombier réalisé par VITRIA PRO.",
    hero_img="tuyaux", hero_small="PLOMBIER · DÉPANNAGE · INSTALLATION", hero_h1="Une fuite ? On intervient vite", hero_em=["fuite ?", "vite"],
    hero_p="Dépannage rapide, devis clair avant intervention, travail propre. Demandez votre devis en deux minutes.", services_label="Voir les services",
    intro_h="Un artisan qui répond, qui vient, qui explique", intro_p="Vous recevez un prix avant le début des travaux, un créneau précis, et un plombier qui laisse l'endroit propre. Pas de mauvaise surprise sur la facture.",
    about_link="Découvrir l'entreprise", intro_img="pro",
    why_h="Pourquoi nous faire confiance", why=[("Réponse rapide", "Vous nous écrivez, on vous rappelle dans l'heure en journée."), ("Devis avant travaux", "Le prix est annoncé avant d'intervenir, sans supplément caché."), ("Travail propre", "On protège, on répare, on nettoie. Vous retrouvez votre intérieur comme avant.")],
    cards_h="Nos interventions les plus demandées", cards_p="Ce pour quoi on nous appelle le plus.",
    cards=[("tuyaux", "Fuite et dépannage", "Recherche et réparation rapide"), ("sdb", "Salle de bains", "Rénovation et pose complète"), ("chantier", "Chauffe-eau et chaudière", "Installation et entretien")],
    book_h="Demandez votre devis", book_p="Décrivez votre besoin, choisissez un créneau : on vous rappelle.",
    hours="Lundi au samedi<br>8h – 19h<br>Urgences : 7j/7 (téléphone)", addr="Zone d'intervention : 30 km autour de la ville", phone="06 12 34 56 78",
    services_title="Services et tarifs", serv_img="atelier", serv_small="SERVICES ET TARIFS", serv_h1="Ce qu'on fait, à quel prix", serv_p="Des prix annoncés à l'avance.",
    serv_h2="Nos services", serv_lead="Chaque intervention commence par un diagnostic et un devis clair.",
    menu=[("Urgences", [("Dépannage fuite d'eau", "Recherche et réparation", "dès 89 €"), ("Débouchage canalisation", "Évier, WC, douche", "dès 79 €"), ("Déplacement et diagnostic", "Déduit si vous commandez les travaux", "49 €")]),
          ("Installation", [("Chauffe-eau", "Pose et mise en service", "sur devis"), ("Salle de bains", "Rénovation complète", "sur devis"), ("Remplacement robinetterie", "Fourniture et pose", "dès 69 €")]),
          ("Entretien", [("Entretien chaudière", "Contrôle annuel", "dès 95 €"), ("Détartrage", "Chauffe-eau et circuits", "dès 85 €")])],
    serv_note="Tarifs indicatifs de démonstration : services et prix fictifs. Devis gratuit et sans engagement.", serv_cta_h="Un problème de plomberie ?",
    gallery=["tuyaux", "sdb", "chantier", "atelier", "plombier", "pro"], gal_img="sdb", gal_small="RÉALISATIONS", gal_h1="Nos chantiers, nos résultats", gal_title="Réalisations", gal_h2="Quelques chantiers",
    about_title="L'entreprise", about_img="chantier", about_small="L'ENTREPRISE", about_h1="Un artisan, une équipe, un engagement", about_h2="Artisan plombier depuis plus de dix ans",
    about_p="Plomberie Delmas, c'est une petite équipe qui intervient en dépannage comme en rénovation. Notre promesse : un prix annoncé avant les travaux, un plombier qui arrive à l'heure, et un chantier laissé propre.", about_photo="plombier",
    team_h="L'équipe", team=[("Marc", "Artisan plombier, gérant"), ("Samir", "Plombier chauffagiste"), ("Léo", "Plombier, urgences")], about_cta="Parlez-nous de votre projet",
    rdv_title="Devis", rdv_img="pro", rdv_small="DEVIS", rdv_h1="Demander un devis", rdv_p="Dites-nous ce qu'il vous faut, on vous rappelle.",
    rdv_h2="Votre demande en quelques secondes", rdv_lead="Pour une urgence (fuite importante), appelez directement le numéro indiqué en bas de page.",
    opt_label="Type d'intervention", options=["Fuite d'eau", "Débouchage", "Chauffe-eau", "Salle de bains", "Robinetterie", "Entretien chaudière", "Autre"], slot_label="Créneau souhaité", submit="Envoyer ma demande",
    contact_img="atelier", contact_h1="Une question ? Contactez-nous", contact_lead="Décrivez votre besoin : nous vous répondons sous 24 h, souvent dans l'heure.", plan="Zone d'intervention et itinéraire en un geste<br>(carte intégrée sur votre vrai site)",
    band_h="Vous êtes plombier ?", band_p="vos services, vos chantiers, vos zones, avec demande de devis directement sur votre téléphone.", foot_tag="Dépannage, installation et entretien.")

build("coiffeur", COIFFEUR)
build("plombier", PLOMBIER)
