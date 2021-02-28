
# Librerías y Dependencias
Para el desarrollo del proyecto se está utilizando las siguientes librerías y versiones:
## Para el ordenador principal:
Maquina donde se desarrollen los modelos de Deep Learning y se haga el entrenamiento de dichos modelos.
En mi caso cuento con una maquina Lenovo Y50, que cuenta con 12 GB de memoria Ram y adicionalmente una GPU NVIDIA GEFORCE GTX 960M.
Se recomienda el uso de la plataforma de código abierto [ANACODNA](https://www.anaconda.com/products/individual) para el desarrollo del proyecto (Conda version 4.8.3).
#### La versión de python 
La versión más actual al momento de desarrollo es python 3.7.6.
#### Librerías:
La plataforma ANACONDA ofrece cientos de paquetes y librerías actualizadas y disponibles para su uso. En esta sección se repasará las librerías usadas y si es necesario, su línea de instalación a través del ANACONDA PROMT.


| Libreria | versión |
| ------ | ------ |
| Numpy | 1.18.5 |
| matplotlib base | 3.2.2 |
| imutils | 0.5.3 |
| opencv-python | 4.2.0|
| scipy| 1.4.1 |
| Tensorflow | 1.13.1 GPU version |

Para la correcta instalación de tensorflow-gpu en anaconda, usar en el ANACONDA Promt:
```sh
$ conda install -c anaconda tensorflow-gpu
```


## Para Raspberry Pi:

Dispositivo portátil (ordenador de placa reducida) de bajo coste, en el cual se cargaran los modelos desarrollados y entrenados para poder realizar un procesamiento en tiempo real de la información suministrada.
En mi caso cuento con una Raspberry Pi 4
#### La versión de python 
La versión más actual al momento de desarrollo es python 3.7.6.}
#### Librerías:


| Librería | versión |
| ------ | ------ |
| Numpy | 1.18.5 |
| matplotlib base | 3.2.2 |
| imutils | 0.5.3 |
| opencv-python | 4.2.0|
| scipy| 1.4.1 |
| Tensorflow | 2.3 |
| Tensorflow | LITE |

Para la instalación de Tensorflow lite se requiere el archivo wheel apropiado al hardware y software del dispositivo usado [TensorFlow Lite quickstart guide](https://www.tensorflow.org/lite/guide/python). 
En mi caso solo basta con aplicar la siguiente línea en la ventana de comandos:
```sh
$ pip3 install https://dl.google.com/coral/python/tflite_runtime-2.1.0.post1-cp37-cp37m-linux_armv7l.whl
```
#### Archivo Ejecutable
Al ejecutar el archivo Instalaciones.sh en la terminal dentro de la Raspberry Pi, se realizará de forma automática la instalacion de todas las lirerías y dependencias necesarias.
```sh
$ ./Instalaciones.sh
```
