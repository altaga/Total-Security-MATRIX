# Total-Security-MATRIX

<img src="https://i.ibb.co/ZByMp41/Logo-only-logo.png" width="500">

Always use technology to improve the world, if you are a black hat or gray hat hacker please abstain at this point ......... or at least leave your star to make me feel less guilty XP.

# Table of contents

* [Introduction](#introduction)
* [Materials](#materials)
* [Connection Diagram](#connection-diagram)
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


## Connection Diagram:

This is the connection diagram of the system:

<img src="https://i.ibb.co/H2GMrM1/Esquema-Rasp.png" width="800">

Lock Connection Diagram:

<img src="https://i.ibb.co/N1B3tgS/MCU.png" width="800">

## Raspberry Setup:

Before performing any other task, it was vital to be able to generate a model for elbow rehabilitation, the system can be extended to any rehabilitation but we chose elbow as the first sample.

4 basic movements were programmed for the rehabilitation of the elbow, of which 3 of them will be used in the final rehabilitation.

Elbow flexoextension:

<img src="https://i.ibb.co/qkX5VfF/image.png" width="400">
<img src="https://i.ibb.co/RBY7K7L/image.png" width="400">

Arm Lift:

<img src="https://i.ibb.co/CzXGq2v/image.png" width="400">
<img src="https://i.ibb.co/XZdHHrS/image.png" width="400">

Elbow Flexion:

<img src="https://i.ibb.co/jkJ4qfd/image.png" width="400">
<img src="https://i.ibb.co/hDrN088/image.png" width="400">

This is the model that was developed and the number of repetitions for each movement:

<img src="https://i.ibb.co/mbXWD8T/image.png" width="400">

Model motion confusion matrix:

<img src="https://i.ibb.co/m4jWHMt/image.png" width="400">

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
