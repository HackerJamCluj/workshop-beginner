import RPi.GPIO as GPIO
from time import sleep, time_ns

GPIO.setmode(GPIO.BCM)

PHOTOCELL_PIN = 26

GPIO.setup(PHOTOCELL_PIN, GPIO.IN)

last_val = 1
start_time = None

hand_size = 9

try:
    while True:
        val = GPIO.input(PHOTOCELL_PIN)
        if val == 0 and start_time == None:
            start_time = time_ns()

        if val == 1 and start_time != None:
            time_delta = time_ns() - start_time
            start_time = None
            print(f"Speed: {hand_size / (time_delta/1_000_000_000)} cm/s")
            
        sleep(0.1)
except KeyboardInterrupt:
    GPIO.cleanup()
