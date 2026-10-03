# Infraestructura 1 — Segmentación y controles de seguridad

## Propósito

Implementar una arquitectura segmentada con FortiGate como firewall principal, separando usuarios, servidor web y base de datos, y aplicando controles de acceso, NAT, DHCP y perfiles de seguridad.

## Direccionamiento

| Segmento | Red | Gateway | Equipo principal |
|---|---|---|---|
| VLAN 10 USERS | `10.21.39.0/25` | `10.21.39.1` | Cliente de usuario |
| VLAN 20 WEB | `10.21.39.128/28` | `10.21.39.129` | WEB `10.21.39.130` |
| VLAN 30 DB | `10.21.39.144/28` | `10.21.39.145` | DB `10.21.39.146` |

## Controles documentados

- Segmentación por VLAN.
- DHCP para usuarios.
- NAT y ruta por defecto.
- USERS → WEB por HTTPS/443.
- USERS → DB bloqueado.
- WEB → DB limitado a TCP/3306.
- IPS para patrones SQL Injection.
- Cuarentena/bloqueo de atacante.
- File Filter para ejecutables.
- Política DoS/SYN flood.

## Evidencias e imágenes

![Topología de Infraestructura 1](../laboratorio/diagrams/Diagrama_Topologia.png)

Documentación existente:

- [Propósito](../laboratorio/docs/proposito.md)
- [Pruebas](../laboratorio/docs/pruebas.md)
- [Configuración DB](../laboratorio/docs/db-server.md)
- [Running-config FortiGate sanitizado](../laboratorio/configs/fortigate/fortigate-running-config-sanitized.conf)
- [Estado WEB Server](../laboratorio/configs/servers/web-server-running-config.txt)
- [Estado DB Server](../laboratorio/configs/servers/db-server-running-state.txt)
- [Scripts de pruebas](../laboratorio/scripts/tests/security-tests.sh)
