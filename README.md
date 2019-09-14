# XRP Messenger

XRP Messenger is a Python 3 library for getting the current BUY value of XRP from Altcoin Trader(South African cryptocurrency exchange). It checks the value against your limit that you set and sending you a Telegram message if the BUY value of XRP is equal or greater than your limit. 

NB!! You MUST create a Telegram Bot before using this program.

## Installation

1. Install dependencies easily by cd-ing to this folder in terminal and running the following commands:
	
pip3 install -r requirements.txt

and

sudo apt install figlet toilet


2. In Ubuntu do the following to run an executable text file when double-clicked:

Open the File Manager.

Click on the "hamburger" symbol on the top right of the window, left of the "Minimize" symbol. A menu will drop down.

Click "Preferences". A tabbed dialog box will be displayed.

Select the "Behavior" tab.

Choose your preferred behavior for "executable text files" aka scripts.


## Usage

1. Create a Telegram Bot. Many tutorials can be found online. It takes only a couple of minutes to do.

2. Open mercury.py in your favourite IDE or text editor and edit the following lines:

line 45   xrpval = 5.0 # enter your limit in ZAR without the "R". R5.00 in this example.

line 67	  api_key = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'# Delete "x"'s and enter your Telegram API key
line 68   bot_chatID = 'xxxxxxxxx'  #Delete "x"'s and enter your bot_chat ID 

3. Double-click start.sh to run the program.


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
