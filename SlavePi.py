from smbus import SMBus
import time

#bus = smbus.SMBus(1)

#Slave address for arduino is 0x04
address = 0x04
bus = SMBus(1)
time.sleep(0.1) #we need to sleep everytime for the smbus to work properly
#A short delay is needed for i2c to settle

letterMap = {
    " ": 0,
    "a": 32,
    "b": 48,
    "c": 36,
    "d": 38,
    "e": 34,
    "f": 52,
    "g": 54,
    "h": 50,
    "i": 20,
    "j": 22,
    "k": 40,
    "l": 56,
    "m": 44,
    "n": 46,
    "o": 42,
    "p": 60,
    "q": 62,
    "r": 58,
    "s": 28,
    "t": 30,
    "u": 41,
    "v": 57,
    "w": 23,
    "x": 45,
    "y": 47,
    "z": 43,
    ".": 19,
    ",": 16,
    "-": 9,
    "!": 26,
    "?": 25,
    ":": 18,
    ";": 24
}

    
def writeNumber(value):
    print(type(value))
    bus.write_byte(address,value)
    time.sleep(0.1)
    
    return -1

def readNumber():
    number = bus.read_byte(address)
    time.sleep(0.1)
    return number

def mapText(text):
    return letterMap[text.lower()]


def sendText(text):
    numberToSend = mapText(text)
    print("working here")
    writeNumber(numberToSend)
    print("RPI: ", text)
    print("Arduino: ", letterMap[readNumber()])
    
