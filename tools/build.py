"""Génère les pages intérieures VITRIA PRO dans le style de la nouvelle page d'accueil.
Usage : python3 tools/build.py  (depuis la racine du dépôt)"""
import html

WA = "https://wa.me/595992666002?text="
WA_PROJET = WA + "Bonjour%20VITRIA%20PRO%2C%20je%20souhaite%20parler%20de%20mon%20projet."
UNS = "https://images.unsplash.com/{}?auto=format&fit=crop&w=2000&q=85"

HEAD = """<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="icon" href="favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Inter+Tight:wght@500;600;700&family=Instrument+Serif:ital@0;1&display=swap" rel="stylesheet">
<link rel="stylesheet" href="vitria.css">
</head>
<body>
<header class="header" id="header">
 <div class="wrap nav">
  <a class="brand" href="index.html" aria-label="VITRIA PRO"><img src="logo-vitria-pro.png" alt="VITRIA PRO"></a>
  <nav class="menu">
   <a href="index.html#secteurs">Secteurs</a>
   <a href="index.html#offres">Offres</a>
   <a href="realisations.html">Réalisations</a>
   <a href="garantie.html">Garantie</a>
  </nav>
  <div class="nav-cta"><a class="wa" href="{wa}"><svg class="wai" viewBox="0 0 24 24" width="18" height="18" aria-hidden="true"><path fill="currentColor" d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413Z"/></svg>Contacter</a><a class="btn" href="rendez-vous.html">Être appelé</a></div>
 </div>
</header>
<main>
"""

FOOT = """</main>
@@FOOTER@@
<div class="mbar" id="mbar"><a href="rendez-vous.html">Être appelé</a><a href="{wa}">Contacter</a></div>
<script>
const io=new IntersectionObserver(es=>es.forEach(e=>{{if(e.isIntersecting){{e.target.classList.add('in');io.unobserve(e.target)}}}}),{{threshold:.12}});
document.querySelectorAll('.rv').forEach(el=>io.observe(el));
const h=document.getElementById('header'),m=document.getElementById('mbar');
function onScroll(){{h.classList.toggle('solid',scrollY>200);m.classList.toggle('show',scrollY>500)}}
addEventListener('scroll',onScroll,{{passive:true}});onScroll();
</script>
{extra}
<script src="track.js" defer></script>
</body>
</html>
"""


ICO = '<svg class="wai" viewBox="0 0 24 24" width="18" height="18" aria-hidden="true"><path fill="currentColor" d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413Z"/></svg>'
FOOTER = open("tools/footer.html").read().replace("@@WA@@", WA_PROJET).replace("@@ICO@@", ICO)


def page(title, desc, body, extra=""):
    return (HEAD.format(title=title, desc=desc, wa=WA_PROJET) + body + FOOT.format(wa=WA_PROJET, extra=extra)).replace("@@FOOTER@@", FOOTER)


def hero(eyebrow, h1, lead, ctas, note="", photo=None, stats=""):
    ph = f'<div class="photo" style="background-image:url({UNS.format(photo)})"></div>' if photo else ""
    c = "".join(ctas)
    n = f'<p class="note">{note}</p>' if note else ""
    return f"""<section class="page-hero">{ph}
 <div class="wrap">
  <span class="eyebrow">{eyebrow}</span>
  <h1>{h1}</h1>
  <p class="lead">{lead}</p>
  <div class="cta">{c}</div>{n}{stats}
 </div>
</section>
"""


def btn(text, href, cls="btn-white"):
    return f'<a class="btn {cls}" href="{href}">{text}</a>'


def head(eyebrow, h2, p="", mid=True):
    pp = f"<p>{p}</p>" if p else ""
    return f'<div class="sec-head rv" style="margin-bottom:0"><div><span class="eyebrow">{eyebrow}</span><h2 class="{"mid" if mid else ""}">{h2}</h2></div>{pp}</div>'


def cards(items, cls=""):
    out = "".join(f'<div class="c rv"><span class="n">{n}</span><h3>{t}</h3><p>{p}</p></div>' for n, t, p in items)
    return f'<div class="cards3 {cls}">{out}</div>'


def faq(items):
    return '<div class="faq-list rv">' + "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in items) + "</div>"


# ---------- Pages secteur ----------
STEPS = [("01", "Un appel de 15 minutes", "Vous présentez votre activité et vos clients. Nous nous occupons du reste."),
         ("02", "Votre maquette", "Vous validez votre futur site, à votre nom, avant sa mise en ligne."),
         ("03", "En ligne en 5 jours, ou 48 h", "Textes, design, mobile et Google : votre site est prêt à recevoir vos premiers appels.")]

