import serial
import time

STM32 = serial.Serial('COM5',57600)

while True:
    time.sleep(1)
    text = STM32.read().decode('ascii')
    print(text)

STM32.close()

