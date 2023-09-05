FROM balenalib/rpi-raspbian

WORKDIR /display

COPY display.py .

RUN apt update -y
RUN apt install python3 python3-pip libjpeg-dev zlib1g-dev libfreetype6-dev libopenjp2-7 libtinfo5 libtiff5 libxcb1 -y
RUN pip3 install fastapi uvicorn[standard] gpiozero spidev RPi.GPIO requests waveshare-epaper
RUN pip3 install -U Pillow==8.1.2

CMD ["python3", "-m", "uvicorn", "display:app", "--host", "0.0.0.0", "--port", "7000"]
