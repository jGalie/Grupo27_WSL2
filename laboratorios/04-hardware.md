# Laboratorio 04. Diagnóstico de módulos, `loop`, KVM y USB

**Propósito:** distinguir **soporte en el kernel**, **dispositivo expuesto** y **funcionamiento efectivo**, tomando como antecedentes reportes concretos de usuarios de WSL y usbipd-win.

La herramienta [`diagnostico_wsl2_v6_1.py`](../scripts/diagnostico_wsl2_v6_1.py) ejecutó 25 comprobaciones no destructivas. Sus resultados se complementaron con pruebas manuales para `loop` y USB. No se afirmó que las 25 comprobaciones fueran pruebas funcionales.

## `loop`: diagnóstico y operación real

`modinfo loop` devolvió `Module loop not found`, pero `/proc/config.gz` mostró `CONFIG_BLK_DEV_LOOP=y`: el soporte está compilado dentro del kernel. Después se creó un archivo temporal de 16 MB, asociado a `/dev/loop0` con `losetup`; `dd` leyó 1 MB y produjo el mensaje `LECTURA_LOOP_OK`. Se liberó el dispositivo y se eliminó el archivo de prueba.

```bash
IMG=$(mktemp "$HOME/prueba_loop_XXXXXX.img")
truncate -s 16M "$IMG"
DEVICE=$(sudo losetup --find --show "$IMG")
echo "Dispositivo asignado: $DEVICE"
sudo losetup -j "$IMG"
sudo dd if="$DEVICE" of=/dev/null bs=1M count=1 status=none && echo "LECTURA_LOOP_OK"
sudo losetup -d "$DEVICE"
rm -- "$IMG"
```

**Conclusión:** la asociación y lectura mediante `loop` funcionaron en este entorno; no se probó montaje de particiones ni significa que no existan problemas específicos en otros escenarios.

## KVM: soporte configurado y disponibilidad

Se identificó `CONFIG_KVM=m` y `CONFIG_KVM_AMD=m`. `modinfo kvm_amd` encontró el módulo; `modprobe -n -v kvm_amd` simuló dependencias sin ejecutar la carga. En el entorno AMD estudiado no estaban expuestos `svm` ni `/dev/kvm`. No se ejecutó una VM sobre KVM ni se determinó la causa de la ausencia del dispositivo.

## USB físico: integración con `usbipd-win`

Windows identificó un dispositivo `0930:6545` en estado `Shared`, pero Ubuntu no lo enumeraba inicialmente. El dispositivo se vinculó mediante `usbipd bind --busid 2-2` y `usbipd attach --wsl --busid 2-2`. `lsusb` confirmó su enumeración; después se utilizó `usbipd detach --busid 2-2` y se comprobó que dejó de aparecer.

La herramienta Python solamente inspeccionó el estado y no conectó ni desconectó el USB. La enumeración comprobada no equivale a una prueba de lectura/escritura de archivos del pendrive.

**Evidencias:** [Fig. 14](../evidencias/hardware/fig-14.png), [15](../evidencias/hardware/fig-15.png), [16](../evidencias/hardware/fig-16.png), [17](../evidencias/hardware/fig-17.png), [18](../evidencias/hardware/fig-18.png), [19](../evidencias/hardware/fig-19.png), [20](../evidencias/hardware/fig-20.png), [21](../evidencias/hardware/fig-21.png), [22](../evidencias/hardware/fig-22.png).
