# Arquitectura y direccionamiento

## Segmentos

| VLAN | Función | Red | Gateway | Host principal |
|---|---|---|---|---|
| 10 | USERS | 10.21.39.0/25 | 10.21.39.1 | user-client: 10.21.39.11 |
| 20 | WEB | 10.21.39.128/28 | 10.21.39.129 | web-server: 10.21.39.130 |
| 30 | DB | 10.21.39.144/28 | 10.21.39.145 | db-server: 10.21.39.146 |

## Flujo de tráfico esperado

- USERS → WEB: permitido por HTTPS/443.
- USERS → DB: MySQL/3306 denegado.
- WEB → DB: MySQL/3306 permitido.
- WEB → DB: cualquier otro servicio bloqueado por deny implícito.
- USERS → Internet: permitido mediante NAT.

## Servicios

- WEB Server: Nginx.
- DB Server: MySQL.
- FortiGate: firewall, NAT, DHCP, IPS, File Filter y DoS Policy.
