from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import textwrap
import epd2in7

app = FastAPI()

epd = epd2in7.EPD()
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
    smallFont = ImageFont.truetype('/usr/share/fonts/truetype/freefont/FreeSansBold.ttf', 20)
    largeFont = ImageFont.truetype('/usr/share/fonts/truetype/freefont/FreeSansBold.ttf', 27)
    draw.rectangle((0, 0, 264, 40), fill = 0)
    draw.text((10, 10), f'{author} said:', font = smallFont, fill = 255)
    offset = 0
    for line in textwrap.wrap(text, width=15):
        draw.text((10, 50+offset), line, font = largeFont, fill = 0)
        offset += largeFont.getsize(line)[1]

    image = image.transpose(Image.ROTATE_90)
    epd.display_frame(epd.get_frame_buffer(image))
    
@app.get("/picture")
async def picture():
  image = Image.open('in.jpg')
  image = image.resize((264, 176))
  image = image.transpose(Image.ROTATE_90)
  epd.display_frame(epd.get_frame_buffer(image))