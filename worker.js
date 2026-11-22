// Mesure anonyme d'où viennent les visites (pub, e-mail, recherche...). Pas de cookie, pas d'IP, pas d'identité.
const EV = ["view", "cta"];
const BOT = /bot|crawl|spider|slurp|preview|scan|headless|curl|python|go-http|monitor/i;
export default {
  async fetch(req, env) {
    const url = new URL(req.url);
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
