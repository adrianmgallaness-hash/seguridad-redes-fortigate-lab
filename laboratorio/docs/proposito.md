# Propósito del laboratorio

El laboratorio tiene como objetivo implementar una red segmentada y aplicar controles de seguridad en un FortiGate utilizando su interfaz gráfica.

Los objetivos técnicos principales son:

- Separar usuarios, servidor WEB y servidor de base de datos mediante VLANs.
- Proporcionar direccionamiento dinámico mediante DHCP a la VLAN de usuarios.
- Controlar el tráfico entre segmentos mediante políticas de firewall.
- Permitir acceso HTTPS desde usuarios hacia el servidor WEB.
- Impedir acceso directo desde usuarios hacia MySQL.
- Permitir al servidor WEB comunicarse con el DB Server únicamente mediante TCP/3306.
- Proporcionar salida a Internet mediante default route y NAT.
- Detectar y bloquear intentos de SQL Injection mediante IPS.
- Poner en cuarentena al origen de una detección SQLi.
- Bloquear descargas de archivos ejecutables mediante File Filter.
- Mitigar tráfico DoS mediante una política de anomalías.
