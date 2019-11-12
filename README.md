# Total-Security-MATRIX

<img src="https://i.ibb.co/LtQMtPd/LogoTSdM.png" width="500">

Always use technology to improve the world, if you are a black hat or gray hat hacker please abstain at this point ......... or at least leave your star to make me feel less guilty XP.

# Table of contents

* [Introduction](#introduction)
* [Materials](#materials)
* [Connection Diagram](#connection-diagram)
* [Snips Setup](#snips-setup)
* [AWS Setup](#aws-setup)
* [Your Image Setup](#your-image-setup)
* [Raspberry Setup](#raspberry-setup)
* [Esp8266 Setup](#esp8266-setup)
* [Case](#case)
* [The Final Product](#the-final-product)
* [Future Rollout](#future-rollout)
* [References](#references)

## Introduction:



## Materials:

Hardware Snips Module:

- RaspberryPi 3 B                                              x1.

https://www.raspberrypi.org/products/raspberry-pi-3-model-b/

- 5v - 2.5A Source                                             x1.

https://www.amazon.com/dp/B00MARDJZ4/ref=cm_sw_em_r_mt_dp_U_OeHYDbCX06MWR

- WebCam (Any webcam is fine)                                  x1.

https://www.amazon.com/dp/B06ZXXYRL3/ref=cm_sw_em_r_mt_dp_U_2iHYDb88SG8FE

Hardware Lock Module:

- 12v - 2A Source                                              x1.

https://www.amazon.com/dp/B01GD4ZQRS/ref=cm_sw_em_r_mt_dp_U_SoHYDbZJ30G2F

- Breadboard Power Supply Module (or any 12v to 3.3v circuit)  x1.

https://www.amazon.com/dp/B010UJFVTU/ref=cm_sw_em_r_mt_dp_U_-qHYDb736C7JG

- ESP8266 (NodeMCU)                                            x1.

https://www.amazon.com/dp/B010O1G1ES/ref=cm_sw_em_r_mt_dp_U_1fHYDbYBWXF12

- Tip120                                                       x1.

https://www.amazon.com/dp/B00NAY1IBS/ref=cm_sw_em_r_mt_dp_U_IhHYDbX7FENP6

- Lock Assembly Solenoid DC 12V                                x1.

https://www.amazon.com/dp/B01FH1JCPU/ref=cm_sw_em_r_mt_dp_U_PMKYDb9ASPK24

- Diode 4007                                                   x1.

https://www.amazon.com/dp/B07YYL4LFP/ref=cm_sw_em_r_mt_dp_U_clHYDbH76KJP9

- 2.2k Ohms Resistor                                           x1.

https://www.amazon.com/dp/B07WGMZ7ZD/ref=cm_sw_em_r_mt_dp_U_jmHYDbVXDX16F

Software:

- Anrduino IDE.

- Sam Command Line Interface.

- Python Anaconda (Only for Debugging).

- AWS Cloud.

## Connection Diagram:

This is the connection diagram of the system:

<img src="https://i.ibb.co/H2GMrM1/Esquema-Rasp.png" width="800">

Lock Connection Diagram:

<img src="https://i.ibb.co/N1B3tgS/MCU.png" width="800">

## Snips Setup:

If you are noob with Snips consider follow the Snips official guide. 
https://docs.snips.ai/getting-started/quick-start-console

Despues de este tutorial deberias de poder ver la siguiente ventana:

<img src="https://i.ibb.co/kSxtWsZ/Capture.png" width="400">

Una vez presiones el boton de "Deploy Assistant" deberas obtener el siguiente comando, este comando lo guardaremos para la configuracion de la Raspberry.

<img src="https://i.ibb.co/VwyFJdz/Untitled-1.png" width="400">

Command:

    sam install assistant -i proj_XXXXXXXXXXX

## Aws Setup:

To communicate with Snips with AWS Rekognition Service we need to create a User in the IAM console in order to authorize our RPI use the service.

- The first step is to create a User that allows us to communicate with AWS.

<img src = "https://i.ibb.co/gdQNnTJ/image.png" width = "700">

- Configurar el usuario de la siguiente forma.

<img src = "https://i.ibb.co/pJGZkT1/image.png" width = "700">

- Añadir el siguiente permiso para utilizar el servicio de AWS Rekognition.

<img src = "https://i.ibb.co/DgKqHfs/image.png" width = "700">

- Una ves creemos el usuario tendremos que guardar el "Access key ID" y el "Secret access key".

<img src = "https://i.ibb.co/hDGSsRD/image.png" width = "700">

## Your Image Setup:

- Toma una imagen tuya de cara, preferentemente bien iluminada y con un fondo sencillo.

- Una vez tengas el archivo en png pegalo en la carpeta "/home/pi" para que el programa funcione correctamente.

<img src = "https://i.ibb.co/g3BpLch/image.png" width = "700">

## Raspberry Setup:

If you are noob consider setting up your raspberry with the following tutorial. 

https://projects.raspberrypi.org/en/projects/raspberry-pi-setting-up

Especificamente necesitas bajar el siguiente sistema operativo, ya que es la ultima version de Raspbian qie es compatible con SNIPS.

http://downloads.raspberrypi.org/raspbian/images/raspbian-2019-04-09/2019-04-08-raspbian-stretch.zip

Si quieres intentar bajar otra version antigua de Raspbian, aqui el enlace con todos las versiones de raspbian de la historia.

http://downloads.raspberrypi.org/raspbian/images/

Para la siguiente parte seguir la documentacion oficial de Matrix para instalar el microfono correctamente:

https://matrix-io.github.io/matrix-documentation/matrix-creator/resources/microphone/

Ahora antes de proseguir, en tu computadora seguir el siguiente tutorial para instalar el Sam Command Line Interface que es el software de snips para realizar la instalacion y el debugging de Snips.

En mi caso yo uso windows.
https://docs.snips.ai/getting-started/quick-start-raspberry-pi

Antes de usar el comando "sam test speaker" realizar lo siguiente:

- Add (portaudio_playback = "default") to the [snips-audio-server] section of your (/etc/snips.toml) configuration file. Use the next command for edit. 

        sudo nano /etc/snips.toml

- Usar el siguiente comando despues de eso.

        sudo systemctl restart snips-audio-server

Dejar la guia oficial y utiliza los siguientes comandos:

- Primero iniciemos sesion en SAM.

        sam login

- Una vez hayamos iniciado sesion correctamente, correr el comando que guardamos en la parte anterior.
NOTA: el comando tenemos que correrlo 2 veces.

        sam install assistant -i proj_XXXXXXXXXXX
    
- Ya que hayamos terminado esta configuracion solo hace falta ir al escritorio de la Raspberry y seleccionar manualmente la salida analoga de audio, para abrir el menu de seleccion de salida de audio, haz clic derecho en el icono de audio y saldra el menu.

<img src = "https://i.ibb.co/gMzjLcy/Analog.png">

- Lo siguiente sera seguir la siguiente guia oficial de Matrix.

https://matrix-io.github.io/matrix-documentation/matrix-core/getting-started/core-installation/

- Una vez termines esa guia realizar la siguiente guia, sin embargo antes de ejecutar "pip3 install -r requirements.txt", detente y ve al siguiente punto.

https://matrix-io.github.io/matrix-documentation/matrix-core/getting-started/python-installation/

- Cuando pases a este punto ejecuta los siguientes comandos.

        pip3 install boto3 appdirs==1.4.3 backports-abc==0.5 certifi==2017.4.17 matrix_io-proto==0.0.10 packaging==16.8 protobuf==3.3.0 pyparsing==2.2.0 pyzmq==16.0.2 singledispatch==3.4.0.3 six==1.10.0 tornado==4.5.1

        sudo apt-get install matrixio-protobuf libmatrixio-malos matrixio-malos -y

        mv utils.py /home/pi/.local/lib/python3.5/site-packages

        sudo reboot

        sudo nano app.py

- Este ultimo comando nos abrira el editor de texto donde podremos pegar el codigo en la carpeta de "Raspberry Code".

- Una vez hayamos guardado nuestro codigo, instalaremos el AWS CLI para proporcionarle a la Raspberry el acceso a AWS Rekognition.

        sudo apt-get install awscli

- Una vez instalado el CLI con el siguiente comando configuraremos todo.

        aws configure
        AWS Access Key ID [None]: YOURACCESKEY
        AWS Secret Access Key [None]: YOURSECRET
        Default region name [None]: us-east-1
        Default output format [None]: json
        
- Una vez configurado correctamente AWS CLI corremos los siguientes comandos para finalizar el Setup de la Raspberry.

        pip3 install opencv-python
        sudo apt-get install libatlas-base-dev
        sudo apt-get install libjasper-dev
        sudo apt-get install libqtgui4
        sudo apt-get install python3-pyqt5
        sudo apt install libqt4-test
        
- Debido a la configuracion de SNIPS, este inicia con la raspberry, osea que su asistente siempre correra sin problema, ahora tenemos que configurar que nuestro programa corra desde el inicio de la raspberry.

https://www.instructables.com/id/Raspberry-Pi-Launch-Python-script-on-startup/

- Terminado esto corre el siguiente comando para obtener el ip para el mqtt.

        hostname -I

- Una vez todo configurado ahora si corre el siguiente comando y una vez reiniciado, todo deberia funcionar perfectamente.

        sudo reboot
        
## Esp8266 Setup:

Si pudiste armar correctamente el circuito mostrado en "Connection Diagram" carga el programa en la carpeta de "ESP Code", pero cambiando los siguientes datos a los datos de tu red y Mqtt.

        const char* ssid = "YOUR_SSID";
        const char* password =  "YOUR_PASS";
        const char* mqttServer = "YOUR_RPI_IP";
        
Una vez subido el programa al ESP ya todo estara listo para poner todo en una bonita Case.

## Case

LE DOK DALE AQUI.

## The Final Product:

Snips Module:

<img src="https://i.ibb.co/s1j880V/DSC00122.jpg" width="800">
<img src="https://i.ibb.co/mRjGTXz/DSC00123.jpg" width="800">
<img src="https://i.ibb.co/ChHSVt6/DSC00124.jpg" width="800">
<img src="https://i.ibb.co/Jd2qfhz/DSC00120.jpg" width="800">

ESP8266 Lock Module:

<img src="https://i.ibb.co/Qk1546p/DSC00126.jpg" width="800">
<img src="https://i.ibb.co/X5W3cWK/DSC00131.jpg" width="800">
<img src="https://i.ibb.co/7XsFvsb/DSC00132.jpg" width="800">

### Our Epic DEMO:

Video: Click on the image
[![Rehab](https://i.ibb.co/LtQMtPd/LogoTSdM.png)](https://youtu.be/4hl60aqGA-g)

Sorry github does not allow embed videos.

## Future Rollout:

 inventa algo

## References:

Links 
