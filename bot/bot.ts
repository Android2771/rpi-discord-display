import { REST, Routes, Client, GatewayIntentBits, Partials, ButtonBuilder, ButtonStyle, ActionRowBuilder, ButtonInteraction, ChatInputCommandInteraction, Interaction } from 'discord.js';
import https from 'https';
import fs from 'fs'
import { fileURLToPath } from 'url';
import { dirname } from 'path';

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);
const token = fs.readFileSync(`${__dirname}/resources/token.txt`, 'utf8').replace(/(\r\n|\n|\r)/gm, "");
const botId = atob(token.split('.')[0])

const client = new Client(
    {
        intents: [GatewayIntentBits.DirectMessages,
        GatewayIntentBits.Guilds,
        GatewayIntentBits.GuildMessages,
        GatewayIntentBits.MessageContent,
        GatewayIntentBits.GuildMembers,
        GatewayIntentBits.DirectMessageReactions,
        GatewayIntentBits.GuildMessageReactions,
        GatewayIntentBits.GuildPresences
        ], partials: [Partials.Channel]
    })

client.login(token);

client.on("messageCreate", async (message: any) => {
    if (message.content.startsWith("draw ")) {
        const text = message.content.substring(5)
        const name = message.author.username
        message.react("⏱️")
        fetch(`http://display:7000/draw?author=${name}&text=${text}`)
            .then(() => {
                const botReactions = message.reactions.cache.filter((reaction: any) => reaction.users.cache.has(botId));
                for (const reaction of botReactions.values())
                    reaction.users.remove(botId);
                message.react("✏️");
            }).catch((err) => {
                console.error(err)
                message.react("❌");
            });
    } else if (message.attachments.size === 1) {
        message.attachments.forEach((item: any) => {
            const url = item.url.split('?')[0];
            if (url.endsWith("jpg") || url.endsWith("jpeg") || url.endsWith("png")) {
                message.react("⏱️")
                const file = fs.createWriteStream('/display/resources/in.jpg');
                https.get(item.url,  (response : any) => {
                    response.pipe(file);
                    file.on('finish', function () {
                        file.close(() => {
                            fetch('http://display:7000/picture').then(() => {
                                const botReactions = message.reactions.cache.filter((reaction: any) => reaction.users.cache.has(botId));
                                for (const reaction of botReactions.values())
                                    reaction.users.remove(botId);
                                message.react("✏️");
                            }).catch(() => {
                                const botReactions = message.reactions.cache.filter((reaction: any) => reaction.users.cache.has(botId));
                                for (const reaction of botReactions.values())
                                    reaction.users.remove(botId);
                                message.react("❌");
                            });
                        });
                    });
                })
            } else {
                message.react("❌")
            }
        });
    }
})
