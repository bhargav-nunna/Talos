#import serial as ser
#import serial.tools.list_ports as prtlst

#global COMs
#COMs=[]
#def getCOMs():
#    global COMs
#    pts= prtlst.comports()
#
#    for pt in pts:
#        if 'USB' in pt[1]: #check 'USB' string in device description
#            COMs.append(pt[0])



import glob

def scan():
    return glob.glob('/dev/tty*') + glob.glob('/dev/cu*')

for port in scan():
    print port
   # do something to check this port is open.
