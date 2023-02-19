# Wymates is a libary to use BreadBoard Mates with Micropython

# Thomas Wyschkony

# February 2023
# Version 1.0



from machine import UART
from machine import Pin
from time import sleep

class wy_mates():

    def __init__(self, com, txp, rxp, resetp):
        self.com = com
        self.txp   = txp
        self.rxp   = rxp
        self.resetp = resetp
        self.page = 0
        
    def begin(self):
        if self.resetp!=99:
            port = UART(self.com, baudrate=9600, tx=Pin(self.txp), rx=Pin(self.rxp))
            resetpin=Pin(self.resetp,Pin.OUT)
            resetpin.value(0)
            sleep(0.5)
            resetpin.value(1)
            print("wait for reset")
            sleep(5)
            while port.any():
                return(port.read())
        else:
            command=(b'\x24\x00\x09')
            return(self.senduart(command))

    def senduart(self,command):
        port = UART(self.com, baudrate=9600, tx=Pin(self.txp), rx=Pin(self.rxp))
        port.write(command)
        sleep(0.5)
        while port.any():
            return(port.read())
        
    def sendfast(self,command):
        port = UART(self.com, baudrate=9600, tx=Pin(self.txp), rx=Pin(self.rxp))
        port.write(command)
        sleep(0.1)
        while port.any():
            return(port.read())
        
    def setpage(self,x):
        x=(x).to_bytes(2,'big')
        command=(b'\x24\x00\x00')+x
        return(self.senduart(command))
    
    def setLedDigits(self,idx,x):
        x=(x).to_bytes(2,'big')
        idx=(idx).to_bytes(1,'big')
        command=(b'\x24\x00\x02\x05')+idx+x
        return(self.senduart(command))
        
    def setMediaGaugeA(self,idx,x):
        x=(x).to_bytes(2,'big')
        idx=(idx).to_bytes(1,'big')
        command=(b'\x24\x00\x02\x46')+idx+x
        return(self.senduart(command))
        
    def setMediaGaugeB(self,idx,x):
        x=(x).to_bytes(2,'big')
        idx=(idx).to_bytes(1,'big')
        command=(b'\x24\x00\x02\x47')+idx+x
        return(self.senduart(command))    

    def setMediaGaugeC(self,idx,x):
        x=(x).to_bytes(2,'big')
        idx=(idx).to_bytes(1,'big')
        command=(b'\x24\x00\x02\x48')+idx+x
        return(self.senduart(command))
    
    def setMediaGaugeD(self,idx,x):
        x=(x).to_bytes(2,'big')
        idx=(idx).to_bytes(1,'big')
        command=(b'\x24\x00\x02\x49')+idx+x
        return(self.senduart(command))
    
    def setMediaThermometer(self,idx,x):
        x=(x).to_bytes(2,'big')
        idx=(idx).to_bytes(1,'big')
        command=(b'\x24\x00\x02\x4A')+idx+x
        return(self.senduart(command))
    
    def setScope(self,idx,x,max):
        max=int(max/2)
        if x > max:
            x = max
        elif x < -max:
            x = -max
        x=(x+max).to_bytes(2,'big')
        idx=(idx).to_bytes(1,'big')
        command=(b'\x24\x00\x02\x4D')+idx+x
        self.sendfast(command)

    def setTextArea(self,idx,x):
        idx=(idx).to_bytes(2,'big')
        command=(b'\x24\xFF\xFF')+idx+x+(b'\0x00')
        return(self.senduart(command))

    def clearPrintArea(self,idx):
        idx=(idx).to_bytes(2,'big')
        command=(b'\x24\x00\x07')+idx
        return(self.senduart(command))

    def setPrintArea(self,idx,x):
        idx=(idx).to_bytes(2,'big')
        x=(x).to_bytes(2,'big')
        command=(b'\x24\xFF\xFE')+idx+x+(b'\0x00')
        return(self.senduart(command))


    def setMediaLed(self,led,x):
        led=(led).to_bytes(1,'big')
        x=(x).to_bytes(2,'big')
        command=(b'\x24\x00\x02\x40')+led+x
        return(self.senduart(command))
    
    def setLed(self,led,x):
        led=(led).to_bytes(1,'big')
        x=(x).to_bytes(2,'big')
        command=(b'\x24\x00\x02\x00')+led+x
        return(self.senduart(command))
        
    def getpage(self):
        port = UART(self.com, baudrate=9600, tx=Pin(self.txp), rx=Pin(self.rxp))
        command=(b'\x24\x00\x01')
        port.write(command)
        sleep(0.5)
        while port.any():
            x,y,z=port.read()
            return(z)
        
    def checkpages(self,show):
        active = self.getpage()
        print("please wait until i check the numbers of pages")
        check = True
        page = 0
        while check:
            self.setpage(page)
            if self.getpage() != page:
                check = False
            else:
                page += 1
            sleep(show)
        self.setpage(active)
        return(page-1)

    def setBacklight(self,x):
        if x > 15:
            x = 15            
        x=(x).to_bytes(2,'big')
        command=(b'\x24\x00\x06')+x
        return(self.senduart(command))