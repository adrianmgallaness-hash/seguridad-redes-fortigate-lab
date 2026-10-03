#!/usr/bin/env python3
"""Servidor HTTPS mínimo utilizado para validar el laboratorio."""

from http.server import HTTPServer, SimpleHTTPRequestHandler
import ssl

HOST = "0.0.0.0"
PORT = 443
CERT = "cert.pem"
KEY = "key.pem"

httpd = HTTPServer((HOST, PORT), SimpleHTTPRequestHandler)
context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain(certfile=CERT, keyfile=KEY)
httpd.socket = context.wrap_socket(httpd.socket, server_side=True)

print(f"HTTPS escuchando en {HOST}:{PORT}")
httpd.serve_forever()
