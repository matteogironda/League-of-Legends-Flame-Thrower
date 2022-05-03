import os 
import discord
import get_match as gm

TOKEN = 'token-number'
client = discord.Client()
guild = discord.Guild
channel = client.get_guild(970872820081000529)

@client.event
async def on_ready():
    print(f'{client.user} has connected')
    return

@client.event
async def on_message(message):

    msg = message.content
    summoner = msg[1]

    if msg == "Is f{summoner} good at League?": 
        channel.send(gm.throw_flame(summoner))
    else:
        pass
    return

client.run(TOKEN)
