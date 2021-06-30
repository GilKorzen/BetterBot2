
# dead.py
import os
import random
import discord
from discord.utils import get
from discord.ext import commands
import youtube_dl
import datetime
from KeepAlive import keep_alive

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
  if message.content == "!time":
    await  message.channel.send(datetime.datetime.now().strftime("%X"))
  print(str(message.author.id) ==str(os.environ['DISLIKED_MEMBER_ID']))
  if str(message.author.id) ==str(os.environ['DISLIKED_MEMBER_ID']) and message.content==os.environ['ZUKERL_SECRET_WORD']:
    await message.channel.send(message.author.mention + "יובל לוי")

  if str(message.author.id) == str(os.environ['LIKED_MEMBER_ID']):
    aylon_count[0] += 1
    if aylon_count[0] == 3:
      await message.channel.send(message.author.mention + " You are the king of this server")
      aylon_count[0] = 0

  if str(message.author.id) == str(os.environ['ZUKREL']):
    await message.reply(message.author.mention+"אבל מי שאל?")
  print (message.author.id)
  if str(message.author.id)==os.environ['NARCISSISM']:
    await message.reply(":point_up_2_tone2:"+" המלך אמר")
  await save_audit_logs(message.channel.guild,message.channel)


async def save_audit_logs(guild,channel):
  
  if is_running[0]:
    return
  else:
    is_running[0]=True
  previous_entry= None
   # with open(f'audit_logs_{guild.name}', 'r'):
  for member in guild.members:
    if str(member.id) == str(os.environ['DISLIKED_MEMBER_ID']):
      snitch_name=member.name
      snitch_user=member
      snitch_id=member.id
      break
  notifyUser='<@%a>' %snitch_id

  while True:
    async for entry in guild.audit_logs(limit=1):
      if  previous_entry is not  None and entry != previous_entry:
        print(entry)
        print (('{0.user}'.format(entry))+" STOP DISCONNECTING")
        if entry.user==snitch_user:
          await channel.send(notifyUser+" STOP DISCONNECTING")


      previous_entry = entry

  is_running[0]=False

keep_alive()
client.run(TOKEN)
