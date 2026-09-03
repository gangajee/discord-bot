import os
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

instents = discord.Intents.default()
instents.message_content = True

client = discord.Client(intents=instents)

@client.event
async def on_ready() :
  print(f'Log in Complete : {client.user}')

@client.event
async def on_message(message): 
  if message.author == client.user :
    return

  if message.content.startwith('hello') :
    await message.channel.send('hello, this is Pseudo-Investmemt discord-Bot')

client.run(TOKEN)