OFFERS = """<section class="section" id="offre"><div class="wrap">
 <div class="sec-head rv" style="margin-bottom:0"><div><span class="eyebrow">Offres</span><h2 class="mid">Un prix clair. <em>Une seule fois.</em></h2></div><p>Livraison en 5 jours incluse. Besoin d'aller plus vite ? L'Express met votre site en ligne en 48 heures.</p></div>
 <div class="offers">
  <div class="offer rv"><div class="offer-tag"><span>01</span></div><h3>Essentiel</h3><p class="sub">Pour être trouvé et appelé.</p><div class="price">990 €</div><div class="once">Paiement unique</div><ul><li>Site one-page haut de gamme</li><li>Textes rédigés pour vous</li><li>Appel et contact en un geste</li><li>Référencement local de base</li><li>Fiche Google Business configurée</li><li>7 jours de suivi après la mise en ligne</li></ul><div class="express"><span>Option Express 48 h</span><b>+199 €</b></div><a class="btn btn-line" href="rendez-vous.html">Réserver mon appel</a></div>
  <div class="offer feat rv"><div class="offer-tag"><span>02</span><span>Le plus choisi</span></div><h3>Business</h3><p class="sub">Pour présenter chaque service.</p><div class="price">1 490 €</div><div class="once">Paiement unique</div><ul><li>Jusqu'à 5 pages</li><li>Une page par service, rédigée pour vous</li><li>Formulaire de demande de devis</li><li>Référencement local optimisé</li><li>Fiche Google Business configurée</li><li>14 jours de suivi après la mise en ligne</li></ul><div class="express"><span>Option Express 48 h</span><b>+199 €</b></div><a class="btn" href="rendez-vous.html">Réserver mon appel</a></div>
  <div class="offer rv"><div class="offer-tag"><span>03</span></div><h3>Premium</h3><p class="sub">Pour s'imposer dans son secteur.</p><div class="price">2 490 €</div><div class="once">Paiement unique</div><ul><li>Jusqu'à 10 pages</li><li>Sections sur mesure et galerie</li><li>Formulaire de demande de devis</li><li>Référencement local optimisé</li><li>Fiche Google Business configurée</li><li>30 jours de suivi après la mise en ligne</li></ul><div class="express"><span>Option Express 48 h</span><b>+199 €</b></div><a class="btn btn-line" href="rendez-vous.html">Réserver mon appel</a></div>
 </div>
 <div class="all rv"><h4>Dans toutes les offres</h4><p>Nom de domaine et hébergement inclus pendant 3 ans · Adresse e-mail professionnelle · Mentions légales et RGPD · Inscription sur Google · Design adapté au mobile · Site qui vous appartient · Garantie satisfait ou remboursé 14 jours</p></div>
</div></section>
"""


P_A = "photo-1758611974917-f7f7a58b74b0"
P_B = "photo-1752650735119-8929e5f7d1ec"
P_C = "photo-1758876020337-2501eeb1ede5"


def human(photo, eyebrow="Parlons de votre activité"):
    img = UNS.replace("w=2000", "w=1100").format(photo)
    return f"""<section class="hband"><div class="wrap">
 <div class="hph" style="background-image:url({img})"></div>
 <div class="htx"><span class="eyebrow" style="color:#ffffffc0">{eyebrow}</span>
  <h2>Un vrai échange, <em>avec une vraie personne.</em></h2>
  <p>15 minutes pour parler de votre activité et de ce dont vous avez besoin. Pas de robot, pas de pression.</p>
  <div class="cta">{btn("Être appelé", "rendez-vous.html")}{btn("Contacter", WA_PROJET, "btn-line")}</div>
 </div></div></section>
"""

TRUST = ["Une présence en ligne pensée pour", "Être compris rapidement", "Inspirer confiance", "Générer des contacts", "Être consultée sur mobile"]


def sector(file, title, desc, photo, eyebrow, h1, lead, att_h2, att_p, att_cards, checks, faqs):
    body = hero(eyebrow, h1, lead,
                [btn('Être appelé', "rendez-vous.html"), btn("Voir les offres", "#offre", "btn-line")],
                "En ligne en 5 jours ou 48 h · Paiement unique · Satisfait ou remboursé 14 jours", photo)
    body += '<div class="trustbar"><div class="wrap">' + "".join(f"<span>{t}</span>" for t in TRUST) + "</div></div>\n"
    body += f'<section class="section"><div class="wrap">{head("Les attentes de vos clients", att_h2, att_p)}{cards(att_cards)}</div></section>\n'
    body += ('<section class="section white"><div class="wrap">'
             + head("Un site utile, pas simplement joli", "Les bons éléments, au bon endroit.",
                    "Le contenu et les fonctionnalités sont définis selon votre activité, vos objectifs et le périmètre validé ensemble. Voici des éléments que nous pouvons prévoir.")
             + '<div class="checks rv">' + "".join(f"<div>{c}</div>" for c in checks) + "</div></div></section>\n")
    body += ('<section class="section dark"><div class="wrap">'
             + head("Méthode", "Simple pour vous. <em>Exigeant</em> pour nous.",
                    "Vous continuez votre activité. Nous nous occupons de tout, des textes à la mise en ligne.")
             + cards(STEPS) + "</div></section>\n")
    body += OFFERS
    body += f'<section class="section" style="padding-top:0"><div class="wrap faq-grid"><div class="rv"><span class="eyebrow">Questions fréquentes</span><h2 class="h2" style="font-size:clamp(36px,4.2vw,62px)">Avant de vous <em>lancer.</em></h2></div>{faq(faqs)}</div></section>\n'
    body += human({"restaurants.html":P_B,"coiffeurs.html":P_A}.get(file,P_C))
    open(file, "w").write(page(title, desc, body))


