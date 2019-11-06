from smbus import SMBus
import time

#bus = smbus.SMBus(1)

#Slave address for arduino is 0x04
address = 0x04
bus = SMBus(1)


def writeNumber(value):
    bus.write_byte(address,value)
    return -1

def readNumber():
    number = bus.read_byte(address)
    return number

while True:
    var = input("Enter 1-9: ")
    if not var:
        continue
    
    writeNumber(int(var))
    print("RPI: Hi Arduino, I sent you ", var)
    time.sleep(1)
    
    number = readNumber()
    print("Arduino: Hey RPI, I received a digit ", number)