import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

LED_PIN = 26

GPIO.setup(LED_PIN, GPIO.OUT)

try:
    while True:
        GPIO.output(LED_PIN, GPIO.HIGH)
        sleep(2)
        GPIO.output(LED_PIN, GPIO.LOW)
        sleep(2)
except KeyboardInterrupt:
    GPIO.cleanup()
