from irobot.robots.create2 import Create2
from irobot.openinterface.constants import MODES
# instantiate robot
port = '/dev/ttyUSB0'
robot = Create2(port)
# read sensor
print(robot.left_encoder_counts)
# change mode to drive (SAFE|FULL)
robot.oi_mode = MODES.FULL
robot.drive_straight(50)
#time.sleep( 5 ) 
# stop driving
robot.drive_straight(0)
# return to passive mode
robot.oi_mode = MODES.PASSIVE
# shutdown OI
robot.stop()
