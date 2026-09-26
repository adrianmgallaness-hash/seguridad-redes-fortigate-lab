# FortiGate Running Config

Esta carpeta contiene la configuración exportada del FortiGate utilizada en el laboratorio.

## Archivo

- `fortigate-running-config-sanitized.conf`: copia del running-config preparada para el repositorio público.

La copia publicada conserva la configuración necesaria para documentar el laboratorio, incluyendo interfaces/VLANs, DHCP, políticas de firewall, NAT, IPS, la firma personalizada de SQL Injection, File Filter y DoS Policy.

## Seguridad

El backup original exportado desde FortiGate contiene material sensible generado por el sistema, como contraseñas cifradas y claves privadas. Por este motivo, el archivo publicado fue sanitizado antes de subirlo a GitHub. El backup original debe conservarse localmente y no publicarse en un repositorio público.

Configuraciones relevantes presentes en el archivo:

- VLAN 10 USERS, VLAN 20 WEB y VLAN 30 DB.
- DHCP en VLAN10-USERS.
- Políticas `USERS-to-WEB-HTTPS`, `USERS-to-DB-BLOCK-3306`, `WEB-to-DB-MYSQL` y `USERS-to-INTERNET`.
- IPS `SQLI-PROTECT`.
- Firma personalizada `LAB.SQLI.TEST`.
- File Filter `BLOCK-EXE`.
- IPv4 DoS Policy.
