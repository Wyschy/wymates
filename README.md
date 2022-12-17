# wymates

A libary to use Breadboard Mates with micropython

Description:

To use wymates create an object with the class wy_mates and the following attributes:

Comport = Number of serial port
txPin = TX-Pin of Comport
rxPin = RX-Pin of Comport
resetPin = Pin for Hardware-Reset (99 if no Hardware Reset)

Example:

    import wymates
    mate = wymates.wy_mates(0,0,1,2)

create a object named "mate" with comport = 0, tx-Pin = GPIO 0, rx-Pin = GPIO 1, ResetPin = GPIO 2

Alternative:
    #import wymates
    #mate = wymates.wy_mates(0,0,1,99)

create a object "mate" with no Hardware Reset.

