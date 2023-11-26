from gpiozero import LED
from time import sleep

led1 = LED(14)
led2 = LED(15)

while True:
    led1.on()
    led2.off()

    sleep(1)
    led2.on()
    led1.off()
    sleep(1)
