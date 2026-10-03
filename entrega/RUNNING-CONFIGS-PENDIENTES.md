# Running-configs — estado de entrega

El repositorio ya contiene un running-config sanitizado de FortiGate correspondiente al laboratorio base:

- [FortiGate running-config sanitizado](../laboratorio/configs/fortigate/fortigate-running-config-sanitized.conf)

También contiene estados/configuraciones de servidores:

- [WEB Server](../laboratorio/configs/servers/web-server-running-config.txt)
- [DB Server](../laboratorio/configs/servers/db-server-running-state.txt)

## Archivos adicionales incluidos

En [configs/](configs/) se agregaron extractos verificados de las configuraciones de Infraestructura 2 y 3.

## Para cumplir literalmente con “Running-Configs deben ser subidos”

Antes de entregar, capturar los completos y sustituir/complementar los extractos:

### Cisco R2

```text
terminal length 0
show running-config
```

### ISP Cisco

```text
terminal length 0
show running-config
```

### FortiGate

Exportar/respaldar la configuración por GUI y sanitizar cualquier contraseña, PSK, token o clave privada antes de publicarla.

> Nunca publicar credenciales reales en un repositorio público.
