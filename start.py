#!/usr/bin/env python
# -*- coding: utf-8 -*-

from irobot.robots.create2 import Create2
from irobot.openinterface.constants import MODES
from flask import Flask
from flask_restful import Api, Rescource, reqparse

import time

#Globals
cleaning = 0


def initateConnnection():
	# instantiate robot
	port = '/dev/ttyUSB0'
	robot = Create2(port)
	return robot
	
 
def initiateCleaning(robot):
	# change mode to drive (SAFE|FULL)
	robot.ou_mode = MODES.SAFE
	#start cleaning
	try:
		robot.clean()
		cleaning=1
	except e:
		print(e)

def pauseCleaning(robot):
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

def startSelfDocking(robot):
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
		

def main():
	robot=initateConnnection()
	initiateCleaning(robot)
	pauseCleaning(robot)
	startSelfDocking(robot)
	
	

if __name__== '__main__':
	main()