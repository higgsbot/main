# HiggsBot

HiggsBot is a Discord bot written for the Discord Hack-A-Ton. \
The bot compiles or interprets various programming languages and prints the various results in chat. \
A few safety measures have been implemented. For more information, read the [documentation](https://github.com/higgsbot/documents).

## Supported Languages

- C
- asm
- Go

## Requirements

HiggsBot must be ran in a Linux environment with the following packages preinstalled:

- gcc
- golang
- NASM
- Python 3.6+
- Pip
- Git

WSL on Windows is supported.

## Install Instructions

Ubuntu: 
```bash
sudo apt update
sudo apt install build-utils golang nasm python3.7 git -y
git clone https://github.com/higgsbot/main.git
cd main
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python3.7 get-pip.py
pip3 install $(cat requirements.txt)
```

Launch the bot using `python3.7 bot.py`.
It will automatically close back down, but create a few files.

Open `token.txt` and paste in your bot token from the Discord developer website. \
Open `owner.txt` and paste in the user IDs of the bot owners/administrators seperated by "," eg. "231312312,421412421".

The users with their IDs in that file will be able to give and take away CodeTokens from other users and themselves.

## License
[MIT](https://choosealicense.com/licenses/mit/)