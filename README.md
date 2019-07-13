# HiggsBot

HiggsBot is a Discord bot written for the Discord Hack-A-Ton. \
The bot compiles or interprets various programming languages and prints the various results in chat. \
A few safety measures have been implemented. For more information, read the [documentation](https://github.com/higgsbot/documents).

## Supported Languages

- C
- C++

## Requirements

HiggsBot must be ran in a Linux environment with the following packages preinstalled:

- gcc
- g++
- Python 3.6+
- Pip
- Git

WSL on Windows is supported.

## Install Instructions

Ubuntu: 
```bash
sudo apt update
sudo apt install build-essentials nasm python3.7 git -y
git clone --recurse-submodules https://github.com/higgsbot/main.git
cd main
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python3.7 get-pip.py
```

Launch the bot using `python3.7 bot.py`.
You will be prompted to input some data.

First paste in your bot token from the Discord developer website. \
After that paste in the user IDs of the bot owners/administrators seperated by "," eg. "231312312,421412421".

The users with their IDs in that file will be able to give and take away CodeTokens from other users and themselves.

Now go to the maintenance menu by typing `2` and pressing enter, and type `2` again to install the bot requirements.

Unless you want to enter your sudo password in to the console each time sudo times out, you will have to allow the bot to run sudo commands without password. Follow [this SO](https://askubuntu.com/questions/147241/execute-sudo-without-password/147265#147265) to accomplish that.

## Credits
- [@1byte2bytes](https://github.com/1byte2bytes) aka Sydney: All the magic that compiles and runs the code, and the libcontainer library.
- [@IOIIIO](https://github.com/IOIIIO) aka NoOne: launcher, libcurrency, and the cogs for use with the main bot.
- [@zackerthescar](https://github.com/zackerthescar): Parts of the bot and QC.

## License
[MIT](https://choosealicense.com/licenses/mit/)