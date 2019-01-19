#!/usr/bin/env python

"""robotCommandServer.py: This is a Flask API server to send commands to iRobot Create2 robot.
This code uses iRobot python wrapper developed my Matther Witherwax to send commands to iRobot Create2.
This code is deployed on the onboard computer conncted to iRobot Create2 and will help to integrate Alexa with iRobot Create2."""

from irobot.robots.create2 import Create2
from irobot.openinterface.constants import MODES
from flask import Flask
import time

__author__ = "Bhargav Nunna"
__copyright__ = "Copyright 2019, Bhargav Nunna"
__credits__ = ["Matthew Witherwax"]
__license__ = "---"
__version__ = "1.0.1"
__maintainer__ = "Bhargav Nunna"
__email__ = "bhargav.vmf33@gmail.com"
__status__ = "Development"

#Globals
cleaning = 0
app = Flask(__name__)

def initateConnnection():
	# instantiate robot
	port = '/dev/ttyUSB0'
	robot = Create2(port)
	return robot
	
@app.route("/clean")
def initiateCleaning():
	robot=initateConnnection()
	# change mode to drive (SAFE|FULL)
	robot.ou_mode = MODES.SAFE
	#start cleaning
	try:
		robot.clean()
		cleaning=1
	except e:
		print(e)
	
	return "Success"

@app.route("/pause")
def pauseCleaning():
	robot=initateConnnection()
	# change mode to drive (SAFE|FULL)
	robot.ou_mode = MODES.SAFE
	#start cleaning
	try:
		if(cleaning ==1):
			robot.clean()
			cleaning=0
			print('Robot paused')
		else:
			print('Robot already pasued. Ignoring request.')
	except e:
		print(e)
	
	return "Success"

@app.route("/dock")
def startSelfDocking():
	robot=initateConnnection()
	# change mode to drive (SAFE|FULL)
	robot.ou_mode = MODES.SAFE
	#start cleaning
	try:
		if(cleaning ==1):
			print('Robot currently in cleaning state. Pausing...')
			pauseCleaning(robot)
		robot.seek_dock()
		print('Robot started docking process.')
	except e:
		print(e)
	
	return "Success"

@app.route("/")
def welcome():
	text = 'Welcome! \n This is Flask server to send commands to iRobot. \nPossible options are: \n /clean \n /dock \n /pause'
	return text

#robot=initateConnnection()

if __name__== '__main__':
	app.run(host='0.0.0.0')