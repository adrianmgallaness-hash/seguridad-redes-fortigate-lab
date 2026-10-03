# Infraestructura 2 — VPN Site-to-Site FortiGate ↔ Cisco

## Propósito

Comunicar el segmento de usuarios con el servidor mediante una VPN IPsec Site-to-Site. La comunicación entre ambos extremos debe depender de que el túnel VPN se encuentre activo.

## Requisitos cubiertos

- FortiGate configurado y demostrado por GUI.
- Configuración de red y NAT en FortiGate.
- VPN Site-to-Site entre FortiGate y Cisco.
- Equipo Cisco con red, NAT y VPN IPsec.
- ISP con direccionamiento público simulado.
- Servidor WEB en /28 con HTTPS.
- Usuarios en /25, VLAN 10, DHCP y traceroute.

## Direccionamiento

| Enlace/segmento | Dirección |
|---|---|
| USERS | `10.21.39.0/25` |
| Gateway USERS (FortiGate) | `10.21.39.1` |
| Cliente | DHCP, validado como `10.21.39.10/25` |
| FortiGate WAN | `198.51.100.22/30` |
| ISP hacia FortiGate | `198.51.100.21/30` |
| ISP hacia Cisco | `203.0.113.37/30` |
| Cisco R2 WAN | `203.0.113.38/30` |
| Server LAN | `10.21.39.128/28` |
| R2 LAN/Gateway | `10.21.39.129/28` |
| Ubuntu Server | `10.21.39.130/28` |

## VPN

- Nombre FortiGate: `VPN-FGT1-CISCO`.
- Peer FortiGate: `203.0.113.38`.
- Peer Cisco: `198.51.100.22`.
- IKEv1.
- Propuestas de baja encriptación requeridas por la VM de evaluación: DES/MD5 o DES/SHA1.
- Tráfico interesante: `10.21.39.0/25 ↔ 10.21.39.128/28`.

## Validación

Con el túnel activo se validó:

- IKE SA en estado `QM_IDLE` / activo.
- Contadores ESP de cifrado y descifrado incrementando.
- Ping del usuario al servidor.
- HTTPS al servidor con respuesta `HTTP/1.0 200 OK`.
- Traceroute hacia `10.21.39.130`.

Con el túnel deshabilitado se obtuvo ausencia de conectividad hacia el servidor, demostrando que la comunicación depende de la VPN.

![Diagrama Infraestructura 2](diagramas/infraestructura-2.svg)

Los extractos de configuración verificados están en [configs/](configs/).
