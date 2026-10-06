#!/usr/bin/env python3
"""
Catalog Server — serves the app's curated JSON catalogs over the LAN so the
TV apps refresh daily without an APK reinstall (the daily 5h cron rebuilds
kids-series.json + kids-films-streaming.json in assets/).

GET-only, *.json only, read-only, no directory listing. Port 8099.

Portability (future Mac mini): pure stdlib — move the repo, run this same
script under launchd, and point the app's "Catalog URL" setting at the new
host. Nothing else changes.
"""

import http.server
import logging
import os

logging.basicConfig(level=logging.INFO, format='%(asctime)s [%(levelname)s] %(message)s')
log = logging.getLogger('catalog-server')

HERE = os.path.dirname(os.path.abspath(__file__))
ASSETS_DIR = os.path.join(HERE, 'app', 'src', 'main', 'assets')
PORT = 8099


class CatalogHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=ASSETS_DIR, **kwargs)

    def do_GET(self):
        # Only flat *.json files — no listing, no traversal, nothing else.
        name = self.path.lstrip('/').split('?')[0]
        if '/' in name or not name.endswith('.json') or \
                not os.path.isfile(os.path.join(ASSETS_DIR, name)):
            self.send_error(404)
            return
        super().do_GET()

    def do_HEAD(self):
        self.do_GET()

    def log_message(self, fmt, *args):
        log.info("%s %s", self.address_string(), fmt % args)


def main():
    log.info(f'Serving *.json from {ASSETS_DIR} on 0.0.0.0:{PORT}')
    http.server.ThreadingHTTPServer(('0.0.0.0', PORT), CatalogHandler).serve_forever()


if __name__ == '__main__':
    main()