sector("restaurants.html", "Création de sites web pour restaurants et cafés | VITRIA PRO",
       "Sites vitrines pour restaurants et cafés : carte lisible sur mobile, univers en images, horaires et contact.",
       "photo-1517248135467-4c7edcad34c4", "Restaurants & cafés · Sites web professionnels",
       "Donnez envie de découvrir votre table. <em>Avant même d'y entrer.</em>",
       "Votre site doit donner un aperçu de votre cuisine, rendre votre carte facile à consulter et permettre à vos clients de trouver rapidement les informations pratiques pour venir chez vous.",
       "Un site qui donne les bonnes raisons de choisir votre établissement.",
       "Vos futurs clients veulent voir ce que vous proposez, comprendre l'ambiance et savoir comment vous trouver. Votre site rassemble ces réponses dans une présentation claire.",
       [("01", "Une carte facile à consulter", "Présentez vos menus, spécialités et formules dans un format lisible sur téléphone."),
        ("02", "Votre univers en images", "Mettez en valeur votre salle, votre équipe, vos plats et l'identité de votre établissement."),
        ("03", "Les informations essentielles", "Horaires, adresse, accès et moyens de contact sont faciles à repérer.")],
       ["Carte et menus consultables sur mobile", "Galerie photo de l'établissement et des plats", "Horaires, adresse et itinéraire",
        "Bouton d'appel et contact direct", "Lien vers votre outil de réservation si vous en utilisez un", "Base SEO locale et pages structurées"],
       [("Puis-je modifier ma carte ?", "Le mode de mise à jour est défini selon le projet. Les modifications peuvent être prévues dans une prestation séparée ou un contrat de maintenance."),
        ("La réservation en ligne est-elle incluse ?", "Un lien vers votre outil existant peut être intégré. Un système de réservation spécifique fait l'objet d'un périmètre et d'un devis distincts."),
        ("Le site sera-t-il adapté aux téléphones ?", "Oui. L'adaptation mobile fait partie de l'offre standard.")])

sector("coiffeurs.html", "Création de sites web pour coiffeurs et instituts | VITRIA PRO",
       "Sites vitrines pour coiffeurs et instituts : prestations et tarifs, univers du salon, accès direct au rendez-vous.",
       "photo-1521590832167-7bcbfaa6381f", "Coiffeurs & instituts · Sites web professionnels",
       "Votre savoir-faire mérite une première impression <em>à sa hauteur.</em>",
       "Avant de réserver, vos futurs clients veulent découvrir votre univers, comprendre vos prestations et savoir où vous trouver. Votre site doit rendre ce parcours simple et rassurant.",
       "Transformez la visite en ligne en envie de prendre rendez-vous.",
       "Une présentation soignée permet de montrer votre style, vos services et les informations pratiques sans obliger vos clients à chercher partout.",
       [("01", "Prestations et tarifs", "Présentez clairement vos coupes, soins, couleurs, forfaits et tarifs."),
        ("02", "Un univers reconnaissable", "Montrez votre salon, vos réalisations et l'expérience que vous proposez."),
        ("03", "Un accès direct au rendez-vous", "Facilitez le contact et renvoyez vers votre outil de réservation si vous en avez un.")],
       ["Prestations et tarifs organisés clairement", "Galerie de réalisations et photos du salon", "Présentation de l'équipe et de l'approche",
        "Horaires, adresse et coordonnées visibles", "Bouton de contact ou lien de réservation", "Base SEO locale et expérience mobile"],
       [("Pouvez-vous intégrer mon outil de réservation ?", "Un lien vers votre solution actuelle peut être ajouté. Une intégration technique spécifique est chiffrée séparément."),
        ("Puis-je présenter plusieurs prestations ?", "Oui. Les pages et rubriques sont organisées selon votre carte de services et le périmètre convenu."),
        ("Le site sera-t-il adapté aux mobiles ?", "Oui. La consultation sur smartphone est intégrée à la conception du site.")])

sector("artisans.html", "Création de sites web pour artisans et bâtiment | VITRIA PRO",
       "Sites vitrines pour artisans et entreprises du bâtiment : prestations, réalisations, zones d'intervention et demande de devis.",
       "photo-1600607687939-ce8a6c25118c", "Artisans & bâtiment · Sites web professionnels",
       "Montrez la qualité de votre travail. <em>Obtenez de meilleures demandes.</em>",
       "Quand un particulier cherche un artisan, il veut comprendre vos services, voir des réalisations et vérifier votre zone d'intervention. Votre site doit lui donner confiance et faciliter la demande de devis.",
       "Un site conçu pour rassurer avant le premier appel.",
       "Votre savoir-faire mérite mieux qu'une simple fiche de coordonnées. Présentez vos spécialités, vos chantiers et votre façon de travailler avec clarté.",
       [("01", "Vos prestations et spécialités", "Expliquez vos services, vos domaines d'intervention et les types de projets acceptés."),
        ("02", "Des réalisations concrètes", "Mettez en avant des photos de chantiers, avant/après et exemples de travaux."),
        ("03", "Une demande de devis simple", "Aidez vos prospects à décrire leur besoin et à vous transmettre leurs coordonnées.")],
       ["Présentation de vos services et spécialités", "Galerie de chantiers et réalisations", "Zones géographiques d'intervention",
        "Formulaire de demande de devis", "Coordonnées et horaires accessibles", "Qualifications et garanties si applicables"],
       [("Puis-je ajouter mes zones d'intervention ?", "Oui. Les villes ou secteurs couverts peuvent être présentés sur le site selon votre activité."),
        ("Le formulaire peut-il recueillir les détails du chantier ?", "Oui. Les champs sont définis avec vous pour recueillir les informations utiles à une première qualification."),
        ("Pouvez-vous intégrer mes avis clients ?", "Des avis authentiques provenant de plateformes ou de témoignages autorisés peuvent être mis en valeur.")])

