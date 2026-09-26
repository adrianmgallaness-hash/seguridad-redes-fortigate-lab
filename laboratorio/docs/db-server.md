# DB Server - Configuración validada

Este documento registra únicamente los parámetros del DB Server que fueron observados y comprobados durante el laboratorio.

## Red

- VLAN: **VLAN 30 - DB**
- Red: `10.21.39.144/28`
- IP: `10.21.39.146/28`
- Gateway: `10.21.39.145`

## Servicio

- Sistema: Ubuntu Server
- Motor: MySQL
- Puerto: TCP/3306
- Estado validado: servicio escuchando en `10.21.39.146:3306`

## Validación

```bash
hostname -I
ip route
sudo ss -lntp | grep 3306
```

Pruebas realizadas:

- WEB Server `10.21.39.130` → DB `10.21.39.146:3306`: permitido.
- WEB Server → DB TCP/22: bloqueado / timeout.
- USERS `10.21.39.11` → DB TCP/3306: bloqueado / timeout.

## Políticas relacionadas

- WEB → DB MySQL TCP/3306: ALLOW.
- USERS → DB MySQL TCP/3306: DENY.
- Otros servicios WEB → DB: deny implícito.

> Nota: no se incluyen valores de archivos como `/etc/netplan/*` o `mysqld.cnf` porque su contenido exacto no fue capturado. Este archivo documenta el estado validado del servidor sin inventar configuraciones.
