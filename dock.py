from irobot.robots.create2 import Create2
from irobot.openinterface.constants import MODES
import time

port = '/dev/ttyUSB0'
robot = Create2(port)

print(robot.left_encoder_counts)

robot.ou_mode = MODES.SAFE
robot.seek_dock()
