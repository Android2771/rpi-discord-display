# RPI Discord Display
<img src="readmepic.png">

## Requirements
* Compatible Waveshare Screens
* Raspberry Pi (tested on 3B and 4)

## Running the project
### Preliminary Steps
#### Discord Bot
Create a [Discord Application](https://discord.com/developers/applications) and place the token and the discord bot's ID inside a `token.txt` file in the `resources` directory
```sh
mkdir -p bot/resources
echo <token> > bot/resources/token.txt
```

#### Waveshare Version
Head to `display/resources/waveshare.txt` and select your model by prepending the line with a dash and a space `- `. 

Currently, `epd2in7` is selected by default for a Waveshare 2.7 inch display. Note that you need to remove the dash from epd2in7 to change versions.

### Running using docker
To install docker:
```
curl -fsSL https://get.docker.com -o get-docker.sh
chmod +x get-docker.sh
sudo ./get-docker.sh
rm get-docker.sh
```

To build and run the bot with the display:
```
sudo docker compose up -d --build
```

## Using the project
### Text
Head to a discord chat in which you added the bot and type `draw <text>` to show the text on the display

### Image
Type in `image` on a chat and attach a single image in the same message to have it displayed on the display

## Troubleshooting
If the display isn't working, make sure that you selected the right version on `display/resources/waveshare.txt`. If it matches your model, note that each model has multiple versions which are worth trying to make it work. For example, the Waveshare 2.7 inch display has `epd2in7`, `epd2in7b`, `epd2in7b_V2` to try from.
