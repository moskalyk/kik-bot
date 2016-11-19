#Deloitte Digital Gif Bot

##1. Python Installation

You can download [Python 3.5.2 by going to the following Link](https://www.python.org/downloads/)
Once python is installed, open up your Terminal (Mac) or Command Prompt (Windows) and type the following command to confirm that it is installed (command are always without the $ sign!).

```
$ python3 --version

Python 3.5.2
```

##2. Virtual Env Installation
```
$ pip3 install --upgrade virtualenv

Collecting virtualenv
  Downloading virtualenv-15.1.0-py2.py3-none-any.whl (1.8MB)
    100% |████████████████████████████████| 1.8MB 389kB/s
```

##3. Kik Developer Authorization

1. Download Kik on your mobile phone.
2. Go to the [developer portal](https://dev.kik.com/#/login) to login
3. Scan the QR code
4. You'll then get asked by the Botsworth if you want to login on your phone, select 'Yes'
5. Choose a new username by telling Botsworth what you want it to be
5. Then go to the [configuration](https://dev.kik.com/#/engine/5702738761744384) tab to generate an API key, and keep that for later fun ;)

##4. Ngrok Installation

##Mac users

If you're a sexy Mac user, then I would highly suggest installing [brew](http://brew.sh/). This can be done by performing the following command (yes you'll be asked for your passwored 5-8 times, this is normal):
```
$ /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```
Then, to just install ngrok, do a little:
```
$ brew install ngrok
```
Finally, go to the ngrok website and create an account and follow their instructions to set your lcoal configurations.


##Windows Users
Download directly from the [ngrok website.](https://ngrok.com/download) and follow their instructions to set your local configurations.