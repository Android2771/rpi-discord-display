FROM node:lts

WORKDIR /bot

COPY . .
COPY package.json .
COPY package-lock.json .
COPY tsconfig.json .

RUN npm i
RUN npm i typescript -g
RUN tsc

CMD ["node", "/bot/bot.js"]
