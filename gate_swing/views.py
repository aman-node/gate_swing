from ast import Return
from django.shortcuts import render
import time
from socket import timeout
from serial.tools import list_ports
import serial
import requests


def home(requests):
    frwd = ''
    bcwd = ''
    for ports,desc,hwid in sorted(list_ports.comports()):   
        data=("{}:{} [{}]".format(ports,desc,hwid)+"\n")
        print(data)
    dat1 = serial.Serial(ports, 9600 , timeout=1)
    print(dat1)
    time.sleep(3)
    Forward_gate=dat1.write(b'\x02\x44\x49\x30\x30\x03')
    print('come_in=',Forward_gate)
    frwd = 'come_in=' +str(Forward_gate)
    time.sleep(10)

    Backward_gate=dat1.write(b'\x02\x44\x4F\x30\x30\x03')
    print('go_out=',Backward_gate)
    bcwd = 'go_out='+str(Backward_gate)
    time.sleep(3)
    S=dat1.read(dat1.in_waiting)  
    dat1.close()
    # return bcwd
        # return render(requests,'index.html',context)
    return render(requests,'index.html',{'forward':frwd, 'backward':bcwd})