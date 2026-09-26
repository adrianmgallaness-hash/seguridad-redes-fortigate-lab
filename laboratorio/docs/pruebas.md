# Pruebas y validaciones

## HTTPS

Desde `user-client`:

```bash
curl -k -i -m 5 https://10.21.39.130/
```

Resultado esperado: `HTTP/1.1 200 OK`.

## USERS → DB bloqueado

```bash
nc -vz -w 5 10.21.39.146 3306
```

Resultado esperado: timeout/bloqueo.

## WEB → DB permitido por MySQL

Desde `web-server`:

```bash
nc -vz -w 5 10.21.39.146 3306
```

Resultado esperado: conexión exitosa.

## WEB → DB por otro puerto

```bash
nc -vz -w 5 10.21.39.146 22
```

Resultado esperado: timeout por deny implícito.

## SQL Injection controlado

```bash
curl -i "http://10.21.39.130/sqli-test?q=UNION%20SELECT%201"
```

Resultado esperado: detección por la firma IPS `LAB.SQLI.TEST`. Con acción Quarantine, la IP origen es puesta en cuarentena.

## Verificación de cuarentena

```text
diagnose user quarantine list
```

IP observada: `10.21.39.11`.

## File Filter EXE

```bash
curl -v -o prueba.exe http://10.21.39.130/prueba.exe
```

Resultado esperado: archivo `prueba.exe` bloqueado por el perfil File Filter.

## Prueba DoS controlada

```bash
sudo hping3 -S -p 443 -i u1000 -c 1000 10.21.39.130
```

Resultado esperado: generación de eventos de anomalía y aplicación de la acción configurada en la DoS Policy.
