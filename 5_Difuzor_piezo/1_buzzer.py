import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

BUZZER_PIN = 12

GPIO.setup(BUZZER_PIN, GPIO.OUT)

buzzer = GPIO.PWM(BUZZER_PIN, 1000)
buzzer.start(10)

sleep(1)

buzzer.ChangeFrequency(3000)

sleep(1)

GPIO.cleanup()
