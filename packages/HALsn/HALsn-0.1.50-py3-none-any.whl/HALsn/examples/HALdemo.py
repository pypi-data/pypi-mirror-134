#! /usr/bin/env python3

'''

HEY EVERYONE! THIS IS A QUICK DEMO TO SHOWCASE THE CAPABILITIES WE HAVE 
WITH BDP AND HAL ABSTRACTION. THIS CODE WILL BE SHARED WITH THE GROUP
AFTER THIS MEETING. IF YOU WANT TO PLAY AROUND WITH THE TOOLS I'LL HAVE
A CFP SET UP AT MY DESK AND YOU CAN COME GET FAMILIAR WITH CONTROLLING IT
USING THIS API.

'''

import time
import sys
sys.path.insert(1, '/home/pi/HALsn/HALsn/maps')
sys.path.insert(1, '/home/pi/HALsn/HALsn')
from SKU import CFP             # import the CFP SKU into the code
from scheduler import Routine   # import the Routine utility to schedule tasks 

cfp = CFP()                     # declare the CFP
cfp.open_port()                 # open the serial port, default is closed
cfp.command('debug_off')        # put the CFP in debug off so it will accept commands

rout = Routine()                # declare a routine

def bfnc(*args):
    '''
    This is the BREAK function for the routine.
    a routine must have a BREAK function but it
    does not require STANDARD functions. As long
    as your BREAK function returns True it can do
    whatever other tasks are required as well.
    '''

    print(rout.ext_timer())     # print the Routines current time

    data = cfp.master_query()   # collect all master_query() enabled queries

    print(rout.ext_timer())

    print(data)                 # print the data

    if data[0] == '$LT0\r':     # if the first index (current brew) is equivalent
                                # to '$LT0\r', the command for idle, then break
        return True             # the loop by returning True

rout.add_break_functions(bfnc, None) # Add break function to the routine

time.sleep(0.25)
cfp.command('6_oz_classic_K')        # Start the brew with an external command
time.sleep(0.25)
cfp.command('debug_on')              # Enable debug mode to collect all avilable data
time.sleep(0.25)

try:                        
    rout.run()                       # Start the routine. Runs unitl break condition is met
except KeyboardInterrupt:               
    cfp.command('debug_off')         # If ctrl+c is pressed, the loop will break and the
    cfp.command('cancel_brew')       # machine will turn off