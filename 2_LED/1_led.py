import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

LED_PIN = 26

GPIO.setup(LED_PIN, GPIO.OUT)

GPIO.output(LED_PIN, GPIO.HIGH)
