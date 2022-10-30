import os
import time
import json
import discord
from discord.ext import commands as c
from discord import FFmpegPCMAudio
from dotenv import load_dotenv
from webserver import keep_alive

load_dotenv()

JSON_FILE = './src/structure.json'
with open(JSON_FILE, encoding='utf8') as jsonFile:
    jsonData = json.load(jsonFile)

client = c.Bot(command_prefix='.')

# return command list in alphabetical order
def getCommands():
    commands = []
    for value in jsonData:
        commands.append(value)
    commands.sort()
    formattedCommands = '\n'.join(commands)
    return formattedCommands

@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == '.help':
        embedVar = discord.Embed(title="Lista de comandos", color=0x00ff00)
        embedVar.add_field(name="Lista", value=getCommands(), inline=False)
        await message.channel.send(embed=embedVar)
        return

    discordCommand = message.content
    if discordCommand in jsonData:
        jsonObject = jsonData[discordCommand]

        if jsonObject['image']:
            await message.channel.send(jsonObject['image'])

        if jsonObject['phrase']:
            await message.channel.send(jsonObject['phrase'])

        if jsonObject['audio']:
            channel = message.author.voice.channel
            voice = await channel.connect()
            source = FFmpegPCMAudio(jsonObject['audio'])
            voice.play(source)
            # Is this really required? Can't be async?
            time.sleep(jsonObject['duration'])
            await voice.disconnect()

    else:
        await message.channel.send('Digite .help para ver a lista de comandos')

keep_alive()
client.run(os.getenv('DISCORD_TOKEN'))
