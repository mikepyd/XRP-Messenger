'''
This module calls networkchecker.py and starts the process of getting the buy data of XRP 
from Altcoin Trader.

Author: Michiel Odendaal
Date last modified: 12 Aug 2019
email: mikescryptot@gmail.com
'''

import sys
import os
import netCheck

def main():
    os.system("clear") # Clear the screen
    netCheck.checkNetwork() # Start netCheck module
main()











