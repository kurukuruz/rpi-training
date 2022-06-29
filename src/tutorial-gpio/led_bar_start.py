import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

ids = list(range(18, 28))

# setup
GPIO.setup(ids, GPIO.OUT)

# water
for id in ids:
  GPIO.output(id, GPIO.HIGH)
  time.sleep(0.3)
  GPIO.output(id, GPIO.LOW)

# all blink
for num in range(2):
  GPIO.output(ids, GPIO.HIGH)
  time.sleep(0.3)

  GPIO.output(ids, GPIO.LOW)
  time.sleep(0.3)

GPIO.output(ids, GPIO.HIGH)
time.sleep(1)
GPIO.output(ids, GPIO.LOW)

GPIO.cleanup()
