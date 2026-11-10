// Cloudflare Pages Function: GA4 Anti-Bot Edge Protection
// Intercepts known datacenter ASNs without referer to prevent headless bot pollution in GA4

const DATACENTER_BOT_ASNS = new Set([
  45102,  // Alibaba Cloud (Singapore / US)
  37963,  // Alibaba Cloud
  132203, // Tencent Cloud (Singapore)
  45090,  // Tencent Cloud
  14061,  // DigitalOcean
  20473,  // Vultr / Choopa
  16276,  // OVH
  24940,  // Hetzner
  9009,   // M247
]);

export async function onRequest(context) {
  const cfAsn = Number(context.request.cf && context.request.cf.asn ? context.request.cf.asn : 0);
  const referer = context.request.headers.get("referer") || "";
  const isSuspiciousDatacenterDirect = DATACENTER_BOT_ASNS.has(cfAsn) && !referer;

  const response = await context.next();
  const contentType = response.headers.get("content-type") || "";

  if (contentType.includes("text/html") && typeof HTMLRewriter !== "undefined") {
    let rewriter = new HTMLRewriter();

    if (isSuspiciousDatacenterDirect) {
      rewriter = rewriter.on("head", {
        element(el) {
          el.prepend(
            `<script data-cfasync="false">window['ga-disable-G-MYFWHFPSYB'] = true;</script>`,
            { html: true }
          );
        },
      });
    }

    return rewriter.transform(response);
  }

  return response;
}
