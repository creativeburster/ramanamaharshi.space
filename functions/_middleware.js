/**
 * Cloudflare Pages Edge Middleware
 * 使用内置 HTMLRewriter 在流式返回 HTML 时为全站所有 <script> 标签自动注入 data-cfasync="false"，
 * 从边缘层彻底屏蔽 Cloudflare Rocket Loader 对全站 JS 及 GA4 统计脚本的改写与拦截。
 */
class ScriptCfAsyncRewriter {
  element(element) {
    if (element.getAttribute('data-cfasync') !== 'false') {
      element.setAttribute('data-cfasync', 'false');
    }
  }
}

export async function onRequest(context) {
  const response = await context.next();
  const contentType = response.headers.get('content-type') || '';

  if (contentType.includes('text/html')) {
    return new HTMLRewriter()
      .on('script', new ScriptCfAsyncRewriter())
      .transform(response);
  }

  return response;
}
