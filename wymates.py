#Types:

#0x30 = GaugeA
#0x40 = MediaLED
#0x41 = MediaColorLED
#0x46 = MediagaugeA
#0x47 = MediagaugeB
#0x48 = MediagaugeC
#0x49 = MediagaugeD
#0x4A = Mediathermometer
#0x4D = Scope
#0x4F = RotaryGauge
#0x05 = LED Digits



from machine import UART
from machine import Pin
from time import sleep

class wy_mates():
    """ Instanz erstellen mit Com-Port, tx-Pin, rx-Pin und Resetpin
    Pico Com0: com=0, tx-Pin=0, rx-Pin=1"""

    def __init__(self, com, txp, rxp, resetp):
        self.com = com
        self.txp   = txp
        self.rxp   = rxp
        self.resetp = resetp
        self.page = 0
        
    def begin(self):
        port = UART(self.com, baudrate=9600, tx=Pin(self.txp), rx=Pin(self.rxp))
        resetpin=Pin(self.resetp,Pin.OUT)
        resetpin.value(0)
        sleep(0.5)
        resetpin.value(1)
        print("wait for reset")
        sleep(5)
        while port.any():
            return(port.read())

    def senduart(self,command):
        port = UART(self.com, baudrate=9600, tx=Pin(self.txp), rx=Pin(self.rxp))
        port.write(command)
        print("Gesendet: ",command)
        sleep(0.5)
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

    def setTextArea(self,idx,x):
        idx=(idx).to_bytes(2,'big')
        command=(b'\x24\xFF\xFF')+idx+x
        return(self.senduart(command))



    def setMediaLed(self,led,x):
    #[ SetWidgetValue: Set MediaLed0 (0x4000) value to 1 ]
    #24 00 02 40 00 00 01
        led=(led).to_bytes(1,'big')
        x=(x).to_bytes(2,'big')
        command=(b'\x24\x00\x02\x40')+led+x
        return(self.senduart(command))




        
        
    #def getpage(self):
        #port = UART(self.com, baudrate=9600, tx=Pin(self.txp), rx=Pin(self.rxp))
        #command=(b'\x24\x00\x01')
        #port.write(command)
        #print("Gesendet: ",command)
        #sleep(0.5)
        #while port.any():
            #x=port.read()
            #x=int.from_bytes(port.read(),'big')
            #print(x)
            #sleep(0.5)
