'''
This module collects the Buy Value of XRP from Altcoin Trader. 
It compares the limit you have set to the fetched data.

If necessary it will send you a notification of the Buy Price.

Author: Michiel Odendaal
Date last modified: 12 Aug 2019
email: mikescryptot@gmail.com
'''

import os
import telegram_send
import requests
import urllib
from bs4 import BeautifulSoup as bs
import re
import time
import datetime

def messenger():
    while KeyboardInterrupt != True:
        
        os.system("clear")
        print('\n Mercury successfully started...\n')
        
        # Enter the desired value into xrpval (ZAR without the R)
        xrpval = 5.0
        # The URL to Altcoin Trader XRP page
        url = 'https://www.altcointrader.co.za/xrp'
        
        #Headers to be sent to the site  and get the contets of the page
        headers = {
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'} 
        data = urllib.parse.urlencode(headers)
        data = data.encode('ascii')
        url_req = requests.get(url, data)
        html = url_req.content
        
        #Asking BeaurifulSoup to parse the data and find only the "Buy" value, converting it to text so that we can retrieve and read it.
        soup = bs(html, features='lxml')
        xrp_valBuy = soup.find("td", {"class": 'orderUdBPr'})
        buy_results = str(xrp_valBuy.text)
        
        #Convert the STR into FLOAT so that we can compare values
        buy_value = float(buy_results)
        
        try:
            if buy_value >= 5.00:
            
                print('\n Attempting to send message... \n  ')
                # Send your Bot API key and Bot chat ID together with the Buy Value to Telegram       
                api_key = '675170124:AAGU4a7PctTiyxiRHvaHvEcZkFWcWQE7Kj8'
                bot_chatID = '950175748'
                send_text = 'https://api.telegram.org/bot' + api_key + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + buy_results
                
                #Checking to see if the message has been delivered.
                response = requests.get(send_text)
                
                if response == 200:
                    print('\n Message delivered! Check your Telegram!')
                    
                else:
                    print('Could not send message!')
                    break
                
            else:
                print('\n Time now: ', datetime.datetime.now())
                print('\n Value now: ','R',buy_value, ' Below', ' R',xrpval, ' Not sending a message.')
        except:
            print('Could either not connect to the site or retrieve the data!')
            break
        
        print('\n Checking again in 10 minutes...')
        #wait for 600 seconds then start again
        time.sleep(600)
        
        print ('\n Checking now ...')


    
    
