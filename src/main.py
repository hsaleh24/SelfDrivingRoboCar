import RPi.GPIO as GPIO
import time


def Main():
    #GPIOSetup()
    return;


def GPIOSetup():
    GPIO.setmode(GPIO.BCM) #reference pins with BCM vs BOARD numbering

    # MOTOR CONTROL
    GPIO.setup(13, GPIO.OUT) # ENABLE PIN
    GPIO.setup(19, GPIO.OUT) # 1 of 2 input pins
    GPIO.setup(26, GPIO.OUT) # 2 of 2 input pins

    # SERVO CONTROL
    GPIO.setup(23, GPIO.OUT) # GRND
    GPIO.setup(24, GPIO.OUT) # SIGNAL to control angle (PWM)

    # DISTANCE SENSOR
    GPIO.setup(14, GPIO.IN)  # ECHO PIN
    GPIO.setup(15, GPIO.OUT) # TRIGGER PIN
    
    # camera - does it go here? ...is it GPIO?
    return;


def StartDistanceSensor():
    GPIO.output(14, GPIO.HIGH)
    time.sleep(0.000010) # 10 microsecond
    GPIO.output(14, GPIO.LOW)
    return;


def MonitorDistanceSensor(): # setup as a seperate task
    return;
    
## should setup all sensors as their own task/thread
## also make sure to put the pin numbers as constants
## double check PWM pin, i.e. which pins can be setup as PWM on rasp pi 3 and how to do
