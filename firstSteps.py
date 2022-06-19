import libhousy
import time
#You can define helper functions here, make sure to but them *above* the main function
startTime = 0
def main(robot: libhousy.robot):
    global startTime
    if startTime == 0:
        startTime = time.time()
    if time.time() - startTime < 4:
        robot.lDrive.Set(0.6)
        robot.rDrive.Set(0.6)
    else:
        robot.lDrive.Set(0)
        robot.rDrive.Set(0)
    
    
    return libhousy.DONE
