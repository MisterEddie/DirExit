#import libraries
import time
from socket import*
import RPi.GPIO as GPIO

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

#--------------------------------------------------------------------------------

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


if __name__ == '__main__':
    try:
        while True:
            dist = distance()
            print ("Measured Distance = %.1f cm" % dist)
            time.sleep(1)

            if dist < 5.0:
                #create UDP serverSocket
                clientSocket = socket(AF_INET, SOCK_DGRAM)
                #set timeout to 1 second
                clientSocket.settimeout(1)
                #message to ping server
                ping = "block"
                #send message
                clientSocket.sendto(ping.encode(), address)

                try:
                    message,serverAddress = clientSocket.recvfrom(1024)
                    print(message.decode())

                except timeout:
                    print("Message timed out")

    # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        print("Measurement stopped by User")
        GPIO.cleanup()
