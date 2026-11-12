# VITRIA PRO

Site commercial de VITRIA PRO, agence de création de sites vitrines pour TPE, PME et indépendants en France.

## Pages publiques
- `index.html` : accueil, offres et présentation.
- `restaurants.html` : page dédiée aux restaurants et cafés.
- `coiffeurs.html` : page dédiée aux coiffeurs et instituts.
- `artisans.html` : page dédiée aux artisans et entreprises du bâtiment.
- `rendez-vous.html` : réservation Calendly de 30 minutes.
- `recrutement-commercial.html` : recrutement de commerciaux indépendants.
- `robots.txt`, `sitemap.xml` et `favicon.svg`.

## Offres
- Essentiel : 990 € — site vitrine one-page.
- Business : 1 490 € — jusqu'à 5 pages.
- Premium : 2 490 € — jusqu'à 10 pages.

Prix indicatifs. Le devis confirme le périmètre, la devise, le traitement fiscal, les délais, les frais tiers et les modalités de paiement. Ne pas afficher HT ou TTC tant que le régime applicable n'a pas été confirmé.

## Contact et réservation
- E-mail : `contact@vitriapro.com`.
- Calendly : `https://calendly.com/contact-vitriapro/30min`.
- Le formulaire de contact prépare un e-mail via `mailto:`; il ne transmet pas les données à un serveur.

## Déploiement
- Dépôt : `Tausska/vitriapro`.
- Branche de production : `main`.
- Worker Cloudflare : `vitriapro`.
- Configuration Wrangler : `wrangler.jsonc`.
- Déploiement attendu : Cloudflare Workers Builds, commande `npx wrangler deploy`.
- Les fichiers `README.md`, `docs/**`, `.github/**`, `.git/**`, `.wrangler/**`, `.gitignore`, `.assetsignore` et `wrangler.jsonc` sont exclus des assets publics via `.assetsignore`.

Après chaque push sur `main`, vérifier dans Cloudflare Workers Builds qu'un build est déclenché et que son commit correspond au dernier commit GitHub. Un commit GitHub ne prouve pas à lui seul que le site public a été déployé.

## Documentation opérationnelle
- `docs/kit-commercial.md` : offre, qualification, scripts et objections.
- `docs/recrutement-commercial.md` : annonce de recrutement.
- `docs/devis-modele.md` : modèle de devis.
- `docs/contrat-client-modele.md` : projet de contrat client.
- `docs/accord-commercial-modele.md` : projet d'accord commercial.
- `docs/kit-prospection-100-prospects.md` : plan de prospection.
- `docs/procedure-production-livraison.md` : production et livraison.
- `docs/mentions-legales-a-completer.md` et `docs/politique-confidentialite-a-completer.md` : documents à compléter et faire vérifier.
- `docs/checklist-lancement.md` : checklist de lancement.

## Garde-fous
Les images de démonstration ne sont pas des réalisations clients. Ne publier aucun témoignage, résultat chiffré ou référence sans preuve. Les contrats et notices sont des brouillons, pas des avis juridiques ou fiscaux. Compléter l'identité de l'entité exploitante et faire vérifier les obligations fiscales transfrontalières, la qualification juridique des commerciaux et les règles applicables aux clients français avant signature ou publication.