sector("plomberie.html", "Création de sites web pour plombiers | VITRIA PRO",
       "Sites vitrines pour plombiers et chauffagistes : urgences, prestations, zone d'intervention et demande de devis.",
       "photo-1607472586893-edb57bdc0e39", "Plomberie & chauffage · Sites web professionnels",
       "Quand la fuite arrive, <em>c'est vous qu'on appelle.</em>",
       "En urgence comme pour un devis, vos clients cherchent un plombier proche, joignable vite et de confiance. Votre site doit leur permettre de vous appeler en un geste.",
       "Un site pensé pour l'urgence et pour le devis.",
       "Un particulier qui cherche un plombier compare vite. Il retient celui qu'il comprend, qu'il peut joindre tout de suite et qui lui inspire confiance.",
       [("01", "Un appel en un geste", "Votre numéro est visible et cliquable sur téléphone, là où vos clients en ont besoin."),
        ("02", "Des prestations claires", "Dépannage, chauffe-eau, salle de bain, rénovation : chaque service est présenté simplement."),
        ("03", "Votre zone d'intervention", "Vos clients voient tout de suite si vous intervenez chez eux, puis demandent leur devis.")],
       ["Numéro d'appel visible et cliquable sur mobile", "Présentation des prestations et des urgences", "Zones géographiques d'intervention",
        "Formulaire de demande de devis", "Photos de chantiers si vous en avez", "Base SEO locale et expérience mobile"],
       [("Puis-je afficher un numéro pour les urgences ?", "Oui. Le numéro et les modalités d'appel sont définis avec vous, selon votre organisation."),
        ("Puis-je indiquer mes villes d'intervention ?", "Oui. Les villes ou secteurs couverts sont présentés selon votre activité."),
        ("Le site sera-t-il adapté aux téléphones ?", "Oui. L'adaptation mobile fait partie de l'offre standard.")])

# ---------- Garantie ----------
G = [("1. Bénéficiaires et offres concernées", "La garantie est proposée aux clients professionnels qui commandent directement auprès de VITRIA PRO l'une des offres de création de site internet Essentiel, Business ou Premium. Elle doit être mentionnée sur le devis accepté. Elle ne s'applique pas aux prestations ou achats réalisés directement auprès de fournisseurs tiers."),
     ("2. Durée et point de départ", "Le délai est de <strong>14 jours calendaires</strong>. Il commence le lendemain de la mise en ligne effective du site sur le nom de domaine convenu. La date de mise en ligne est communiquée au client par écrit. La demande doit parvenir à VITRIA PRO avant l'expiration de ce délai."),
     ("3. Comment demander le remboursement", 'Le client adresse sa demande par écrit à <a href="mailto:contact@vitriapro.com">contact@vitriapro.com</a> en indiquant le nom de son entreprise, la référence du devis et le site concerné. Aucun motif particulier n\'est exigé au titre de cette garantie commerciale.'),
     ("4. Montant remboursé", "Lorsque les conditions de la garantie sont remplies, VITRIA PRO rembourse intégralement les sommes effectivement encaissées par VITRIA PRO au titre de la prestation de création du site concerné. Les frais de fournisseurs tiers (notamment nom de domaine, hébergement, licences, abonnements ou services externes) ne sont pas inclus lorsqu'ils ont été commandés ou facturés séparément et identifiés comme tels dans le devis."),
     ("5. Retrait du site et arrêt de son utilisation", "En contrepartie du remboursement, le site réalisé par VITRIA PRO est dépublié ou désactivé. Le client cesse de l'utiliser et ne peut pas exploiter, reproduire, transmettre ou faire exploiter les éléments de conception et de développement réalisés par VITRIA PRO au titre de cette prestation remboursée. Les éléments et services appartenant à des tiers restent soumis à leurs propres licences et conditions."),
     ("6. Modalités de remboursement", "Après réception de la demande dans le délai et organisation du retrait du site, VITRIA PRO confirme par écrit la prise en compte de la garantie et procède au remboursement par le moyen de paiement initial, dans un délai maximal de 14 jours calendaires à compter de cette confirmation, sous réserve des délais de traitement de l'établissement de paiement."),
     ("7. Droits légaux", "Cette garantie commerciale ne se substitue pas aux garanties, recours ou droits impératifs dont le client pourrait bénéficier en vertu de la loi. Elle ne constitue pas une renonciation à un éventuel droit légal de rétractation lorsqu'il est applicable."),
     ("8. Contact", 'Pour toute question relative à cette garantie : <a href="mailto:contact@vitriapro.com">contact@vitriapro.com</a>.')]
body = hero("Engagement commercial VITRIA PRO", "14 jours pour décider <em>sereinement.</em>",
            "La garantie commerciale VITRIA PRO permet aux clients professionnels concernés de demander le remboursement de la prestation de création de leur site dans les 14 jours calendaires suivant sa mise en ligne, selon les conditions ci-dessous.",
            [btn('Être appelé', "rendez-vous.html")])
