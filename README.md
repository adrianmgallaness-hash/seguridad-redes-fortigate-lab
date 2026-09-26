# Laboratorio de Seguridad de Redes con FortiGate

## 🎥 Video demostrativo

> **Enlace del video:** https://youtu.be/tVhtWXWO9dE

---

## Propósito del laboratorio

Implementar y validar una arquitectura de red segmentada mediante VLANs y protegida por un firewall FortiGate, aplicando controles de acceso, NAT, DHCP, IPS, detección y bloqueo de SQL Injection, filtrado de archivos ejecutables y protección contra tráfico DoS.

## Topología lógica

- **FortiGate:** FortiOS 7.0.9
- **VLAN 10 — USERS:** `10.21.39.0/25`
  - Gateway: `10.21.39.1`
  - Cliente de prueba: `10.21.39.11`
  - DHCP habilitado
- **VLAN 20 — WEB:** `10.21.39.128/28`
  - Gateway: `10.21.39.129`
  - WEB Server: `10.21.39.130`
- **VLAN 30 — DB:** `10.21.39.144/28`
  - Gateway: `10.21.39.145`
  - DB Server: `10.21.39.146`

## Controles implementados

| Control | Estado |
|---|---|
| Segmentación VLAN | ✅ |
| DHCP para usuarios | ✅ |
| Default route | ✅ |
| NAT hacia Internet | ✅ |
| Users → WEB HTTPS/443 | ✅ |
| Users → DB TCP/3306 bloqueado | ✅ |
| WEB → DB solo TCP/3306 | ✅ |
| MySQL en DB Server | ✅ |
| IPS SQL Injection | ✅ |
| Bloqueo y cuarentena del atacante | ✅ |
| File Filter para archivos EXE | ✅ |
| Protección DoS / SYN flood | ✅ |

## Evidencias principales

La documentación y las capturas de las pruebas se almacenan en:

- [`laboratorio/docs/`](laboratorio/docs/) — explicación técnica del laboratorio.
- [`laboratorio/images/`](laboratorio/images/) — capturas utilizadas en la documentación.
- [`laboratorio/diagrams/`](laboratorio/diagrams/) — diagramas de topología.
- [`laboratorio/configs/`](laboratorio/configs/) — running-configs y configuraciones relevantes.
- [`laboratorio/scripts/`](laboratorio/scripts/) — scripts y comandos utilizados.
- [`laboratorio/evidence/`](laboratorio/evidence/) — evidencias de validación de los controles.

## Pruebas realizadas

Entre las pruebas realizadas se encuentran:

- Acceso HTTPS exitoso desde USERS al WEB Server.
- Bloqueo de conexión desde USERS hacia MySQL en el DB Server.
- Conexión exitosa desde WEB Server hacia DB Server por TCP/3306.
- Bloqueo de otros puertos entre WEB y DB mediante deny implícito.
- Detección de un patrón SQLi mediante IPS.
- Bloqueo y cuarentena de la IP atacante `10.21.39.11`.
- Bloqueo de descarga de un archivo PE/EXE de prueba.
- Generación controlada de SYNs para validar la política DoS.

## Estructura del repositorio

```text
.
├── README.md
├── VIDEO.md
└── laboratorio/
    ├── configs/
    │   ├── fortigate/
    │   └── servers/
    ├── diagrams/
    ├── docs/
    ├── evidence/
    ├── images/
    └── scripts/
        ├── tests/
        └── web/
```

## Nota sobre la demostración SQLi

La detección SQLi se validó en un endpoint HTTP controlado dentro del laboratorio para permitir al motor IPS inspeccionar el payload. El servicio principal del WEB Server permanece disponible mediante HTTPS/443.

## Estado

Laboratorio técnico completado. La documentación, las evidencias, los diagramas, los scripts y los running-configs se encuentran organizados dentro de `laboratorio/`.
