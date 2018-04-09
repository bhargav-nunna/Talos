from irobot.robots.create2 import Create2
from irobot.openinterface.constants import MODES
import time
# instantiate robot
port = '/dev/ttyUSB0'
robot = Create2(port)
# read sensor
print(robot.left_encoder_counts)
# change mode to drive (SAFE|FULL)
robot.oi_mode = MODES.SAFE
robot.drive_straight(150)
time.sleep( 3 )
robot.spin_left(150)
time.sleep(1)
robot.drive_straight(150)
robot.spin_right(150)
time.sleep(2)
robot.drive_straight(150)
time.sleep(2)
# stop driving
robot.drive_straight(0)
# return to passive mode
robot.oi_mode = MODES.PASSIVE
# shutdown OI
robot.stop()