body += '<section class="section"><div class="wrap"><div class="article rv"><div class="callout"><strong>À lire avant de commander.</strong> Cette garantie est un engagement commercial volontaire de VITRIA PRO. Elle s\'ajoute aux droits légaux éventuellement applicables et ne les limite pas. Les conditions particulières figurant au devis accepté restent applicables pour le périmètre et les frais propres à la commande.</div>'
body += "".join(f"<h2>{t}</h2><p>{p}</p>" for t, p in G) + "</div></div></section>\n"
open("garantie.html", "w").write(page("Garantie commerciale 14 jours — VITRIA PRO", "Conditions de la garantie commerciale VITRIA PRO : 14 jours après la mise en ligne pour décider.", body))

# ---------- Mentions légales ----------
ML = [("Éditeur du site", "Le site vitriapro.com est édité par <strong>Alan Laurençont</strong>, entrepreneur individuel exerçant sous le nom commercial <strong>VITRIA PRO</strong>.<br>RUC (Paraguay) : 9418022-9<br>Adresse : La Cofi Coworking, Luis Alberto de Herrera 463, Asunción, Paraguay<br>Téléphone : +595 992 666 002<br>E-mail : <a href=\"mailto:contact@vitriapro.com\" style=\"text-decoration:underline\">contact@vitriapro.com</a><br>Directeur de la publication : Alan Laurençont."),
      ("Hébergement", "Le site est hébergé par Cloudflare, Inc., 101 Townsend Street, San Francisco, CA 94107, États-Unis (cloudflare.com)."),
      ("Prix et taxes", "Les prix sont indiqués en euros, toutes taxes comprises (TTC). Le paiement est unique. Le périmètre exact de chaque prestation est précisé dans le devis accepté par le client."),
      ("Garantie commerciale", "Les conditions de la garantie de 14 jours sont décrites sur la page <a href=\"garantie.html\" style=\"text-decoration:underline\">Garantie 14 jours</a>."),
      ("Démonstrations et photographies", "Les sites présentés par secteur sont des démonstrations. Les entreprises qui y figurent sont fictives. Les photographies sont des illustrations, issues de la banque d'images Unsplash et utilisées selon sa licence."),
      ("Propriété intellectuelle", "Les textes, éléments graphiques et le logo de VITRIA PRO sont la propriété de l'éditeur. Toute reproduction sans autorisation écrite est interdite."),
      ("Données personnelles", "Les informations que vous transmettez par e-mail, par WhatsApp ou via l'agenda de rendez-vous servent uniquement à répondre à votre demande et à préparer votre projet. Elles ne sont ni vendues ni cédées. La prise de rendez-vous passe par le service Cal.com. Si vous arrivez sur ce site depuis un de nos e-mails, nous enregistrons que le lien a été ouvert et quelles pages vous consultez, afin de savoir quels messages sont utiles ; aucun cookie n'est déposé. Pour consulter, corriger ou faire supprimer vos données, écrivez à contact@vitriapro.com."),
      ("Contact", "Pour toute question sur le site ou une prestation, écrivez à contact@vitriapro.com ou écrivez-nous sur WhatsApp.")]
body = hero("Informations légales", "Mentions <em>légales.</em>", "Qui est derrière VITRIA PRO, où le site est hébergé, et comment sont traités vos prix et vos données.", [])
body += '<section class="section"><div class="wrap"><div class="article rv">' + "".join(f"<h2>{t}</h2><p>{p}</p>" for t, p in ML) + "</div></div></section>\n"
open("mentions-legales.html", "w").write(page("Mentions légales — VITRIA PRO", "Mentions légales de VITRIA PRO : éditeur, hébergement, prix, données personnelles.", body))

# ---------- Rendez-vous ----------
body = """<section class="rvhero"><div class="wrap">
 <div>
  <span class="eyebrow">Prise de rendez-vous</span>
  <h1>Parlons de votre projet, <em>simplement.</em></h1>
  <p class="lead">Un vrai échange de 15 minutes avec une vraie personne. On écoute votre activité et vos clients, et on vous dit ce qu'il vous faut.</p>
  <ul class="rvpts"><li>15 minutes, sans engagement</li><li>Votre site en ligne en 5 jours ou 48 h</li><li>Réponse humaine, pas de robot</li></ul>
 </div>
 <div class="rvph" style="background-image:url(""" + UNS.replace("w=2000","w=1000").format("photo-1758876020337-2501eeb1ede5") + """)"><div class="cap"><b>Un appel de 15 minutes</b>Choisissez votre créneau juste en dessous.</div></div>
</div></section>
"""
body += """<section class="section" style="padding-top:60px"><div class="wrap">
 <div id="calendar">
  <div class="sec-head rv" style="margin-bottom:0"><div><span class="eyebrow">Agenda</span><h2 class="mid">Choisissez une date et une heure</h2></div><p>Les disponibilités s’affichent dans votre fuseau horaire local. Sélectionnez le créneau qui vous convient.</p></div>
  <div class="calendar"><div id="my-cal-inline-vitriapro15" style="width:100%;height:100%;overflow:scroll"></div></div>
  <p class="fine-note">Un problème pour choisir votre créneau ? Écrivez-nous à <a href="mailto:contact@vitriapro.com" style="text-decoration:underline">contact@vitriapro.com</a>.</p>
 </div>
</div></section>
"""
CAL = """<script>
(function (C, A, L) { let p = function (a, ar) { a.q.push(ar); }; let d = C.document; C.Cal = C.Cal || function () { let cal = C.Cal; let ar = arguments; if (!cal.loaded) { cal.ns = {}; cal.q = cal.q || []; d.head.appendChild(d.createElement("script")).src = A; cal.loaded = true; } if (ar[0] === L) { const api = function () { p(api, arguments); }; const namespace = ar[1]; api.q = api.q || []; if (typeof namespace === "string") { cal.ns[namespace] = cal.ns[namespace] || api; p(cal.ns[namespace], ar); p(cal, ["initNamespace", namespace]); } else p(cal, ar); return; } p(cal, ar); }; })(window, "https://app.cal.com/embed/embed.js", "init");
Cal("init", "vitriapro15", { origin: "https://app.cal.com" });
Cal.ns.vitriapro15("inline", { elementOrSelector: "#my-cal-inline-vitriapro15", calLink: "vitriapro/15min", config: { layout: "month_view", theme: "light" } });
Cal.ns.vitriapro15("ui", { styles: { branding: { brandColor: "#0a1533" } } });
</script>"""
open("rendez-vous.html", "w").write(page("Prendre rendez-vous — VITRIA PRO", "Réservez un échange avec VITRIA PRO : appel de 15 minutes.", body, CAL))

