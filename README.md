# RPI Discord Display

## Requirements
* Waveshare 2.7 Inch Display
* Raspberry pi (tested on 3 and 4)

## Install the packages
```sh
npm i
pip3 install fastapi Pillow
```

## Running the project
### Discord Bot Client
Create a [Discord Application](https://discord.com/developers/applications) and place the token and the discord bot's ID as arguments
```sh
node bot.js <token> <bot ID>
```

### Python Backend
```sh
cd display
./start.sh
```
