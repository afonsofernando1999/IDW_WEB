# -*- coding: utf-8 -*-

import os
import webbrowser
import http.server
import socketserver


PASTA = os.path.dirname(
    os.path.abspath(
        __file__
    )
)


os.chdir(
    PASTA
)


PORTA = 8000


URL = (
    f"http://127.0.0.1:{PORTA}/"
)


class Handler(
    http.server.SimpleHTTPRequestHandler
):

    def end_headers(
        self
    ):

        self.send_header(
            "Cache-Control",
            "no-store, no-cache, must-revalidate, max-age=0"
        )

        self.send_header(
            "Pragma",
            "no-cache"
        )

        self.send_header(
            "Expires",
            "0"
        )

        super().end_headers()


class Servidor(
    socketserver.TCPServer
):

    allow_reuse_address = True


print()
print(
    "=" * 60
)

print(
    "IDW WEB PROFISSIONAL"
)

print(
    "=" * 60
)

print()
print(
    URL
)

print()
print(
    "CTRL+C para terminar."
)

print()


webbrowser.open(
    URL
)


with Servidor(

    (
        "127.0.0.1",
        PORTA
    ),

    Handler

) as servidor:

    servidor.serve_forever()
