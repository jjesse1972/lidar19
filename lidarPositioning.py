from rplidar import RPLidar
import time


class fieldCoordinates:
    """A frame manager for lidar. This class is responsible for reading lidar data 
    and maintainning a data frame the represents the latest 360 degree view of the field"""

    mLidar = None
    min_frame_len = 120 # based on onbservation, a scan returns between 125 and 135 points
    max_loop = 5 # arbitrary value
   
    def __init__(self, lidarDevice):
            self.mLidar = lidarDevice

    def getCurrentPosition(self,gyro):
        """Returns current position of the robot based on evaluation of a lidar field scan"""

        fieldScan = self.getMostRecentFrame()

        towers = self.extractFeatures(fieldScan)

        return self.calculatePosition(towers, gyro)

    def getMostRecentFrame(self):
        """The purpose of this method is to return the latest lidar field scan"""
        
        #  flush any stale data to ensure that we are getting the latest scan
        self.mLidar.clear_input() 

        # return the first scan from RPLidar that meets minimum legth. 
        # RPLidar.iter_scan provides basic frame manageemnt for us
        for i,recentFrame in enumerate(self.mLidar.iter_scans()):
            if len(recentFrame) > self.min_frame_len:
                return recentFrame;

            if i > self.max_loop:
                raise Exception("Unable produce frame with min points")

        return

    def extractFeatures(self, latestFieldScan):
        """The purpose of this method is to return the latest lidar field scan"""

        print ("extractFeatures: empty implementation. Scan len : " + str(len(latestFieldScan)))

        #TO DO : Write logic to analyze the field scan, identify the towers within
        #        the scan, and return tower locations to caller


        return #TO DO what does your data type look like for returning tower positions?
    
    def calculatePosition(self,towerList, gyro):
        """Calculates position based on tower location (found by extractFeatures) and gyro data 
            (convert robot perspective to a global field coordinate)"""

        print ("calculatePostion: empty implementation")
        
        #TO DO : Take tower location data (returned from extractFeatures) and
        #        gyro data and produce a field coordinate location

        return {'x': 0,'y':0}


# Simple test
lidar = RPLidar('COM3')
time.sleep(5)

coordinateFinder = fieldCoordinates(lidar)

position = coordinateFinder.getCurrentPosition(0)
print ("Position : " + str(position))

lidar.stop()
lidar.stop_motor()
lidar.disconnect()
