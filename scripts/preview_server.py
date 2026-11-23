# ** local preview server **
# Serves public/ with clean URLs like Cloudflare does (/team -> team.html),
# so internal links work locally. Python standard library only.
# Run from the project folder: python3 scripts/preview_server.py
import http.server
import os
import sys
from urllib.parse import urlsplit

PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 8123
PUBLIC = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'public')


class CleanURLHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=PUBLIC, **kwargs)

    # ** pick the file for each request **
    def send_head(self):
        url = urlsplit(self.path)
        path = url.path
        query = '?' + url.query if url.query else ''
        local = self.translate_path(path)

        # old .html addresses redirect to the clean URL, like the live site
        if path.endswith(('/index.html', '/index')):
            return self.redirect(path[:path.rindex('/') + 1] + query)
        if path.endswith('.html'):
            return self.redirect(path[:-len('.html')] + query)

        # folders such as /services/ use their index.html
        if os.path.isdir(local):
            if not os.path.isfile(os.path.join(local, 'index.html')):
                return self.not_found()
            if not path.endswith('/'):
                return self.redirect(path + '/' + query)
            return super().send_head()

        # assets, robots.txt and sitemap.xml
        if os.path.isfile(local):
            return super().send_head()

        # pages such as /team use team.html; /team/ redirects to /team
        page = local.rstrip('/') + '.html'
        if os.path.isfile(page):
            if path.endswith('/'):
                return self.redirect(path.rstrip('/') + query)
            self.path = path + '.html'
            return super().send_head()

        return self.not_found()

    # ** responses **
    def redirect(self, location):
        self.send_response(307)
        self.send_header('Location', location)
        self.send_header('Content-Length', '0')
        self.end_headers()
        return None

    def not_found(self):
        page = open(os.path.join(PUBLIC, '404.html'), 'rb')
        self.send_response(404)
        self.send_header('Content-Type', 'text/html; charset=utf-8')
        self.send_header('Content-Length', str(os.fstat(page.fileno()).st_size))
        self.end_headers()
        return page


if __name__ == '__main__':
    server = http.server.ThreadingHTTPServer(('127.0.0.1', PORT), CleanURLHandler)
    print(f'Previewing public/ at http://localhost:{PORT} (Ctrl+C to stop)')
    server.serve_forever()
