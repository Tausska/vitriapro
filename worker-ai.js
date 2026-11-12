const SYSTEM_PROMPT = `Tu es l'assistant commercial de VITRIA PRO, une agence de création de sites internet pour les entreprises françaises.
Réponds en français, clairement, avec des messages courts et professionnels.
Ta mission : comprendre le métier du visiteur, son besoin (création ou refonte), son site actuel, ses pages/fonctionnalités et son calendrier, puis l'orienter vers une demande de devis ou WhatsApp.
Offres indicatives : Essentiel 990 € (site vitrine one-page), Business 1 490 € (jusqu'à 5 pages), Premium 2 490 € (jusqu'à 10 pages). Le devis confirme toujours le périmètre, la devise, les taxes éventuelles, le calendrier et les coûts tiers.
Ne promets jamais de résultats SEO, de délais, de fonctionnalités ou de prestations non confirmés. E-commerce, réservation avancée, espace client, rédaction complète et prestations récurrentes sont sur devis.
Ne prétends pas être humain. Ne demande pas de données bancaires, mots de passe ou données sensibles. Si tu ne sais pas, dis-le et propose WhatsApp.
Ne pousse pas agressivement à l'achat. Pose une seule question utile à la fois.`;

const cors = {
  "Access-Control-Allow-Origin": "https://vitriapro.com",
  "Access-Control-Allow-Methods": "POST, OPTIONS",
  "Access-Control-Allow-Headers": "Content-Type",
  "Vary": "Origin"
};

export default {
  async fetch(request, env) {
    const url = new URL(request.url);
    if (request.method === "OPTIONS") return new Response(null, { headers: cors });
    if (url.pathname !== "/api/chat") return new Response("Not found", { status: 404 });
    if (request.method !== "POST") return Response.json({ error: "Method not allowed" }, { status: 405, headers: cors });

    try {
      const body = await request.json();
      if (!Array.isArray(body.messages) || body.messages.length === 0 || body.messages.length > 12) {
        return Response.json({ error: "Invalid messages" }, { status: 400, headers: cors });
      }
      const messages = body.messages.map(m => {
        if (!m || !["user", "assistant"].includes(m.role) || typeof m.content !== "string") throw new Error("Invalid message");
        return { role: m.role, content: m.content.slice(0, 1000) };
      });
      if (messages[messages.length - 1].role !== "user") {
        return Response.json({ error: "Last message must be from user" }, { status: 400, headers: cors });
      }
      const result = await env.AI.run("@cf/meta/llama-3.1-8b-instruct", {
        messages: [{ role: "system", content: SYSTEM_PROMPT }, ...messages],
        max_tokens: 350,
        temperature: 0.35
      });
      const reply = result?.response || result?.choices?.[0]?.message?.content;
      if (!reply) throw new Error("Empty model response");
      return Response.json({ reply: String(reply).slice(0, 3000) }, { headers: { ...cors, "Cache-Control": "no-store" } });
    } catch (error) {
      return Response.json({ error: "Assistant temporarily unavailable" }, { status: 503, headers: cors });
    }
  }
};
