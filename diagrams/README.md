# Diagramas

Esta carpeta contendrá el diagrama final de la topología.

Diagrama lógico esperado:

```text
Internet
   |
FortiGate
   |
 Trunk
   |
 Switch
   |--- VLAN 10 USERS ---- user-client
   |--- VLAN 20 WEB ------ web-server
   |--- VLAN 30 DB ------- db-server
```
