import discord
from discord.ext import commands
from discord import FFmpegPCMAudio
import os
from webserver import keep_alive
import time
from listadecomandos import lista


client = commands.Bot(command_prefix='.')

players = {}


@client.event
async def on_ready():
    print("We have logged in as {0.user}"
          .format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('.help'):
      embedVar = discord.Embed(title="Lista de comandos", color=0x00ff00)
      embedVar.add_field(name="Lista", value=lista, inline=False )
      await message.channel.send(embed=embedVar)

    if message.content.startswith('.xoxo'):
        await message.channel.send("https://c.tenor.com/sBtS2bt75twAAAAd/cute-lambida.gif")
        channel = message.author.voice.channel
        voice = await channel.connect()
        source = FFmpegPCMAudio("goat.mp3")
        player = voice.play(source)
        time.sleep(5)
        await voice.disconnect()
    
    if message.content.startswith('.eita') or message.content.startswith('.man'):
      channel = message.author.voice.channel
      voice = await channel.connect()
      source = FFmpegPCMAudio("eitaman.mp3")
      player = voice.play(source)
      time.sleep(1.5)
      await voice.disconnect()

    if message.content.startswith('.rapaaz') or message.content.startswith('.rapaz'):
      await message.channel.send('https://media0.giphy.com/media/fdIFR52nLEJxLzc3tz/giphy.gif')
      channel = message.author.voice.channel

      source = FFmpegPCMAudio("rapaz.mp3")
      player = voice.play(source)
      time.sleep(2)
      await voice.disconnect()

    if message.content.startswith('.irra') or message.content.startswith('.ira'):
      await message.channel.send('IRRAAAAA!!')
      channel = message.author.voice.channel
      voice = await channel.connect()
      source = FFmpegPCMAudio("irra.mp3")
      player = voice.play(source)
      time.sleep(3)
      await voice.disconnect()

    if message.content.startswith('.yamete') or message.content.startswith('.kudasai'):
      await message.channel.send("YAMETE KUDASAI!!")
      channel = message.author.voice.channel
      voice = await channel.connect()
      source = FFmpegPCMAudio("yamete.mp3")
      player = voice.play(source)
      time.sleep(5)
      await voice.disconnect()

    if message.content.startswith('.posto7'):
      await message.channel.send("VENHA AQUI NO POSTO 7!!")
      channel = message.author.voice.channel
      voice = await channel.connect()
      source = FFmpegPCMAudio("posto7.mp3")
      player = voice.play(source)
      time.sleep(10.1)
      await voice.disconnect()

    if message.content.startswith('.dejavu'):
      channel = message.author.voice.channel
      voice = await channel.connect()
      source = FFmpegPCMAudio("bandadejavu.mp3")
      player = voice.play(source)
      time.sleep(1.6)
      await voice.disconnect()

    if message.content.startswith('.cavalo'):
      channel = message.author.voice.channel
      voice = await channel.connect()
      source = FFmpegPCMAudio("cavalo.mp3")
      player = voice.play(source)
      time.sleep(1.6)
      await voice.disconnect()

    if message.content.startswith('.merda'):
      channel = message.author.voice.channel
      voice = await channel.connect()
      source = FFmpegPCMAudio("convmerda.mp3")
      player = voice.play(source)
      time.sleep(16.5)
      await voice.disconnect()
    
    if message.content.startswith('.cadeirudo'):
      channel = message.author.voice.channel
      voice = await channel.connect()
      source = FFmpegPCMAudio("cadeirudo.mp3")
      player = voice.play(source)
      time.sleep(8.5)
      await voice.disconnect()

    if message.content.startswith('.trabaia') or message.content.startswith('.suagu'):
      channel = message.author.voice.channel
      voice = await channel.connect()
      source = FFmpegPCMAudio("trabaia.mp3")
      player = voice.play(source)
      time.sleep(8.5)
      await voice.disconnect()

    if message.content.startswith('.sistema'):
      channel = message.author.voice.channel
      voice = await channel.connect()
      source = FFmpegPCMAudio("sistema.mp3")
      player = voice.play(source)
      time.sleep(14.5)
      await voice.disconnect()

    if message.content.startswith('.uepa') or       message.content.startswith('.epa'):
      channel = message.author.voice.channel
      voice = await channel.connect()
      source = FFmpegPCMAudio("uepa.mp3")
      player = voice.play(source)
      time.sleep(2)
      await voice.disconnect()


    if message.content.startswith('.pauquebrando') or       message.content.startswith('.eitaporra') or message.content.startswith('.briga'):
      channel = message.author.voice.channel
      voice = await channel.connect()
      source = FFmpegPCMAudio("briga.mp3")
      player = voice.play(source)
      time.sleep(8)
      await voice.disconnect()

    if message.content.startswith('.pare'):
      channel = message.author.voice.channel
      voice = await channel.connect()
      source = FFmpegPCMAudio("pare.mp3")
      player = voice.play(source)
      time.sleep(2)
      await voice.disconnect()

    if message.content.startswith('.bora') or message.content.startswith('.horadoshow'):
      channel = message.author.voice.channel
      voice = await channel.connect()
      source = FFmpegPCMAudio("bambam1.mp3")
      player = voice.play(source)
      time.sleep(4.5)
      await voice.disconnect()

    if message.content.startswith('.cademeupau'):
      channel = message.author.voice.channel
      voice = await channel.connect()
      source = FFmpegPCMAudio("cademeu.mp3")
      player = voice.play(source)
      time.sleep(15.5)
      await voice.disconnect()
  
    if message.content.startswith('.moreno'):
      channel = message.author.voice.channel
      voice = await channel.connect()
      source = FFmpegPCMAudio("moreno.mp3")
      player = voice.play(source)
      time.sleep(6)
      await voice.disconnect()

    if message.content.startswith('.marilene'):
      channel = message.author.voice.channel
      voice = await channel.connect()
      source = FFmpegPCMAudio("marilene.mp3")
      player = voice.play(source)
      time.sleep(6.5)
      await voice.disconnect()

    if message.content.startswith('.naoconsegue') or message.content.startswith('.moises'):
      channel = message.author.voice.channel
      voice = await channel.connect()
      source = FFmpegPCMAudio("naoconsegue.mp3")
      player = voice.play(source)
      time.sleep(2)
      await voice.disconnect()

    if message.content.startswith('.taz') or message.content.startswith('.mania'):
      channel = message.author.voice.channel
      voice = await channel.connect()
      source = FFmpegPCMAudio("tazmania.mp3")
      player = voice.play(source)
      time.sleep(8)
      await voice.disconnect()

    if message.content.startswith('.gonorreia'):
      channel = message.author.voice.channel
      voice = await channel.connect()
      source = FFmpegPCMAudio("gonorreia.mp3")
      player = voice.play(source)
      time.sleep(14)
      await voice.disconnect()

    if message.content.startswith('.calma'):
      channel = message.author.voice.channel
      voice = await channel.connect()
      source = FFmpegPCMAudio("calma.mp3")
      player = voice.play(source)
      time.sleep(3)
      await voice.disconnect()

    if message.content.startswith('.javaiboltz'):
      channel = message.author.voice.channel
      voice = await channel.connect()
      source = FFmpegPCMAudio("javaiboltz.mp3")
      player = voice.play(source)
      time.sleep(3.5)
      await voice.disconnect()

    if message.content.startswith('.bicho') or message.content.startswith('.piruleta'):
      channel = message.author.voice.channel
      voice = await channel.connect()
      source = FFmpegPCMAudio("bichopiruleta.mp3")
      player = voice.play(source)
      time.sleep(8)
      await voice.disconnect()
            

    if message.content.startswith('.fdp') or message.content.startswith('.filadaputa'):
      channel = message.author.voice.channel
      voice = await channel.connect()
      source = FFmpegPCMAudio("fdp.mp3")
      player = voice.play(source)
      time.sleep(4)
      await voice.disconnect()

    if message.content.startswith('.puta'):
      channel = message.author.voice.channel
      voice = await channel.connect()
      source = FFmpegPCMAudio("puta1.mp3")
      player = voice.play(source)
      time.sleep(3.5)
      await voice.disconnect()


    if message.content.startswith('.bioca'):
      await message.channel.send('https://i1.sndcdn.com/avatars-000092598790-6np24c-t240x240.jpg')
      channel = message.author.voice.channel
      voice = await channel.connect()
      source = FFmpegPCMAudio("bebo1.mp3")
      player = voice.play(source)
      time.sleep(19)
      await voice.disconnect()

    if message.content.startswith('.chucky'):
      channel = message.author.voice.channel
      voice = await channel.connect()
      source = FFmpegPCMAudio("jogueseu.mp3")
      player = voice.play(source)
      time.sleep(8)
      await voice.disconnect()
    
    if message.content.startswith('.detras'):
      await message.channel.send("DETRÁS DE TI, IMBÉCIL")
      await message.channel.send("https://lparchive.org/LetsPlay/RE4/Update%2016/rockthefuckout.gif")
      channel = message.author.voice.channel
      voice = await channel.connect()
      source = FFmpegPCMAudio("detras.mp3")
      player = voice.play(source)
      time.sleep(5)
      await voice.disconnect()
      

    if message.content.startswith('.vainao'):
      channel = message.author.voice.channel
      voice = await channel.connect()
      source = FFmpegPCMAudio("vainao.mp3")
      player = voice.play(source)
      time.sleep(4)
      await voice.disconnect()

    if message.content.startswith('.linguinha'):
      channel = message.author.voice.channel
      voice = await channel.connect()
      source = FFmpegPCMAudio("linguinha.mp3")
      player = voice.play(source)
      time.sleep(3)
      await voice.disconnect()
    
    if message.content.startswith('.pedemesa'):
      channel = message.author.voice.channel
      voice = await channel.connect()
      source = FFmpegPCMAudio("quem esfolou.mp3")
      player = voice.play(source)
      time.sleep(4)
      await voice.disconnect()
    
    if message.content.startswith('.testa'):
      channel = message.author.voice.channel
      voice = await channel.connect()
      source = FFmpegPCMAudio("testa na cabeça.mp3")
      player = voice.play(source)
      time.sleep(10)
      await voice.disconnect()

    if message.content.startswith('.mickey'):
      channel = message.author.voice.channel
      voice = await channel.connect()
      source = FFmpegPCMAudio("mickey.mp3")
      player = voice.play(source)
      time.sleep(8)
      await voice.disconnect()

    if message.content.startswith('.weedzao'):
      channel = message.author.voice.channel
      voice = await channel.connect()
      source = FFmpegPCMAudio("weedzao.mp3")
      player = voice.play(source)
      time.sleep(15)
      await voice.disconnect()

    if message.content.startswith('.doisovim'):
      channel = message.author.voice.channel
      voice = await channel.connect()
      source = FFmpegPCMAudio("doisovim.mp3")
      player = voice.play(source)
      time.sleep(11)
      await voice.disconnect()

    if message.content.startswith('.partido'):
      channel = message.author.voice.channel
      voice = await channel.connect()
      source = FFmpegPCMAudio("partidodocara.mp3")
      player = voice.play(source)
      time.sleep(4)
      await voice.disconnect()
    
    if message.content.startswith('.treinar'):
      channel = message.author.voice.channel
      voice = await channel.connect()
      source = FFmpegPCMAudio("treinar.mp3")
      player = voice.play(source)
      time.sleep(19)
      await voice.disconnect()

    if message.content.startswith('.alarme'):
      channel = message.author.voice.channel
      voice = await channel.connect()
      source = FFmpegPCMAudio("alarme.mp3")
      player = voice.play(source)
      time.sleep(7)
      await voice.disconnect()

    if message.content.startswith('.fantasias'):
      channel = message.author.voice.channel
      voice = await channel.connect()
      source = FFmpegPCMAudio("fantasias.mp3")
      player = voice.play(source)
      time.sleep(13)
      await voice.disconnect()

    if message.content.startswith('.fudido'):
      channel = message.author.voice.channel
      voice = await channel.connect()
      source = FFmpegPCMAudio("fudido.mp3")
      player = voice.play(source)
      time.sleep(6)
      await voice.disconnect()
 
    if message.content.startswith('.sextacheira'):
      channel = message.author.voice.channel
      voice = await channel.connect()
      source = FFmpegPCMAudio("sextacheira.mp3")
      player = voice.play(source)
      time.sleep(91)
      await voice.disconnect()
    
    if message.content.startswith('.aloispetor'):
      channel = message.author.voice.channel
      voice = await channel.connect()
      source = FFmpegPCMAudio("aloispetor.mp3")
      player = voice.play(source)
      time.sleep(91)
      await voice.disconnect()


keep_alive()
client.run(os.getenv('TOKEN'))