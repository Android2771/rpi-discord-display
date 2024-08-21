from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from gpiozero import Button
import textwrap
import requests
import epaper

btn1 = Button(5)
btn2 = Button(6)
btn3 = Button(13)
btn4 = Button(19)

app = FastAPI()

f = open("resources/waveshare.txt", "r") 
selected_version = [line[2:] for line in f if line.startswith("- ")][0].strip()
  
epd = epaper.epaper(selected_version).EPD()
epd.init()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/draw")
async def draw(author, text):
    image = Image.new('1', (264, 176), 255)
    draw = ImageDraw.Draw(image)
    smallFont = ImageFont.truetype('./resources/FreeSansBold.ttf', 20)
    largeFont = ImageFont.truetype('./resources/FreeSansBold.ttf', 27)
    draw.rectangle((0, 0, 264, 40), fill = 0)
    draw.text((10, 10), f'{author} said:', font = smallFont, fill = 255)
    offset = 0
    for line in textwrap.wrap(text, width=15):
        draw.text((10, 50+offset), line, font = largeFont, fill = 0)
        offset += largeFont.getsize(line)[1]

    image = image.transpose(Image.ROTATE_90)
    image.save('./resources/out.png')
    epd.display(epd.getbuffer(image))
    return 'OK'
    
@app.get("/picture")
async def picture():
  image = Image.open('./resources/in.jpg')
  image = image.resize((264, 176))
  image = image.transpose(Image.ROTATE_90)
  epd.display(epd.getbuffer(image))
  return 'OK'

def clear(btn):
  image = Image.new('1', (176, 264), 255)
  epd.display(epd.getbuffer(image))
  return 'OK'
    
def toggle_picture(btn):
  requests.get('http://localhost:7000/picture')
  return 'OK'

btn1.when_pressed = clear
btn2.when_pressed = toggle_picture
