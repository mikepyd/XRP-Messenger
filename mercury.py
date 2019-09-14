'''
Called from netCheck.py

This module collects the Buy Value of XRP from Altcoin Trader. 
It compares the limit you have set to the fetched data.

It will send you a notification of the current Buy Price if the current value is equal to 
or greater than your specified price. Otherwise it will loop until the Buy value is equal to or greater than your specified value or if you
press "Ctrl+C" to quit.

Author: Michiel Odendaal
Date last modified: 9 Sep 2019
email: mikepydev@gmail.com
'''
from requests import ConnectionError
import os
import telegram_send
import requests
import urllib
from bs4 import BeautifulSoup as bs
import re
import time
import datetime
import json
 
def messenger():
    try:
        while True:

            connection_timeout = 30
            start_time = time.time()
                
            os.system("clear")
            print('\n Network Check completed successfully...Starting Mercury')
            time.sleep(3)
            os.system("clear")
            print('\n Mercury successfully started...\n')
            time.sleep(2)
            os.system("clear")
            print('Mercury Running... Press "Ctrl + C" to quit...')
            
            # Enter the desired value into xrpval (ZAR without the R)
            xrpval = 4.00
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
                if buy_value >= xrpval:
                
                    print('\n Attempting to send message... \n  ')
                    # Send your Bot API key and Bot chat ID together with the Buy Value to Telegram       
                    api_key = 'xxxxxxxxxxxxxxxxxxxxxx'
                    bot_chatID = 'xxxxxxxxxxx'
                    send_text = 'https://api.telegram.org/bot' + api_key + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + buy_results
                    
                    #Checking to see if the message has been delivered.
                    response = requests.get(send_text)
                    code = response.status_code
                    #response = json.loads(response.content)
                    
                    if code == 200:
                        os.system("clear")
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
            '''           
            def countdown(t):
                while t:
                    
                    
                    mins, secs = divmod(t, 60)
                    timeformat = '{:02d}:{:02d}'.format(mins, secs)
                    print(timeformat, end='\r')
                    time.sleep(1)
                    t -= 1

            countdown(600)
            '''
            import progressbar

            for i in progressbar.progressbar(range(600), redirect_stdout=True):
                print('Seconds until checking again', i, end ='\r')
                time.sleep(1)
           
            

    except KeyboardInterrupt:
        os.system("clear")
        print(" GoodBye!")
    
    except ConnectionError:
        if time.time() > start_time + connection_timeout:
            raise Exception('Unable to get updates after {} seconds of ConnectionErrors'.format(connection_timeout))
        else:
            time.sleep(1)
