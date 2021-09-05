<h2 align="centre">VIDEO STREAM BOT</h2>

telegram bot project for streaming video on telegram video chat, powered by [tgcalls](https://github.com/MarshalX/tgcalls) and [pyrogram](https://github.com/pyrogram/pyrogram)

<p align="center"><a href="https://t.me/JawaraStreamBot"><img src="https://telegra.ph/file/4e8717d59d74412cf0e50.jpg" width="300"></a></p>
<p align="center">

## 🛠 Commands:
- /vstream (reply to video) - to start video streaming
- /vstop - to stop video streaming
- /song (song name) - to download song
- /vsong (video name) - to download video

📝 Note: From now, /vstream & /vstop command can only be used by group admins.

## 🧪 Get STRING_SESSION from below:

TAP THIS: [![GenerateString](https://img.shields.io/badge/repl.it-generateString-yellowgreen)](https://replit.com/@levinalab/StringSession#main.py)

## Heroku Deployment 💜
The easy way to host this bot, deploy to Heroku

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/IzzyLord/video-stream)

## VPS Deployment
```sh
- sudo apt update && upgrade -y
- sudo apt install python3-pip -y virtualenv
- sudo apt install ffmpeg -y
- git clone https://github.com/IzzyLord/video-stream
- cd video-stream
- virtualenv venv #Create Virtual Environment.
- source venv/bin/activate #Activate Virtual Environment
- pip3 install --upgrade pip
- pip3 install -U -r requirements.txt
- cp -r sample.env local.env
- nano local.env #Fill it with your variables value.
- python3 -m bot
```

