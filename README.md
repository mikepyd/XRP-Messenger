# XRP Messenger

XRP Messenger is a Linux Python 3 library for getting the current BUY value of XRP from Altcoin Trader(South African cryptocurrency exchange). It checks the value against your limit that you set and sending you a Telegram message if the BUY value of XRP is equal or greater than your limit. 

## Getting Started

1. Create a Telegram Bot. Many tutorials can be found online. It takes only a couple of minutes to do.<br />
2. Open mercury.py in your favourite IDE or text editor and edit the following lines:<br />

2.1. line 42   xrpval = 5.0 # enter your limit in ZAR without the "R". R5.00 in this example.<br />

2.2. line 68	  api_key = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'# Delete "x"'s and enter your Telegram API key<br />
2.3. line 69   bot_chatID = 'xxxxxxxxx'  #Delete "x"'s and enter your bot_chat ID<br />

3. Double-click start.sh to run the program.

### Prerequisites
1. [Telegram Desktop](https://itsfoss.com/install-telegram-desktop-linux/)<br />
2. [Python 3](https://www.python.org/downloads/release/python-373/)<br />
2. [pip3](https://linuxize.com/post/how-to-install-pip-on-ubuntu-18.04/) <br />

### Installing

1. Extract the folder to where you want it.
2. In Terminal cd to this folder and run: sudo apt install figlet toilet
3. Still in Terminal: pip3 install -r requirements.txt
4. In Ubuntu do the following to run an executable text file when double-clicked:

4.1. Open the File Manager.<br />
4.2. Click on the "hamburger" symbol on the top right of the window, left of the "Minimize" symbol. A menu will drop down.<br />
4.3. Click "Preferences". A tabbed dialog box will be displayed.<br />
4.4. Select the "Behavior" tab.<br />
4.5. Choose your preferred behavior for "executable text files" aka scripts.<br />

5. Create a Telegram bot.

## Built With
* [Ubuntu 19.04](http://releases.ubuntu.com/19.04/) - Operating System
* [Python](https://www.python.org/downloads/release/python-373/) - The programming language used
* [VS Code](https://code.visualstudio.com/) - IDE

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.<br />
Please make sure to update tests as appropriate.

## Versioning

1.0 

## Authors

* **Michiel Odendaal** - *Initial work* - [mikepyd](https://github.com/mikepyd)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* [Rahiel Kasim](https://pypi.org/project/telegram-send/) - telegram-send
* [Rick van Hattem](https://pypi.org/project/progressbar2/) - progressbar2
