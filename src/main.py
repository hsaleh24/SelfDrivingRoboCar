import RPi.GPIO as GPIO
import time


ENABLE = 13

ECHO = 14
TRIG = 15

SERVO = 12 #PWM pin

def Main():
    print "Main"
    GPIOSetup()
    #TestMotor()
    GPIO.cleanup()
    return;

def TestMotor():
    print "TestMotor"
    GPIO.output(ENABLE, GPIO.HIGH)
    GPIO.output(19, GPIO.HIGH)
    GPIO.output(26, GPIO.LOW)
    time.sleep(10)
    GPIO.output(ENABLE, GPIO.LOW)
    GPIO.output(19, GPIO.LOW)
    GPIO.output(26, GPIO.LOW)
    print "Done"


def GPIOSetup():
    print "GPIOSetup"
    
    GPIO.setmode(GPIO.BCM) #reference pins with BCM vs BOARD numbering

    # MOTOR CONTROL
    GPIO.setup(ENABLE, GPIO.OUT) # ENABLE PIN
    GPIO.setup(19, GPIO.OUT) # 1 of 2 input pins
    GPIO.setup(26, GPIO.OUT) # 2 of 2 input pins

    # SERVO CONTROL
    GPIO.setup(SERVO, GPIO.OUT) # SIGNAL to control angle (PWM)

    # DISTANCE SENSOR
    GPIO.setup(ECHO, GPIO.IN)  # ECHO PIN
    GPIO.setup(TRIG, GPIO.OUT) # TRIGGER PIN
    StartDistanceSensor()
    
    # camera - does it go here? ...is it GPIO?
    return;


def StartDistanceSensor():
    print "StartDistanceSensor"

    GPIO.output(TRIG, GPIO.LOW)
    time.sleep(2)
    
    GPIO.output(TRIG, GPIO.HIGH)
    time.sleep(0.000010) # 10 microsecond
    GPIO.output(TRIG, GPIO.LOW)
    
    MonitorDistanceSensor() # start new task of MonitorDistanceSensor
    return;


def MonitorDistanceSensor(): # setup as a seperate task
    print "MonitorDistanceSensor"

    # get the time of the rising edge of the pulse
    while GPIO.input(ECHO) == 0:
        pulse_start = time.time()

    # get the time of the falling edge of the pulse
    while GPIO.input(ECHO) == 1:
        pulse_end = time.time()

    # get time of pulse and use to calculate distance
    pulse_time = pulse_end - pulse_start
    distance_cm = pulse_time*34300/2; #(convert time to dist give speed of sound = 343m/s)

    print "Distance: ",distance_cm,"cm"
    
    return;

Main()

## should setup all sensors as their own task/thread
## double check PWM pin, i.e. which pins can be setup as PWM on rasp pi 3 and how to do
