
# dead.py
import os
import random
import discord
from discord.utils import get
from discord.ext import commands
import youtube_dl
import datetime
from KeepAlive import keep_alive
import json
import aiohttp
import random
from googletrans import Translator
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.environ['DISCORD_TOKEN']
intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)

aylon_count = [0]
is_running=[False]

@client.event
async def on_ready():
  print(os.environ['DISLIKED_MEMBER_ID'])
  print("nothing")


@client.event
async def on_member_join(member):
    member.send("ברוך הבא לשרת הטוב יותר")


@client.event
async def on_message(message):
  if message.content== "!SUS":
    embed = discord.Embed(colour=discord.Colour.red())
    session = aiohttp.ClientSession()
    response = await session.get('http://api.giphy.com/v1/gifs/search?q=' +'SUS among us'+ '&api_key='+os.environ['API_GIPHY']+'&limit=10')
    data = json.loads(await response.text())
    gif_choice = random.randint(0, 9)
    embed.set_image(url=data['data'][gif_choice]['images']['original']['url'])

    await session.close()

    await message.channel.send(embed=embed)
  if message.content == "!time":
    await  message.channel.send(datetime.datetime.now().strftime("%X"))
  print(str(message.author.id) ==str(os.environ['DISLIKED_MEMBER_ID']))
  if str(message.author.id) ==os.environ['ALKOBI'] and message.content==os.environ['ZUKERL_SECRET_WORD']:
    await message.channel.send(message.author.mention + "יובל לוי ")

  if str(message.author.id) == str(os.environ['LIKED_MEMBER_ID']):
    aylon_count[0] += 1
    if aylon_count[0] == 3:
      await message.channel.send(message.author.mention + " You are the king of this server")
      aylon_count[0] = 0

  if str(message.author.id) == str(os.environ['ZUKREL']):
    await message.reply(message.author.mention+"אבל מי שאל?")
  print (message.author.id)
  if str(message.author.id)==os.environ['NARCISSISM'] and  message.content.startswith('!'):
    await message.reply(":point_up_2_tone2:"+" המלך אמר")

  if message.content=="תרגם לי" and message.reference is not None:
    if message.reference.cached_message is None:
        # Fetching the message
      channel = client.get_channel(message.reference.channel_id)
      msg = await channel.fetch_message(message.reference.message_id)

    else:
      msg = message.reference.cached_message
    translator=Translator()
    if translator.translate(msg.content).src=='iw':
      await message.reply( translator.translate(msg.content,dest='en').text)
    else:
      await message.reply( translator.translate(msg.content,dest='iw').text)
  await save_audit_logs(message.channel.guild,message.channel)


async def save_audit_logs(guild,channel):
  
  if is_running[0]:
    return 
  else:
    is_running[0]=True
  previous_entry= None
  for member in guild.members:
    if str(member.id) == str(os.environ['DISLIKED_MEMBER_ID']):
      snitch_user=member
      snitch_id=member.id
      break
  notifyUser='<@%a>' %snitch_id

  while True:
    try:
      async for entry in guild.audit_logs(limit=1):
        if  previous_entry is not  None and entry !=  previous_entry:
          print(entry)
          print (('{0.user}'.format(entry))+" STOP DISCONNECTING")
          if entry.user==snitch_user:
            await channel.send(notifyUser+" STOP DISCONNECTING")
        previous_entry = entry
    except:
      break




  is_running[0]=False

keep_alive()
client.run(TOKEN)
