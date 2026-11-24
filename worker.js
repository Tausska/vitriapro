// Mesure anonyme d'où viennent les visites (pub, e-mail, recherche...). Pas de cookie, pas d'IP, pas d'identité.
const EV = ["view", "cta"];
const BOT = /bot|crawl|spider|slurp|preview|scan|headless|curl|python|go-http|monitor/i;
// Langue du site : Paraguay = espagnol (/es/), ailleurs = français. Le visiteur peut changer avec le lien « Español / Français » ; son choix est gardé dans un cookie.
const PAGES = new Set(["index", "rendez-vous", "artisans", "coiffeurs", "plomberie", "restaurants", "realisations", "garantie", "conditions", "mentions-legales", "recrutement-commercial"]);
const ES_COUNTRIES = new Set(["PY", "AR"]);
const ROBOT = /bot|crawl|spider|slurp|preview|facebookexternalhit|whatsapp|telegram/i;
function pageOf(path) {
  let m = path.match(/^\/es(?:\/(?:([\w-]+?)(?:\.html)?)?)?\/?$/);
  if (m) { const p = m[1] || "index"; return PAGES.has(p) ? { lang: "es", page: p } : null; }
  m = path.match(/^\/(?:([\w-]+?)(?:\.html)?)?\/?$/);
  if (m) { const p = m[1] || "index"; return PAGES.has(p) ? { lang: "fr", page: p } : null; }
  return null;
}
const toPath = (lang, page) => (lang === "es" ? "/es/" + (page === "index" ? "" : page) : page === "index" ? "/" : "/" + page);
function langRedirect(req, url) {
  if (req.method !== "GET" && req.method !== "HEAD") return null;
  const pg = pageOf(url.pathname); if (!pg) return null;
  const q = url.searchParams.get("lang");
  const hdr = { "Cache-Control": "private, no-store", Vary: "Cookie" };
  if (q === "fr" || q === "es") return new Response(null, { status: 302, headers: { ...hdr, Location: toPath(q, pg.page), "Set-Cookie": "vp_lang=" + q + "; Path=/; Max-Age=31536000; SameSite=Lax; Secure" } });
  if (pg.lang === "es" || ROBOT.test(req.headers.get("user-agent") || "")) return null;
  const c = (req.headers.get("cookie") || "").match(/(?:^|;\s*)vp_lang=(fr|es)/);
  const want = c ? c[1] : ES_COUNTRIES.has(req.cf && req.cf.country) ? "es" : "fr";
  return want === "es" ? new Response(null, { status: 302, headers: { ...hdr, Location: toPath("es", pg.page) } }) : null;
}
export default {
  async fetch(req, env) {
    const url = new URL(req.url);
    const lr = langRedirect(req, url); if (lr) return lr;
    if (url.pathname !== "/t") return env.ASSETS.fetch(req);
    if (req.method !== "POST") return new Response(null, { status: 204 });
    try {
      const d = JSON.parse((await req.text()).slice(0, 2000));
      const s = (v, n) => String(v || "").slice(0, n);
      const ev = EV.includes(d.ev) ? d.ev : "view";
      const bot = BOT.test(req.headers.get("user-agent") || "") ? 1 : 0;
      await env.DB.prepare("INSERT INTO visits(ev,path,src,med,cam,ref,country,bot,sid) VALUES(?,?,?,?,?,?,?,?,?)")
        .bind(ev, s(d.p, 120), s(d.s, 40), s(d.m, 40), s(d.c, 60), s(d.r, 80), s(req.cf && req.cf.country, 4), bot, s(d.i, 16)).run();
    } catch (_) {}
    return new Response(null, { status: 204 });
  },
};
