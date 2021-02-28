# Face_Mask_Detection_Raspberry_Pi
## Materiales:
- Raspberry Pi (Puede ser 3b+ o 4)
- Memoria SD de mínimo 15 Gb
- Cable HDMI.
- Cámara Raspberry Pi
- Monitor, teclado y ratón.
## Instrucciones de ejecución del sistema de detección de máscaras en tiempo real en Raspberry Pi:
1. Una vez instalado Raspberry Pi OS en la placa y establecida la configuración de idioma, pantalla y red, es nesesario habilitar el módulo de la Pi Camera y reiniciar el sistema. Menu>Preferencias>Configuración de Raspberry Pi.
![imagen](https://github.com/AndresFlorez-Git/Face_Mask_Detection_Raspberry_Pi/blob/main/pic/1.png)
2. Clonar este repositorio.
```sh
$ git clone https://github.com/AndresFlorez-Git/Face_Mask_Detection_Raspberry_Pi
```

3. Ejecutar el archivo de instalación. Este archivo permite de forma automatizada, instalar todas las librerias y dependencias necesarias.
```sh
$ cd Face_Mask_Detection_Raspberry_Pi
```
```sh
$ chmod +x Instalacion.sh
```
```sh
$ ./Instalacion.sh
```

4. Ya se puede ejecutar el programa de detección de máscaras en tiempo real ubicado en la carpeta Mask Detection.
```sh
$ cd Mask\ Detection
```
```sh
$ python3 Real_time_mask_detection.py
```

5. Para finalizar la ejecición del programa, presionar la letra q
