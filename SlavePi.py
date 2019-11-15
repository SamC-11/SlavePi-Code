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
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4,
    "e": 5,
    "f": 6,
    "g": 7,
    "h": 8,
    "i": 9,
    "j": 10,
    "k": 11,
    "l": 12,
    "m": 13,
    "n": 14,
    "o": 15,
    "p": 16,
    "q": 17,
    "r": 18,
    "s": 19,
    "t": 20,
    "u": 21,
    "v": 22,
    "w": 23,
    "x": 24,
    "y": 25,
    "z": 26,
    ".": 27,
    ",": 28,
    "'": 29,
    "-": 30,
    "/": 31,
    "!": 32,
    "?": 33,
    "$": 34,
    ":": 35,
    "(": 36,
    ")": 37,
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
    print("RPI: ", numberToSend)
    print("Arduino: ", readNumber())