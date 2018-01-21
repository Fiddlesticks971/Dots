import pyopencl

def openclDetection():
    print("OpenCl Detection:")
    print(pyopencl.VERSION)
    if pyopencl.VERSION == "":
        return -1
    else:
        return 0

def deviceDetection():
    print("Detecting Devices")
    
    platformList = pyopencl.get_platforms()
    if len(platformList) == 0:
        return -1
    print ("Number of Platforms: " + str(len(platformList)))
    
    deviceList = platformList[0].get_devices()
    if len(deviceList) == 0:
        return -1
    print ("Number of Devices: " + str(len(deviceList)))
    
    return 0
    
def deviceInitialization():
    print("Device Initialization")
    
def applicationInitialization():
    print("Application Initialization")
    
def updateDisplay():
    print("Update Display")

def main():
    OpenCLError = 0
    if openclDetection() == -1:
        return
    if deviceDetection() == -1:
        return
    deviceInitialization()
    applicationInitialization()
    i = 6
    while i > 0:
        updateDisplay()
        i=i-1
    
main()
