'''
This module checks if you are connected to the Altcoin Trader. 
Starts Mercury module if successfully connected.

Author: Michiel Odendaal
Date last modified: 12 Aug 2019
email: mikescryptot@gmail.com
'''

import requests
import urllib
import mercury

def checkNetwork():
      
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
            
            print('\n Success! You are connected to: ', url)
            print('\n Starting mercury Messenger module ... \n')
            mercury.messenger()
        else:
            print(status)
    except:
        print('\n An error occured. Check your network settings.', status)

    
    
