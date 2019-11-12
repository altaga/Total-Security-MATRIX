# -*- coding: utf-8 -*-
"""
Created on Sat Aug 24 12:26:19 2019

@author: VAI
"""

import paho.mqtt.client as mqtt
import json
import boto3
import cv2
## Set Initial Variables ##
import os # Miscellaneous operating system interface
import zmq # Asynchronous messaging framework
import time # Time access and conversions
from random import randint # Random numbers
import sys # System-specific parameters and functions
# Handy function for connecting to the Error port 
from utils import register_error_callback
from matrix_io.proto.malos.v1 import driver_pb2 # MATRIX Protocol Buffer driver library
from matrix_io.proto.malos.v1 import io_pb2 # MATRIX Protocol Buffer sensor library
from multiprocessing import Process, Manager, Value # Allow for multiple processes at once
from zmq.eventloop import ioloop, zmqstream# Asynchronous events through ZMQ
matrix_ip = '127.0.0.1' # Local device ip
everloop_port = 20021 # Driver Base port
led_count = 0 # Amount of LEDs on MATRIX device
flag=False
Color=""

def compare_faces(sourceFile, targetFile):

    client=boto3.client('rekognition')
   
    imageSource=open(sourceFile,'rb')
    imageTarget=open(targetFile,'rb')
    
    response=None

    response=client.compare_faces(SimilarityThreshold=80,
                                  SourceImage={'Bytes': imageSource.read()},
                                  TargetImage={'Bytes': imageTarget.read()})
    for faceMatch in response['FaceMatches']:
        position = faceMatch['Face']['BoundingBox']
        similarity = str(faceMatch['Similarity'])
        print('The face at ' +
               str(position['Left']) + ' ' +
               str(position['Top']) +
               ' matches with ' + similarity + '% confidence')

    imageSource.close()
    imageTarget.close()    
    return len(response['FaceMatches'])    

def on_connect(client, userdata, flags, rc):
    print("rc: " + str(rc))

def on_message(client, obj, msg):
    global flag
    global Color
    topic=msg.topic
    if(topic=="esp/test"):
        print("ESP Online")
    else:
        y = json.loads(msg.payload.decode())
        print(y["intent"]["intentName"])
        print(y["slots"][0]["value"]["value"])
        lock=y["slots"][0]["value"]["value"]
        flag=True
        if(lock=="open" or lock=="unlock"):
            cap = cv2.VideoCapture(0)
            ret, frame = cap.read()
            cv2.imwrite( "image.jpg", frame );
            target_file='image.jpg'
            source_file='myface.jpg'
            face_matches=compare_faces(source_file, target_file)
            if(face_matches>0):
                print("Yes my lord")
                Color="green"   
            else:
                Color="red"
        else:
            Color="none"
               
def on_publish(client, obj, mid):
    print("mid: " + str(mid))

def on_subscribe(client, obj, mid, granted_qos):
    print("Subscribed: " + str(mid) + " " + str(granted_qos))

def on_log(client, obj, level, string):
    #print(string)
    ...

def ping_socket():
    # Define zmq socket
    context = zmq.Context()
    # Create a Pusher socket
    ping_socket = context.socket(zmq.PUSH)
    # Connect to the socket
    ping_socket.connect('tcp://{0}:{1}'.format(matrix_ip, everloop_port+1))
    # Ping with empty string to let the drive know we're still listening
    ping_socket.send_string('')

def everloop_error_callback(error):
    # Log error
    print('{0}'.format(error))

## DATA UPDATE PORT ##
def update_socket():
    # Define zmq socket
    context = zmq.Context()
    # Create a Subscriber socket
    socket = context.socket(zmq.SUB)
    # Connect to the Data Update port
    socket.connect('tcp://{0}:{1}'.format(matrix_ip, everloop_port+3))
    # Connect Subscriber to Error port
    socket.setsockopt(zmq.SUBSCRIBE, b'')
    # Create the stream to listen to data from port
    stream = zmqstream.ZMQStream(socket)

    # Function to update LED count and close connection to the Data Update Port
    def updateLedCount(data):
        # Extract data and pass into led_count global variable
        global led_count
        led_count = io_pb2.LedValue().FromString(data[0]).green
        # Log LEDs
        print('{0} LEDs counted'.format(led_count))
        # If LED count obtained
        if led_count > 0:
            # Close Data Update Port connection
            ioloop.IOLoop.instance().stop()
            print('LED count obtained. Disconnecting from data publisher {0}'.format(everloop_port+3))
    # Call updateLedCount() once data is received
    stream.on_recv(updateLedCount)

    # Log and begin event loop for ZMQ connection to Data Update Port
    print('Connected to data publisher with port {0}'.format(everloop_port+3))
    ioloop.IOLoop.instance().start()

