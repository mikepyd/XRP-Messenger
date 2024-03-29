# XRP Messenger

XRP Messenger is a Linux Python 3 library for getting the current BUY value of XRP from Altcoin Trader(South African cryptocurrency exchange). It checks the value against your limit that you set and sending you a Telegram message if the BUY value of XRP is equal or greater than your limit. 

## Getting Started

* Create a Telegram Bot. <br />
* Open mercury.py in your favourite IDE or text editor and edit the following lines:<br />

  * line 42   xrpval = 5.0 # enter your limit in ZAR without the "R". R5.00 in this example.<br />

  * line 68	  api_key = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'# Delete "x"'s and enter your Telegram API key<br />
  * line 69   bot_chatID = 'xxxxxxxxx'  #Delete "x"'s and enter your bot_chat ID<br />

* Double-click start.sh to run the program.

### Prerequisites
* [Telegram Desktop](https://itsfoss.com/install-telegram-desktop-linux/)<br />
* A [Telegram Bot](https://core.telegram.org/bots)<br />
* [Python 3](https://www.python.org/downloads/release/python-373/)<br />
* [pip3](https://linuxize.com/post/how-to-install-pip-on-ubuntu-18.04/) <br />

### Installing

* Extract the folder to where you want it.
* In Terminal cd to this extracted folder and run: "sudo apt install figlet toilet"
* Still in Terminal: "pip3 install -r requirements.txt". Close Terminal when completed.
* In Ubuntu do the following to run an executable text file when double-clicked:

  * Open the extracted folder in File Manager.<br />
  * Click on the "hamburger" symbol on the top right of the window, left of the "Minimize" symbol. A menu will drop down.<br />
  * Click "Preferences". A tabbed dialog box will be displayed.<br />
  * Select the "Behavior" tab.<br />
  * Choose "Double click" from "Open Action" and "Run them" for Executable Text Files".Close File Manager.<br />
* That's it! Now double-click "start.sh" to start the program.

## Built With
* [Ubuntu 19.04](http://releases.ubuntu.com/19.04/) - Operating System
* [Python](https://www.python.org/downloads/release/python-373/) - The programming language used
* [VS Code](https://code.visualstudio.com/) - IDE

## Contributing

* Pull requests are welcome.<br /> 
* For major changes, please open an issue first to discuss what you would like to change.<br />

## Versioning

1.0 

## Authors

* **Michiel Odendaal** - *Initial work* - [mikepyd](https://github.com/mikepyd)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* [Rahiel Kasim](https://pypi.org/project/telegram-send/) - telegram-send
* [Rick van Hattem](https://pypi.org/project/progressbar2/) - progressbar2
