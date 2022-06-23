import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

PHOTOCELL_PIN = 26

GPIO.setup(PHOTOCELL_PIN, GPIO.IN)

try:
    while True:
        val = GPIO.input(PHOTOCELL_PIN)
        print(val)

        sleep(0.1)
except KeyboardInterrupt:
    GPIO.cleanup()
