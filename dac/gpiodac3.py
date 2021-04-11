import RPi.GPIO as GPIO
import time
import numpy as np
import matplotlib.pyplot as plt
import math 

GPIO.setmode(GPIO.BCM)
change_list=[10,9,11,5,6,13,19,26]
GPIO.setup(change_list, GPIO.OUT)
GPIO.output(change_list, 0)
GPIO.setmode(GPIO.BCM)






ndarray=[]
TiMe=int(input())
frequensy=input()
samplightFrequensy=float(input())


try:
    tim = np.arange(0, TiMe, 1/samplightFrequensy)
    amplitude=np.sin(tim*2*3.1415926*float(frequensy))
    for i in range(len(amplitude)):
        amplitude[i]+=1
        amplitude[i]*=127
    plt.plot(tim, amplitude)
    plt.title('Sin')
    plt.xlabel('Time')
    plt.ylabel('Amplitude sin(time)')
    plt.show()
    for i in range(len(amplitude)):
        LightNumber(math.floor(amplitude[i]))
        time.sleep(1/samplightFrequensy)

finally:
    GPIO.setup(change_list, GPIO.OUT)
    GPIO.output(change_list, 0)