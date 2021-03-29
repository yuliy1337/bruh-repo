import RPi.GPIO as GPIO
import time
import math

GPIO.setmode(GPIO.BCM)
GPIO.setup(10, GPIO.OUT)
GPIO.setup(9, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(5, GPIO.OUT)
GPIO.setup(6, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(19, GPIO.OUT)
GPIO.setup(26, GPIO.OUT)

LED = [10, 9, 11, 5, 6, 13, 19, 26]

def decToBinList(decNumber):
    s = str(bin(decNumber))
    s = s[2:]
    i = len(s) - 1
    j = 0
    A = [0]*8
    while i >= 0:
        A[j] = s[i]
        i -= 1
        j += 1
    return A

def num2dac(value):
    BinList = decToBinList(value)
    for i in range(len(BinList)):
        if int(BinList[i]) == 1:
            GPIO.output(LED[i], 1)
    time.sleep(0.3)



def ad(repetitionsNumber):
    for i in range (repetitionsNumber):
        for g in range (0, 256):
            num1dac(g)
        for s in range (255, -1 ,-1):
            num1dac(s)

def num1dac(n):
    dac_data(decToBinList(n))
    time.sleep(0.1)

GPIO.setwarnings(False)
GPIO.output(LED, 0)
GPIO.cleanup()

x=int(input())
ad(x)