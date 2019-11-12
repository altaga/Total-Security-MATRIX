# Total-Security-MATRIX

<img src="https://i.ibb.co/LtQMtPd/LogoTSdM.png" width="500">

Always use technology to improve the world, if you are a black hat or gray hat hacker please abstain at this point ......... or at least leave your star to make me feel less guilty XP.

# Table of contents

* [Introduction](#introduction)
* [Materials](#materials)
* [Connection Diagram](#connection-diagram)
* [Snips Setup](#snips-setup)
* [AWS Setup](#aws-setup)
* [Raspberry Setup](#raspberry-setup)
* [Esp32 Setup](#esp32-setup)
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

### Widget Configuration:

Press the button to create the widget.

<img src = "https://i.ibb.co/zZSCtkK/image.png" width = "500">

We assign the model to the device.

<img src = "https://i.ibb.co/wC98Vs3/image.png" width = "500">

We create a widget as shown in the image.

<img src = "https://i.ibb.co/tD5b4F3/image.png" width = "500">

We finish the widget.

<img src = "https://i.ibb.co/dkB1cJ0/image.png" width = "500">

We will get a result like the following.

<img src = "https://i.ibb.co/2shLmdn/image.png" width = "500">

### Obtaining Credentials.

Save External access token and User ID.

<img src = "https://i.ibb.co/DCcdzCP/image.png" width = "500">

## CloudMQTT Setup:

Create an account in Cloud MQTT.

https://www.cloudmqtt.com/

Copy the credentials of "Server", "User", "Password" and "Port".

<img src = "https://i.ibb.co/s9wR395/image.png" width = "1000">

## Laptop Setup:

Install Python Anaconda so that you can easily manipulate the MQTT broker, this had to be done because the Arduino library ESP32 for MQTT does not accept connectivity such as Websocket.

https://www.anaconda.com/distribution/

Then install this library:

    pip install paho-mqtt

Download the file Python Files, open "MQTTRehab.py" and put your credentials.

## Arm Setup:

Follow this diagram without making a mistake, IF YOU DON'T CONNECT IT WELL YOU CAN DO A SHORT CIRCUIT:

<img src="https://hackster.imgix.net/uploads/attachments/942233/68747470733a2f2f692e6962622e636f2f4832344451384e2f41524d2d62622e706e67.png" width="800">

After connecting all program the ESP32 with the code in the "Arduino Files" folder.

<img src="https://www.e-ika.com/images/thumbs/0005376_placa-esp32-wifi-bluetooth_600.jpeg" width="800">

Open the "ESP32ARMRehab.ino" file and enter the CloudMQTT credentials.

    const char* ssid = "YOURSSID";
    const char* password =  "YOURPASS";
    const char* mqttServer = "m12.cloudmqtt.com";
    const int mqttPort = 12345;
    const char* mqttUser = "YOURCLOUDMQTTUSER";
    const char* mqttPassword = "YOURCLOUDMQTTPASS";

## The Final Product:

Robotic Arm:

<img src="https://i.ibb.co/X3JNNLB/DSC00056-2.jpg" width="800">
<img src="https://i.ibb.co/HHM2DQ1/DSC00059-2.jpg" width="800">

ESP32 Arm Driver:

<img src="https://i.ibb.co/mJ73KNs/DSC00068.jpg" width="800">

Brainium Module:

<img src="https://i.ibb.co/cFZrYdJ/DSC00061-2.jpg" width="800">
<img src="https://i.ibb.co/kgds0Xn/DSC00062-2.jpg" width="800">
<img src="https://i.ibb.co/xFm1f0T/DSC00063-2.jpg" width="800">

Complete system:

<img src="https://i.ibb.co/dMb7c6V/DSC00066-2.jpg" width="800">

### Our Epic DEMO:

Video: Click on the image
[![Rehab](https://i.ibb.co/Bjg48mh/Brainium-Rehab.png)](https://youtu.be/GYoLvldvk-s)

Sorry github does not allow embed videos.

## Future Rollout:

 inventa algo

## References:

Links 
