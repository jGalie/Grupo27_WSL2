# Laboratorio 02. Conectividad NAT y mirrored

**Propósito:** evaluar el funcionamiento de Nginx por HTTP dentro de Ubuntu y desde una segunda computadora de la misma red local.

**NAT:** con `ip -4 addr` e `ip route` se observó una dirección privada de WSL y su ruta virtual; `curl -i http://localhost` respondió `HTTP/1.1 200 OK`. El acceso desde otro equipo requirió configurar una redirección TCP con `portproxy` y una regla del firewall de Windows, conforme al procedimiento documentado en el artículo.

**Mirrored:** se habilitó `networkingMode=mirrored` en `.wslconfig` y se reinició WSL2. Ubuntu mostró la dirección IPv4 de la interfaz del anfitrión; para el acceso entrante al puerto 80 desde la LAN fue necesaria una regla del firewall de Hyper-V. El cliente de la segunda computadora cargó la página de Nginx sin `portproxy`.

**Resultado:** ambos mecanismos permitieron acceso HTTP bajo condiciones de configuración diferentes. Que Nginx responda en `localhost` no demuestra que sea accesible desde la red local.

**Evidencias:** [Fig. 4](../evidencias/conectividad/fig-04.png), [5](../evidencias/conectividad/fig-05.png), [6](../evidencias/conectividad/fig-06.png), [7](../evidencias/conectividad/fig-07.png), [8](../evidencias/conectividad/fig-08.png), [9](../evidencias/conectividad/fig-09.png).

**Referencia:** [Documentación de redes de Microsoft WSL](https://learn.microsoft.com/es-es/windows/wsl/networking).
