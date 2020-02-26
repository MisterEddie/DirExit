#import libraries
import time
from socket import*
import RPi.GPIO as GPIO
import sys
import math
import subprocess
import os
import datetime
from grove.factory import Factory
from grove.helper import SlotHelper
from grove.adc import ADC
from grove.helper import SlotHelper

pinTemp = 0# sh.argv2pin() A0, A2
pinLight = 4 #ANALOG
rightLED = 23
leftLED = 24
__all__ = ["GroveLightSensor"]

#networking setup
port = 12000
ip_to_send_to = "172.20.10.10" #servername
address = (ip_to_send_to, port)

#GPIO Mode Setup (BOARD/BCM, BCM - GPIO)
GPIO.setmode(GPIO.BCM)
#GPIO PINS
GPIO_TRIGGER = 14
GPIO_ECHO = 15

#set GPIO direction (IN / OUT)
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)

#light indicator GPIO
GPIO.setwarnings(False)
GPIO.setup(rightLED, GPIO.OUT)
GPIO.setup(leftLED, GPIO.OUT)

#flag
blocked = False
#--------------------------------------------------------------------------------
class GroveLightSensor(object):
    '''
    Grove Light Sensor class
    Args:
        pin(int): number of analog pin/channel the sensor connected.
    '''
    def __init__(self, channel):
        self.channel = channel
        self.adc = ADC()

    @property
    def light(self):
        '''
        Get the light strength value, maximum value is 100.0%
        Returns:
            (int): ratio, 0(0.0%) - 1000(100.0%)
        '''
        value = self.adc.read(self.channel)
        return value

Grove = GroveLightSensor

def distance():
    # set Trigger to HIGH
    GPIO.output(GPIO_TRIGGER, True)

    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)

    StartTime = time.time()
    StopTime = time.time()
    # save StartTime
    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()

    # save time of arrival
    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()

    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = (TimeElapsed * 34300) / 2

    return distance

def get_temp():
    sensor = Factory.getTemper("NTC-ADC", pinTemp)
    #print('{} Celsius'.format(sensor.temperature))
    return sensor.temperature

def get_light():
    sensor = GroveLightSensor(pinLight)
    return sensor.light

if __name__ == '__main__':
    try:
        f = open('logfile.txt','a')

        while True:

            dist = distance()
            print ("Measured Distance = %.1f cm  " % dist, end='')
            temp = get_temp()
            print('{} Celsius  '.format(temp), end='')
            lightness = get_light()
            print('Light value: {0}'.format(lightness))
            time.sleep(0.5)
            clientSocket = socket(AF_INET, SOCK_DGRAM)
            clientSocket.settimeout(3)

            google_send = "Distance: "+str(dist)+" Temperature: "+str(temp)+" Brightness: "+str(lightness) + " Date: " + str(datetime.datetime.now())
            clientSocket.sendto(google_send.encode(), address)

            if dist < 5.0 or temp > 26 or lightness < 500:
                blocked = True
                print("Path is blocked")
                #message to ping server
                ping = "block"
                #ping = True
                #send message
                clientSocket.sendto(ping.encode(), address)

                try:
                    message,serverAddress = clientSocket.recvfrom(1024)
                    print(message.decode())
                except timeout:
                    print("Message timed out")

            else:
                blocked = False
                ping = "not"
                #ping = False
                clientSocket = socket(AF_INET, SOCK_DGRAM)
                clientSocket.sendto(ping.encode(), address)
                clientSocket.settimeout(3)

                try:
                    message,serverAddress = clientSocket.recvfrom(1024)
                    print(message.decode())
                except timeout:
                    print("Message timed out")

            if not blocked:
                GPIO.output(rightLED, GPIO.HIGH)
                GPIO.output(leftLED, GPIO.LOW)
            else:
                GPIO.output(leftLED, GPIO.HIGH)
                GPIO.output(rightLED, GPIO.LOW)
    # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        f.close
        print("Measurement stopped by User")
        GPIO.cleanup()
# gsutil cp -r .\logfile.txt\ gs://direxit
