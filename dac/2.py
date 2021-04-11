import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
change_list = [10,9,11,5,6,13,19,26]
GPIO.setup(change_list, GPIO.OUT)
GPIO.output(change_list, 0)





    

def DecToBin(value):
    if value >= 256:
        value %= 256
    N,p,n = 7,0,[]
    value%=256
    while N>0:
        p=int(value/2**N)
        if p==1:
            n.append(1)
            value-=2**N
        else:
            n.append(0)
        N-=1
    n.append(value)
    return list(reversed(n))


def num2dec(value):
    for i in range(8):
        GPIO.output(change_list[i], list(DecToBin(value))[i])

def num1dec(repetitionsNumber):
    i = repetitionsNumber
    k = 0
    while i > 0:
        while k < 255:
            time.sleep(0.01)
            k = k + 1
            num2dec(k)
        while k > 0:
            time.sleep(0.01)
            k = k - 1
            num2dec(k)
        i = i - 1
    


try:
    repetitionsNumber = 0
    while repetitionsNumber != -1:
        num1dec(repetitionsNumber)
        
        repetitionsNumber=int(input())

finally:
    GPIO.setup(change_list, GPIO.OUT)
    GPIO.setup(change_list, 0)


GPIO.cleanup()