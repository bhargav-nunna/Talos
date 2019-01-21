from irobot.robots.create2 import Create2
from irobot.openinterface.constants import MODES
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
	try:
		robot = Create2(port)
		print(robot.left_encoder_counts)
		print port
		print 'Worked!'
		# do something to check this port is open.
