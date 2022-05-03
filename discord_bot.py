import os 
import discord
import get_match as gm

TOKEN = 'your-token-key'
client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected')
    return

@client.event
async def on_message(message):

    if message.author == client.user:
        return
    
    msg = message.content
    summoner = msg.split()[1]

    if msg == "Is "+ summoner + " good at League?": 
        await message.channel.send(gm.throw_flame(summoner))
    else:
        print('not it')
        pass
    return

client.run(TOKEN)
