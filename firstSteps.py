import libhousy
import time
#You can define helper functions here, make sure to but them *above* the main function
startTime = time.time()
def main(robot: libhousy.robot):
    global startTime
    #Here is where your recurring code will go
    if time.time() - startTime < 2:
        robot.lDrive.Set(0.5)
        robot.rDrive.Set(0.5)
    else:
        robot.lDrive.Set(0)
        robot.rDrive.Set(0)
        return libhousy.DONE
    
