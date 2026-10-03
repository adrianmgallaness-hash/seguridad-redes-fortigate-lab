# Pruebas y validaciones

## Infraestructura 1

Las pruebas detalladas se conservan en [laboratorio/docs/pruebas.md](../laboratorio/docs/pruebas.md) y en [laboratorio/images/](../laboratorio/images/).

## Infraestructura 2

### VPN activa

```bash
ping 10.21.39.130
wget --no-check-certificate -T 5 -S -O- https://10.21.39.130/
sudo busybox traceroute -n 10.21.39.130
```

Resultado esperado/validado: conectividad al servidor y respuesta HTTPS 200.

### VPN inactiva

Al bajar el túnel `VPN-FGT1-CISCO`, la comunicación usuario → servidor deja de funcionar.

## Infraestructura 3

### DHCP / VLAN 10

Cliente validado como:

```text
10.21.39.10/25
default via 10.21.39.1
```

R2 mostró un binding DHCP activo sobre `FastEthernet1/0.10`.

### HTTPS sin VPN

```bash
wget --no-check-certificate -T 5 -S -O- https://198.51.100.22/
```

Resultado validado:

```text
HTTP/1.0 200 OK
Servidor HTTPS - Seguridad de Redes
Ubuntu Server 10.21.39.130
```

### SSH sin VPN

```bash
ssh adrian@10.21.39.130
```

Resultado observado:

```text
No route to host
```

### VPN Remote Access

```bash
sudo ipsec up VPN-REMOTE-SSH
sudo ipsec statusall
```

Resultado observado:

- XAuth de `vpnuser` exitoso.
- IKE SA establecida.
- IP virtual `10.99.99.10`.
- CHILD SA establecida para `10.99.99.10/32 === 10.21.39.128/28`.

### SSH con VPN

```bash
ssh adrian@10.21.39.130
```

Resultado: acceso SSH exitoso.

### Traceroute requerido

Para la demostración final:

```bash
sudo busybox traceroute -n 10.21.39.130
```

Guardar captura como evidencia del requisito de traceroute.
