'''
This module checks if you are connected to the Altcoin Trader. 
Starts Mercury module if successfully connected.

Author: Michiel Odendaal
Date last modified: 9 Sep 2019
email: mikepydev@gmail.com
'''

import os
import requests
import urllib
from urllib import *
import mercury
import time

def checkNetwork():

    connection_timeout = 30
    start_time = time.time()
      
    print('\n Network Checker successfully started...')
        
    try:
        
        # The URL to Altcoin Trader XRP page
        url = 'https://www.altcointrader.co.za/xrp'
            
        #Headers to be sent to the site  and get the contets of the page
        headers = {
                    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'} 
        data = urllib.parse.urlencode(headers)
        data = data.encode('ascii')
        print('\n Checking if you are connected to ', url)
        url_req = requests.get(url, data)
        status = url_req.status_code
                
        if status == 200:            
            os.system("clear")
            print('\n Success! You are connected to: ', url)
            print('\n Starting mercury Messenger module ... \n')
            time.sleep(2) 
            mercury.messenger()            
        else:
            print(status)
            
    except ConnectionError:
        if time.time() > start_time + connection_timeout:
            raise Exception('Unable to get updates after {} seconds of ConnectionErrors'.format(connection_timeout))
        else:
            time.sleep(1)
