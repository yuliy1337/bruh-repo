import RPi.GPIO as GPIO
import time

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
    time.sleep(5)
    GPIO.output(LED[0], 0)
    GPIO.output(LED[1], 0)
    GPIO.output(LED[2], 0)
    GPIO.output(LED[3], 0)
    GPIO.output(LED[4], 0)
    GPIO.output(LED[5], 0)
    GPIO.output(LED[6], 0)
    GPIO.output(LED[7], 0)

print("Write a number (-1 for end):")
x = int(input())
while x != -1:
    num2dac(x)
    print("Write a number (-1 for end):")
    x = int(input())
