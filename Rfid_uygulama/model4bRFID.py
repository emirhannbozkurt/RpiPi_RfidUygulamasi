from signal import pause
from gpiozero import Servo
import time
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522


#led
led1 = 27
led2 = 22
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(led1,GPIO.OUT)
GPIO.setup(led2,GPIO.OUT)

#servo
servoPIN = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)

p = GPIO.PWM(servoPIN, 50) # GPIO 17 for PWM with 50Hz
p.start(2.5) # Initialization

#rfid
reader = SimpleMFRC522()

#mesafe
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

TRIG = 23
ECHO = 24

print("HC-SR04 mesafe sensoru")

GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)

while True:
    GPIO.output(TRIG, False)
    print("Olculuyor...")
    time.sleep(2)

    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    while GPIO.input(ECHO)==0:
        pulse_start = time.time()

    while GPIO.input(ECHO)==1:
        pulse_end = time.time()

        pulse_duration = pulse_end - pulse_start

        distance = pulse_duration * 17150
        distance = round(distance, 2)
    if distance > 2 and distance < 50:
        GPIO.output(22,GPIO.HIGH)
        GPIO.output(27,GPIO.LOW)
        id, text = reader.read()
        if id==385755034353:
            
            print(id)
            print(text)
            GPIO.output(27,GPIO.HIGH)
            GPIO.output(22,GPIO.LOW)
            print("Kapı açıldı")
            p.ChangeDutyCycle(5)
            time.sleep(0.5)
            p.ChangeDutyCycle(7.5)
            time.sleep(0.5)
            p.ChangeDutyCycle(10)
            time.sleep(0.5)
            p.ChangeDutyCycle(12.5)
            time.sleep(0.5)
            p.ChangeDutyCycle(10)
            time.sleep(0.5)
            p.ChangeDutyCycle(7.5)
            time.sleep(0.5)
            p.ChangeDutyCycle(5)
            time.sleep(0.5)
            p.ChangeDutyCycle(2.5)
            time.sleep(0.5)
            print("Kapı kapandı")
            GPIO.output(27,GPIO.LOW)
            
            
            
        else:
            print("gecersiz")
            GPIO.output(22,GPIO.HIGH)
            GPIO.output(27,GPIO.LOW)
    else:
        print("Kartı yaklaştırın")