# ---------- Réalisations ----------
def proj(tag, h3, p, lis, mock, link="", alt=""):
    l = f'<a class="btn btn-dark" href="{link[0]}">{link[1]}</a>' if link else ""
    ms = mock
    return f"""<div class="proj rv"><div><span class="tag">{tag}</span><h3>{h3}</h3><p>{p}</p><ul>{''.join(f'<li>{x}</li>' for x in lis)}</ul>{l}</div>
<div class="mock {alt}"><div class="dots"><i></i><i></i><i></i></div><div><small>{ms[0]}</small><strong>{ms[1]}</strong><p>{ms[2]}</p></div><b>{ms[3]}</b></div></div>"""

body = hero("Réalisations", "Voyez le niveau. <em>Imaginez le vôtre.</em>",
            "Notre propre site, conçu et développé en interne, et des concepts par secteur pour vous projeter dans le vôtre.",
            [btn('Prendre rendez-vous', "rendez-vous.html")])
body += '<section class="section"><div class="wrap">' + head("01 / Projet interne", "Une réalisation réelle : VITRIA PRO.", "Le site de l'agence est un projet interne conçu et développé pour présenter les offres, expliquer la méthode et permettre aux entreprises de prendre contact.")
body += '<div style="margin-top:40px">' + proj("Projet interne · Site de marque", "VITRIA PRO — identité et présence web",
             "Conception de l'identité numérique de l'agence et de son site vitrine : direction visuelle, structure des pages, présentation des offres, parcours de contact et adaptation mobile.",
             ["Identité visuelle et système typographique", "Page d'accueil et pages sectorielles", "Présentation des offres et prise de rendez-vous", "Assistant d'orientation et contact WhatsApp"],
             ("AGENCE DE SITES INTERNET", "Des sites qui font venir des clients.", "En ligne en 5 jours ou 48 h.", "RÉSERVER UN APPEL"), ("index.html", "Voir le site"))
body += '</div></div></section>\n'
body += '<section class="section white"><div class="wrap">' + head("02 / Concepts de démonstration", "Trois univers pour se projeter.", "Des directions de design par métier, pour imaginer votre futur site avant même notre premier appel.")
body += '<div style="margin-top:40px">'
body += proj("Concept de démonstration · Artisan", "Artisan / Plomberie & dépannage", "Une page pensée pour rendre les services immédiatement compréhensibles et faciliter l'appel ou la demande de devis.",
             ["Accroche centrée sur le besoin urgent", "Services et zones d'intervention", "Appel téléphonique mis en évidence"],
             ("ARTISAN · DÉPANNAGE", "Un artisan de confiance, près de chez vous.", "Plomberie, chauffage et dépannage. Contactez-nous pour parler de votre besoin.", "DEMANDER UN DEVIS"), ("plomberie.html", "Voir le site plomberie"))
body += proj("Concept de démonstration · Restaurant", "Restaurant / Cuisine contemporaine", "Un univers éditorial pour mettre en avant l'expérience, la carte, les informations pratiques et la réservation.",
             ["Photographies et identité de lieu", "Carte et informations pratiques", "Réservation ou contact selon le besoin"],
             ("MAISON & TABLE · CUISINE DE SAISON", "Le goût des bonnes choses, simplement.", "Une cuisine de saison, des produits choisis et un accueil attentionné.", "DÉCOUVRIR LA CARTE"), alt="alt")
body += proj("Concept de démonstration · Beauté", "Salon / Coiffure & beauté", "Une présentation visuelle soignée pour valoriser les prestations, les tarifs, l'équipe et les possibilités de rendez-vous.",
             ["Univers graphique adapté à la marque", "Prestations et tarifs lisibles", "Prise de rendez-vous ou demande de contact"],
             ("STUDIO ÉPURE · COIFFURE & BEAUTÉ", "Un moment pour révéler votre style.", "Conseil, coupe et soin dans un espace pensé pour vous.", "VOIR LES PRESTATIONS"), alt="alt2")
