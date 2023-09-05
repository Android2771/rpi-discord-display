FROM node:alpine

WORKDIR /bot

COPY . .
COPY package.json .
COPY package-lock.json .
COPY tsconfig.json .

RUN apt update -y
RUN npm install
RUN npm install typescript -g
RUN tsc

CMD ["node", "/bot/bot.js"]
