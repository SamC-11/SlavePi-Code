from smbus import SMBus
import time

#bus = smbus.SMBus(1)

#Slave address for arduino is 0x04
address = 0x04
bus = SMBus(1)
time.sleep(0.1) #we need to sleep everytime for the smbus to work properly
#A short delay is needed for i2c to settle

    
def writeNumber(value):
    bus.write_byte(address,value)
    time.sleep(0.1)
    
    return -1

def readNumber():
    number = bus.read_byte(address)
    time.sleep(0.1)
    return number
                        

while True:
    var = input("Which servo would you like to control?: ");
    print(type(var))
    writeNumber(int(var)-1)
    print("RPI: ", var)
    print("Arduino: ", readNumber())
