"""本地开发服务器 - 自动添加 .html 后缀"""
import http.server, socketserver, os
from urllib.parse import urlparse

PORT = 8080

class CustomHandler(http.server.SimpleHTTPRequestHandler):
    def translate_path(self, path):
        result = super().translate_path(path)
        if path.endswith('/') and not os.path.exists(result):
            html_result = result + '.html'
            if os.path.exists(html_result):
                return html_result
        return result

    def do_GET(self):
        parsed = urlparse(self.path)
        path = parsed.path
        if path.endswith('/'):
            new_path = path.rstrip('/') + '.html'
            check_path = self.translate_path(new_path)
            if os.path.exists(check_path):
                self.path = new_path
        return super().do_GET()

    def end_headers(self):
        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        super().end_headers()

os.chdir(os.path.dirname(os.path.abspath(__file__)))
with socketserver.TCPServer(("", PORT), CustomHandler) as httpd:
    print(f"本地服务器已启动: http://localhost:{PORT}/")
    print("支持自动 .html 后缀重定向")
    httpd.serve_forever()
