import libhousy
import time
#You can define helper functions here, make sure to but them *above* the main function
startTime = time.time()
def main(robot: libhousy.robot):
    #Here is where your recurring code will go
    if time.time() - startTime < 2:
        robot.lDrive.Set(0.4)
        robot.rDrive.Set(0.4)
    else:
        robot.lDrive.Set(0)
        robot.rDrive.Set(0)
        return libhousy.DONE
    
