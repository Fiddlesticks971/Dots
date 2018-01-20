

def deviceDetection():
    print("Detecting Devices")
def deviceInitialization():
    print("Device Initialization")
def applicationInitialization():
    print("Application Initialization")
def updateDisplay():
    print("Update Display")

def main():    
    deviceDetection()
    deviceInitialization()
    applicationInitialization()
    i = 6
    while i > 0:
        updateDisplay()
        i=i-1
    
main()
