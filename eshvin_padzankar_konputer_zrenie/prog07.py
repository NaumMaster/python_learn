import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(3, GPIO.OUT, initial=False)
GPIO.setup(5, GPIO.OUT, initial=False)
GPIO.setup(7, GPIO.OUT, initial=False)
GPIO.setup(8, GPIO.OUT, initial=False)
GPIO.setup(10, GPIO.OUT, initial=False)
GPIO.setup(12, GPIO.OUT, initial=False)
GPIO.setup(11, GPIO.OUT, initial=False)
GPIO.setup(13, GPIO.OUT, initial=False)

def migmig():
    GPIO.output(13, True)
    sleep(0.5)
    GPIO.output(13, False)
    sleep(0.5)
    GPIO.output(13, True)
    sleep(0.5)

def zero():
    GPIO.output(3, True)
    GPIO.output(5, True)
    GPIO.output(7, True)
    GPIO.output(8, True)
    GPIO.output(10, True)
    GPIO.output(12, True)
    GPIO.output(11, False)
    GPIO.output(13, False)

def one():
    GPIO.output(3, False)
    GPIO.output(5, True)
    GPIO.output(7, True)
    GPIO.output(8, False)
    GPIO.output(10, False)
    GPIO.output(12, False)
    GPIO.output(11, False)
    GPIO.output(13, False)

def two():
    GPIO.output(3, True)
    GPIO.output(5, True)
    GPIO.output(7, False)
    GPIO.output(8, True)
    GPIO.output(10, True)
    GPIO.output(12, False)
    GPIO.output(11, True)
    GPIO.output(13, False)

def three():
    GPIO.output(3, True)
    GPIO.output(5, True)
    GPIO.output(7, True)
    GPIO.output(8, True)
    GPIO.output(10, False)
    GPIO.output(12, False)
    GPIO.output(11, True)
    GPIO.output(13, False)

def four():
    GPIO.output(3, False)
    GPIO.output(5, True)
    GPIO.output(7, True)
    GPIO.output(8, False)
    GPIO.output(10, False)
    GPIO.output(12, True)
    GPIO.output(11, True)
    GPIO.output(13, False)

def five():
    GPIO.output(3, True)
    GPIO.output(5, False)
    GPIO.output(7, True)
    GPIO.output(8, True)
    GPIO.output(10, False)
    GPIO.output(12, True)
    GPIO.output(11, True)
    GPIO.output(13, False)

def six():
    GPIO.output(3, True)
    GPIO.output(5, False)
    GPIO.output(7, True)
    GPIO.output(8, True)
    GPIO.output(10, True)
    GPIO.output(12, True)
    GPIO.output(11, True)
    GPIO.output(13, False)

def seven():
    GPIO.output(3, True)
    GPIO.output(5, True)
    GPIO.output(7, True)
    GPIO.output(8, False)
    GPIO.output(10, False)
    GPIO.output(12, False)
    GPIO.output(11, False)
    GPIO.output(13, False)

def eight():
    GPIO.output(3, True)
    GPIO.output(5, True)
    GPIO.output(7, True)
    GPIO.output(8, True)
    GPIO.output(10, True)
    GPIO.output(12, True)
    GPIO.output(11, True)
    GPIO.output(13, False)

def nine():
    GPIO.output(3, True)
    GPIO.output(5, True)
    GPIO.output(7, True)
    GPIO.output(8, False)
    GPIO.output(10, False)
    GPIO.output(12, True)
    GPIO.output(11, True)
    GPIO.output(13, False)


while True:
    zero()
    sleep(0.5)
    migmig()
    
    one()
    sleep(0.5)
    migmig()
    
    two()
    sleep(0.5)
    migmig()

    three()
    sleep(0.5)
    migmig()

    four()
    sleep(0.5)
    migmig()

    five()
    sleep(0.5)
    migmig()

    six()
    sleep(0.5)
    migmig()

    seven()
    sleep(0.5)
    migmig()

    eight()
    sleep(0.5)
    migmig()

    nine()
    sleep(0.5)
    migmig()

    