body += '</div><p class="fine-note">Les noms et textes de ces concepts sont fictifs.</p></div></section>\n'
body += f"""<section class="band"><div class="wrap"><span class="eyebrow">Votre projet</span><h2>Votre activité mérite un site conçu pour <em>vos clients.</em></h2><p>Parlons de votre entreprise, de vos services et de ce que votre site doit permettre à vos visiteurs de faire.</p><div class="cta">{btn('Prendre rendez-vous', "rendez-vous.html")}</div></div></section>
"""
open("realisations.html", "w").write(page("Réalisations & démonstrations | VITRIA PRO", "Projet interne VITRIA PRO et concepts de démonstration par secteur.", body))

# ---------- Recrutement ----------
body = hero("VITRIA PRO Careers · Développement commercial · France", "Vous développez les ventes. <em>Nous concevons les solutions.</em>",
            "VITRIA PRO recherche des commerciaux indépendants capables de développer une clientèle professionnelle et de commercialiser des solutions numériques auprès des PME, artisans et entrepreneurs français.",
            [btn('Présenter ma candidature', "#candidature"), btn("Découvrir la collaboration", "#mission", "btn-line")],
            photo="photo-1521737711867-e3b97375f902",
            stats='<div class="hero-stats"><div><strong>Marché français</strong>PME, artisans et indépendants</div><div><strong>À distance</strong>Prospection organisée librement</div><div><strong>À la commission</strong>Sur les ventes éligibles encaissées</div></div>')
body += '<section class="section" id="mission"><div class="wrap">' + head("L'offre VITRIA PRO", "Une offre simple et forte à <em>commercialiser.</em>", "Mise en ligne en 5 jours ou 48 h, paiement unique et garantie 14 jours : des arguments qui facilitent la vente. Vous vendez, nous concevons.")
body += cards([("01 / Essentiel · 990 €", "Site one-page", "Pour les artisans et indépendants qui veulent être trouvés et appelés."),
               ("02 / Business · 1 490 €", "Jusqu'à 5 pages", "Une page par service, formulaire de devis et référencement local optimisé."),
               ("03 / Premium · 2 490 €", "Jusqu'à 10 pages", "Une structure complète pour les entreprises qui veulent s'imposer dans leur secteur.")]) + "</div></section>\n"
body += '<section class="section dark"><div class="wrap">' + head("Votre mission", "De la première prise de contact à la vente.", "Le rôle est commercial. Vous n'avez pas à concevoir les sites ni à assurer le développement technique. Vous identifiez les opportunités, comprenez le besoin et faites avancer la relation jusqu'à la conclusion, avec l'appui de VITRIA PRO sur le cadrage de l'offre.")
body += cards([("01", "Identifier les entreprises", "Repérer les PME, artisans et indépendants qui ont un besoin numérique réel : création, refonte, vente en ligne ou outil métier."),
               ("02", "Prospecter et obtenir un échange", "Contacter les décideurs par téléphone, e-mail, LinkedIn ou tout autre canal professionnel adapté, dans le respect des règles applicables."),
               ("03", "Qualifier le besoin", "Comprendre l'activité, l'objectif, le calendrier et le besoin du prospect. Ne pas promettre de fonctionnalité, de délai ou de prix non validé."),
               ("04", "Présenter et conclure", "Présenter l'offre et les propositions validées avec VITRIA PRO, répondre aux questions et accompagner la décision commerciale."),
               ("05", "Transmettre un dossier complet", "Après accord du client, transmettre les informations nécessaires. VITRIA PRO organise le cadrage et la réalisation selon le périmètre contractuel.")], "five") + "</div></section>\n"
body += """<section class="section white"><div class="wrap comm rv">
 <div class="big">30 %<small>Commission commerciale envisagée</small></div>
 <div><span class="eyebrow">Rémunération</span><h2 class="h2" style="font-size:clamp(34px,4.2vw,62px)">Une commission liée aux <em>ventes réalisées.</em></h2>
 <p>La rémunération proposée est de <strong>30 % du montant hors taxes effectivement encaissé par VITRIA PRO</strong> au titre d'une vente attribuée au commercial, selon les conditions prévues au contrat. Les remboursements, annulations et avoirs sont traités selon ce contrat. Les modalités d'attribution, d'exigibilité et de versement seront écrites avant le début de la collaboration.</p>
 <p>Le montant de chaque commission dépendra du prix HT réellement facturé et encaissé pour la vente attribuée. Il ne constitue ni un salaire ni un revenu garanti. Collaboration indépendante, sans fixe. Le cadre contractuel, le statut et les modalités de facturation seront validés avant tout démarrage.</p></div>
</div></section>
"""
body += '<section class="section"><div class="wrap">' + head("Le profil recherché", "Un commercial autonome, à l'aise avec les décideurs.", "Nous privilégions la capacité à prospecter, écouter, qualifier et conclure. La qualité de la démarche compte davantage qu'un intitulé de poste sur un CV.")
body += cards([("01", "Prospection B2B", "Vous êtes à l'aise pour contacter des dirigeants et ouvrir une conversation commerciale."),
               ("02", "Autonomie réelle", "Vous savez organiser votre activité, vos relances et votre suivi sans dépendre de leads fournis."),
               ("03", "Écoute et qualification", "Vous posez les bonnes questions avant de proposer une solution."),
               ("04", "Rigueur commerciale", "Vous savez documenter vos échanges et transmettre des informations fiables.")], "four")
