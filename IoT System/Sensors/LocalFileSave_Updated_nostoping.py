# -*- coding: utf-8 -*-
import serial
import time
import requests
import json

firebase_url = 'https://iot-temp-database.firebaseio.com/'
# Connect to Serial Port for communication
ser = serial.Serial('COM4', 9600, timeout=0)
# Setup a loop to send Temperature values at fixed intervals
# in seconds
fixed_interval = 1
# Temperature
while 1:
    try:
        # current time and date
        time_hhmmss = time.strftime('%H:%M:%S')
        date_mmddyyyy = time.strftime('%d/%m/%Y')
        # temperature value obtained from Arduino + DHT Sensor
        dataset = ser.readline()
        if(len(dataset)>3):
            datalist = dataset.split(',')
            if(len(datalist)>3):
                lux=datalist[0]
                temperature = datalist[1]
                hum = datalist[2]
                if(len(datalist[3])!=0 and datalist[3][0]=='Y'):
                    boo=1
                if(len(datalist[3])!=0 and datalist[3][0]=='N'):
                    boo=0
                with open('C:/Users/kevinlee/Desktop/iotdata_413.txt', 'a') as file:
                    file.write(str(boo)+','+str(temperature)+','+str(hum)+','+str(lux)+','+date_mmddyyyy+','+time_hhmmss+'\n')
                print boo
                print temperature
                print hum
                print lux
            
            time.sleep(fixed_interval)
    except IOError:
         print('Error! Something went wrong.')
    time.sleep(fixed_interval)
