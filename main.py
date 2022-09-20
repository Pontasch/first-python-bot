import discord
import os
import time
import discord.ext
from discord.utils import get
from discord.ext import commands, tasks
from discord.ext.commands import has_permissions, CheckFailure, check #do not include brackets or file types
import asyncio
import random
from async_timeout import timeout
import youtube_dl
from pyrandmeme import *
from http.server import HTTPServer, CGIHTTPRequestHandler
from keep_alive import keep_alive
from discord_slash import SlashCommand
import requests
import randfacts
from gtts import gTTS 
# Imports 
guild_ids = os.environ['GUILDS']
my_secret = os.environ['API_KEY']

# Secret

#

# Client start


client =commands.Bot(command_prefix=commands.when_mentioned_or('#'), help_command=None,intents=discord.Intents.all())
client.remove_command('help')

slash = SlashCommand(client, sync_commands=True)



@client.event
async def on_ready():
 
  print("bot online")  # will print "bot online" in the console when the bot is online
  await client.change_presence(activity=discord.Streaming(name='Potatos twitch', url="https://www.twitch.tv/oofed987"))
  

# Client end

# commands start
@client.command()
async def help(ctx):
    embed  = discord.Embed(title="PythonBoi",
                          url='https://discord.com/oauth2/authorize?client_id=841140373597585408&permissions=1133584&scope=bot',
                          description="Commands", color=0x00ff2a)
    embed.set_thumbnail(
        url='https://cdn.discordapp.com/app-icons/841140373597585408/90899d7c65f4fe78a653abbb9d9c0e55.png?size=512')
    embed.add_field(name="#help", value="Shows this menu.", inline=False)
    embed.add_field(name="#ping", value="I respond with Pong!", inline=False)
    embed.add_field(name="#killerkitten", value="Tells you the truth about him.", inline=False)
    embed.set_footer(text="Made by Dave124#6969")
    await ctx.send(embed=embed)
    

@client.command()
async def ping(ctx):
    await ctx.send("pong!")  # simple command so that when you type "!ping" the bot will respond with "pong!"
    

@client.command()
async def graph(ctx):
    await discord.ext.channel.send(findgraph(message.content.lower()))


@client.command()
async def killerkitten(ctx):
    await ctx.send("is biased and leaked Dave's address!")


@client.command()
async def nerd(ctx):
    await ctx.send(randfacts.get_fact())


@client.command()
async def nsfwnerd(ctx):
    await ctx.send(randfacts.get_fact(only_unsafe=True))

@client.command()
async def meme(ctx):
    await ctx.send(embed=await pyrandmeme())


@client.command()
async def gop(ctx):
    await ctx.send("gop")

# End of Musicplayer

@client.command()
async def coc(ctx):
    await ctx.send("coc")


@client.command()
async def say(ctx, *, message):
    myobj = gTTS(text=message, lang="en", slow=False) 
    myobj.save("output.mp3") 
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    voiceChannel = ctx.author.voice.channel
    if voice == None:
      await voiceChannel.connect()
      voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
      voice.play(discord.FFmpegPCMAudio("output.mp3"))
    else :
      voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
      voice.play(discord.FFmpegPCMAudio("output.mp3"))
    await ctx.send(message)


# Start of Musicplayer

@client.command()
async def play(ctx, url2 : str):
    song_there = os.path.isfile("song.mp3")
    try:
        if song_there:
            os.remove("song.mp3")
    except PermissionError:
        await ctx.send("Wait for the current playing music to end or use the 'stop' command")

        return

    voiceChannel = ctx.author.voice.channel
    await voiceChannel.connect()
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)

    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
            
        }],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url2])
    for file in os.listdir("./"):
        if file.endswith(".mp3"):
            os.rename(file, "song.mp3")
    voice.play(discord.FFmpegPCMAudio("song.mp3"))

@client.command()
async def when(ctx):
    voiceChannel = ctx.author.voice.channel
    await voiceChannel.connect()
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    voice.play(discord.FFmpegPCMAudio("Sounds/when_you.mp3"))
    await asyncio.sleep(8)
    await voice.disconnect()
    


@client.command()
async def leave(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_connected():
        await voice.disconnect()
    else:
        await ctx.send("The bot is not connected to a voice channel.")


@client.command()
async def pause(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_playing():
        voice.pause()
    else:
        await ctx.send("Currently no audio is playing.")


@client.command()
async def resume(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_paused():
        voice.resume()
    else:
        await ctx.send("The audio is not paused.")


@client.command()
async def stop(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    voice.stop()

# End of Musicplayer


guild_ids = [800746663048118303]

@slash.slash(name="ping", guild_ids=guild_ids)
async def _ping(ctx): # Defines a new "context" (ctx) command called "ping."
    await ctx.send(f"Pong!")


@slash.slash(name="help", guild_ids = guild_ids)
async def help(ctx):
    embed  = discord.Embed(title="PythonBoi",
                          url='https://discord.com/oauth2/authorize?client_id=841140373597585408&permissions=1133584&scope=bot',
                          description="Commands", color=0x00ff2a)
    embed.set_thumbnail(
        url='https://cdn.discordapp.com/app-icons/841140373597585408/90899d7c65f4fe78a653abbb9d9c0e55.png?size=512')
    embed.add_field(name="#help", value="Shows this menu.", inline=False)
    embed.add_field(name="#ping", value="I respond with Pong!", inline=False)
    embed.add_field(name="#killerkitten", value="Tells you the truth about him.", inline=False)
    embed.add_field(name="#nerd", value="Gives you a random fact", inline=False  )
    embed.set_footer(text="Made by Dave124#6969")
    await ctx.send(embed=embed)

@slash.slash(name="Killerkitten", guild_ids = guild_ids)
async def killerkitten(ctx):
    await ctx.send("is biased and leaked Dave's address!")

@slash.slash(name="nerd", guild_ids = guild_ids)
async def nerd(ctx):
    await ctx.send(randfacts.get_fact())


@slash.slash(name="nsfwnerd", guild_ids = guild_ids)
async def nsfwnerd(ctx):
    await ctx.send(randfacts.get_fact(only_unsafe=True))

@slash.slash(name="meme", guild_ids = guild_ids)
async def meme(ctx):
    await ctx.send(embed=await pyrandmeme())

@slash.slash(name="gop", guild_ids = guild_ids)
async def gop(ctx):
    await ctx.send("gop")
# End of Musicplayer

@slash.slash(name="coc", guild_ids = guild_ids)
async def coc(ctx):
    await ctx.send("coc")


    
@slash.slash(name="when", guild_ids = guild_ids)
async def when(ctx):
    voiceChannel = ctx.author.voice.channel
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    await voiceChannel.connect()
    voice.play(discord.FFmpegPCMAudio("when.mp3"))
    await asyncio.sleep(8)
    await voice.disconnect()
  


keep_alive()
client.run(my_secret)