## BASE PORT ##
def config_socket(ledCount): 
    global flag
    global Color
    # Define zmq socket
    context = zmq.Context()
    # Create a Pusher socket
    socket = context.socket(zmq.PUSH)
    # Connect Pusher to configuration socket
    socket.connect('tcp://{0}:{1}'.format(matrix_ip, everloop_port))

    rc = 0
    
    driver_config_proto = driver_pb2.DriverConfig()
    # Create an empty Everloop image
    image = []
    # For each device LED
    for led in range(ledCount):
        # Set individual LED value
        ledValue = io_pb2.LedValue()
        ledValue.blue = 10
        ledValue.red = 10
        ledValue.green = 10
        ledValue.white = 0
        image.append(ledValue)

    # Store the Everloop image in driver configuration
    driver_config_proto.image.led.extend(image)

    # Send driver configuration through ZMQ socket
    socket.send(driver_config_proto.SerializeToString())

    client = mqtt.Client()
    client.connect("raspberrypi.local", 1883)
    client.subscribe("hermes/nlu/intentParsed")
    client.subscribe("esp/test")
    client.on_message = on_message
    client.on_connect = on_connect
    client.on_publish = on_publish
    client.on_subscribe = on_subscribe
    client.on_log = on_log

    while rc == 0:
        rc = client.loop()
        if(flag):
            # Create a new driver config
            driver_config_proto = driver_pb2.DriverConfig()
            # Create an empty Everloop image
            image = []
            # For each device LED
            if(Color=="red"):
                for led in range(ledCount):
                    # Set individual LED value
                    ledValue = io_pb2.LedValue()
                    ledValue.blue = 0
                    ledValue.red = 100
                    ledValue.green = 0
                    ledValue.white = 0
                    image.append(ledValue)
            elif(Color=="blue"):
                for led in range(ledCount):
                    # Set individual LED value
                    ledValue = io_pb2.LedValue()
                    ledValue.blue = 100
                    ledValue.red = 0
                    ledValue.green = 0
                    ledValue.white = 0
                    image.append(ledValue)
            elif(Color=="green"):
                client.publish("esp/lock", "Hello")
                for led in range(ledCount):
                    # Set individual LED value
                    ledValue = io_pb2.LedValue()
                    ledValue.blue = 0
                    ledValue.red = 0
                    ledValue.green = 100
                    ledValue.white = 0
                    image.append(ledValue)
            else:
                for led in range(ledCount):
                    # Set individual LED value
                    ledValue = io_pb2.LedValue()
                    ledValue.blue = 10
                    ledValue.red = 10
                    ledValue.green = 10
                    ledValue.white = 0
                    image.append(ledValue)

            # Store the Everloop image in driver configuration
            driver_config_proto.image.led.extend(image)

            # Send driver configuration through ZMQ socket
            socket.send(driver_config_proto.SerializeToString())
            #Wait before restarting loop

            time.sleep(10)
             # Create a new driver config
            driver_config_proto = driver_pb2.DriverConfig()
            # Create an empty Everloop image
            image = []
            # For each device LED
            for led in range(ledCount):
                # Set individual LED value
                ledValue = io_pb2.LedValue()
                ledValue.blue = 10
                ledValue.red = 10
                ledValue.green = 10
                ledValue.white = 0
                image.append(ledValue)

            # Store the Everloop image in driver configuration
            driver_config_proto.image.led.extend(image)

            # Send driver configuration through ZMQ socket
            socket.send(driver_config_proto.SerializeToString())

            flag=False

if __name__ == "__main__":
        # Initiate asynchronous events
    ioloop.install()
    # Start Error Port connection
    Process(target=register_error_callback, args=(everloop_error_callback, matrix_ip, everloop_port)).start()    

    # Ping the Keep-alive Port once
    ping_socket()
    # Start Data Update Port connection & close after response
    update_socket()
    # Send Base Port configuration
    try:
        config_socket(led_count)
    # Avoid logging Everloop errors on user quiting
    except KeyboardInterrupt:
        print(' quit')