body += '<div class="side-note rv"><strong>Vous n\'avez pas encore vendu de solutions numériques ?</strong> Une expérience de vente B2B dans un autre secteur peut convenir si vous savez prospecter et apprendre une offre. La candidature sera évaluée sur votre méthode et votre mise en situation, pas uniquement sur votre CV.</div></div></section>\n'
body += '<section class="section dark" id="processus"><div class="wrap">' + head("Parcours de sélection", "Un processus clair, en cinq étapes.", "Chaque candidature est examinée. Nous cherchons à vérifier la méthode commerciale et l'adéquation avec une collaboration indépendante.")
body += cards([("01", "Candidature", "Vous présentez votre expérience, votre méthode et vos motivations."),
               ("02", "Étude du profil", "Nous examinons votre parcours et la cohérence de votre démarche."),
               ("03", "Rendez-vous", "Échange sur l'offre, votre organisation et les conditions de collaboration."),
               ("04", "Mise en situation", "Simulation courte de prospection et de qualification d'un prospect PME."),
               ("05", "Cadre & démarrage", "Si accord mutuel : validation du statut, contrat, commission et outils avant lancement.")], "five") + "</div></section>\n"
rec = open("tools/recru_form.html").read()
body += f"""<section class="section" id="candidature"><div class="wrap apply">
 <div class="rv"><span class="eyebrow">Candidature</span><h2>Parlons de votre approche <em>commerciale.</em></h2><p>Décrivez votre expérience et expliquez comment vous trouveriez vos premiers clients pour VITRIA PRO. Un exemple de prospection ou de vente réussie est particulièrement utile.</p>
 <div class="side-note"><strong>À savoir</strong><br>Cette page concerne une collaboration indépendante à la commission, et non un emploi salarié. Aucun salaire fixe ni volume de ventes n'est garanti. Le contrat et les conditions définitives seront communiqués et acceptés avant toute mission.</div></div>
 <div class="rv">{rec}</div>
</div></section>
"""
body += '<section class="section" style="padding-top:0"><div class="wrap faq-grid"><div class="rv"><span class="eyebrow">Questions fréquentes</span><h2 class="h2" style="font-size:clamp(36px,4.2vw,62px)">Les conditions de <em>collaboration.</em></h2></div>' + faq([
    ("Est-ce un poste salarié ?", "Non. Il s'agit d'une proposition de collaboration commerciale indépendante, rémunérée à la commission. Il n'y a pas de salaire fixe, de revenu minimum garanti ni de promesse d'embauche salariée."),
    ("Faut-il déjà avoir une entreprise ?", "Vous pouvez candidater même si votre création d'activité est en cours. En revanche, le statut juridique, la capacité à facturer et le cadre contractuel devront être clarifiés et validés avant toute mission rémunérée."),
    ("Comment la commission est-elle calculée ?", "La base envisagée est de 30 % du montant HT effectivement encaissé par VITRIA PRO sur les ventes attribuées au commercial. Le contrat précisera notamment l'attribution des ventes, les remboursements ou annulations, l'exigibilité et le calendrier de versement."),
    ("Dois-je réaliser moi-même les sites ou les applications ?", "Non. Votre rôle est commercial : prospection, qualification, présentation de l'offre et suivi de la vente. VITRIA PRO prend en charge le cadrage et la coordination de la prestation retenue, dans les limites du périmètre accepté."),
    ("Les prospects sont-ils fournis ?", "Le profil recherché doit savoir développer sa propre prospection. Les modalités de partage et de suivi des opportunités éventuelles seront précisées pendant l'échange de sélection."),
    ("La candidature garantit-elle une collaboration ?", "Non. Chaque profil est évalué. Une collaboration ne commence qu'après accord mutuel et validation écrite du statut, du contrat et des modalités commerciales.")]) + "</div></section>\n"
RJS = open("tools/recru_js.html").read()
open("recrutement-commercial.html", "w").write(page("Recrutement commerciaux indépendants — VITRIA PRO", "VITRIA PRO recherche des commerciaux indépendants rémunérés à la commission.", body, RJS))
print("pages générées")


# ---------- Balises canonical et partage (toutes les pages) ----------
import re as _re
for _f in ["index","restaurants","coiffeurs","artisans","plomberie","garantie","realisations","rendez-vous","recrutement-commercial"]:
    _p = _f + ".html"
    _s = open(_p, encoding="utf-8").read()
    if 'rel="canonical"' in _s:
        continue
    _t = _re.search(r"<title>(.*?)</title>", _s).group(1)
    _d = _re.search(r'<meta name="description" content="(.*?)">', _s).group(1)
    _u = "https://vitriapro.com/" if _f == "index" else f"https://vitriapro.com/{_p}"
    _tags = (f'<link rel="canonical" href="{_u}">\n<meta property="og:type" content="website">\n'
             f'<meta property="og:site_name" content="VITRIA PRO">\n<meta property="og:title" content="{_t}">\n'
             f'<meta property="og:description" content="{_d}">\n<meta property="og:url" content="{_u}">\n')
    _s = _s.replace('<link rel="icon"', _tags + '<link rel="icon"', 1)
    open(_p, "w", encoding="utf-8").write(_s)
