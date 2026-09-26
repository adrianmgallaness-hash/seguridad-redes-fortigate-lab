#!/usr/bin/env bash
# Comandos utilizados durante la validación del laboratorio.
# Ejecutar únicamente dentro del entorno de laboratorio autorizado.

WEB="10.21.39.130"
DB="10.21.39.146"

echo "[1] HTTPS hacia WEB"
curl -k -i -m 5 "https://$WEB/"

echo "[2] MySQL hacia DB"
nc -vz -w 5 "$DB" 3306 || true

echo "[3] SQLi de laboratorio"
curl -i "http://$WEB/sqli-test?q=UNION%20SELECT%201"

echo "[4] Descarga EXE de prueba"
curl -v -o prueba.exe "http://$WEB/prueba.exe"
