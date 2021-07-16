
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
from bs4 import BeautifulSoup
import requests
import asyncio
from googletrans import Translator
from dotenv import load_dotenv
from operator import itemgetter, attrgetter

load_dotenv()
TOKEN = os.environ['DISCORD_TOKEN']
intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)

aylon_count = [0]
ydl_opts = {'format': 'bestaudio'}
FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
messg=[]

@client.event
async def on_ready():
  print(os.environ['DISLIKED_MEMBER_ID'])
  print("nothing")
  channel= client.get_channel(864816075458478110)
  messg.append(await channel.send("Verify you are not a bot by pressing the :thumbsup: reaction"))
  await messg[0].add_reaction('\U0001F44D')

  await save_audit_logs(client.guilds[1],discord.utils.get(client.guilds[1].channels, name="general"))



@client.event
async def on_member_join(member):
    await member.send("ברוך הבא לשרת הטוב יותר")


@client.event
async def on_message(message):

  if message.content=="age ranking":
    date_lst=[[member.name,datetime.datetime.now()- member.created_at] for member in message.guild.members]
    date_lst.sort(key=itemgetter(1),reverse=True)
    embed=discord.Embed(title="Oldest users in this server",colour=discord.Colour.random())
    for i in range(0,5):
      embed.add_field(name=str(i+1)+'. '+date_lst[i][0], value=f"{date_lst[i][1].days//365} years, {date_lst[i][1].days%365} days and {date_lst[i][1].seconds//3600} hours")
    await message.channel.send(embed=embed)


  if message.content=="how old":
    trying=datetime.datetime.now() - message.author.created_at
    print (trying.days, trying.seconds//3600, (trying.seconds//60)%60,trying.seconds%60)
    embed= discord.Embed(title= message.author.name+"'s age",colour=discord.Colour.random())
    embed.add_field(name="Years",value=trying.days//365)
    embed.add_field(name="Days",value=trying.days%365)
    embed.add_field(name="Hours",value=trying.seconds//3600)
    embed.add_field(name="Minutes",value=(trying.seconds//60)%60)
    embed.add_field(name="Seconds",value=trying.seconds%60)
    
    await message.channel.send(embed=embed)

  elif message.content.startswith("how old") and len(message.content.split(' '))==3:
    id=''
    for letter in message.content.split(' ')[2]:
      if letter.isdigit():
        id+=letter
    try:
      id=int(id)
      user=client.get_user(id)
      trying=datetime.datetime.now() - user.created_at
      print (trying.days, trying.seconds//3600, (trying.seconds//60)%60,trying.seconds%60)
      embed= discord.Embed(title= user.name+"'s age",colour=discord.Colour.random())
      embed.add_field(name="Years",value=trying.days//365)
      embed.add_field(name="Days",value=trying.days%365)
      embed.add_field(name="Hours",value=trying.seconds//3600)
      embed.add_field(name="Minutes",value=(trying.seconds//60)%60)
      embed.add_field(name="Seconds",value=trying.seconds%60)
    
      await message.channel.send(embed=embed)
    except Exception as e:
      print(e)




  if message.content=="rick roll":
    voiceChannel = message.author.voice
    if voiceChannel is not None:
      try:
        print(voiceChannel.channel)
        await voiceChannel.channel.connect()
      except Exception as e:
        print(e)
    try:   
      ydl_opts = {'format': 'bestaudio'}
      with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info("https://youtu.be/dQw4w9WgXcQ", download=False)
        URL = info['formats'][0]['url']
      voice = get(client.voice_clients, guild=message.author.guild)
      voice.play(discord.FFmpegPCMAudio(URL,**FFMPEG_OPTIONS))
      await asyncio.sleep(20)
      voice.stop()
      await voice.disconnect()

    except Exception as e:
      print(e)   
  elif message.content=="!join":
    voiceChannel = message.author.voice
    if voiceChannel is not None:
      try:
        print(voiceChannel.channel)
        await voiceChannel.channel.connect()
      except Exception as e:
        print(e)
  if message.content== "!SUS":
    embed = discord.Embed(title="AMOGUS",description="||A very sus|| GIF",colour=discord.Colour.red())
    session = aiohttp.ClientSession()
    response = await session.get('http://api.giphy.com/v1/gifs/search?q=' +'SUS among us'+ '&api_key='+os.environ['API_GIPHY']+'&limit=20')
    data = json.loads(await response.text())
    gif_choice = random.randint(0, 19)
    embed.set_image(url=data['data'][gif_choice]['images']['original']['url'])

    await session.close()

    await message.channel.send(embed=embed)

  if "stalin" in message.content.lower():
    embed = discord.Embed(colour=discord.Colour.gold())
    session = aiohttp.ClientSession()
    response = await session.get('http://api.giphy.com/v1/gifs/search?q=' +'communism'+ '&api_key='+os.environ['API_GIPHY']+'&limit=20')
    data = json.loads(await response.text())
    gif_choice = random.randint(0, 19)
    embed.set_image(url=data['data'][gif_choice]['images']['original']['url'])

    await session.close()

    await message.channel.send(embed=embed)
  if message.content == "!time":
    await  message.channel.send(datetime.datetime.now().strftime("%X"))
  print(str(message.author.id) ==str(os.environ['DISLIKED_MEMBER_ID']))
  if str(message.author.id) ==os.environ['ALKOBI'] and message.content==os.environ['ZUKERL_SECRET_WORD']:
    await message.channel.send(message.author.mention + " יובל לוי  ")

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
      await message.reply(translator.translate(msg.content,dest='en').text,tts=True)
    else:
      await message.reply( translator.translate(msg.content,dest='iw').text)

  if message.content=="wyr":
    url = 'http://either.io/'

    x = requests.get(url)
    text=x.text
    option1=text[text.find("option_1")+len("option_1:")+2:]
    option1=option1[:option1.find(',')-1]
    option2=text[text.find("option_2")+len("option_2:")+2:]
    option2=option2[:option2.find(',')-1]
    txt="**Would you rather?** \n:regional_indicator_a: "+option1+"\n**OR** \n:regional_indicator_b: "+option2
    message_temp=await message.channel.send(txt)
    await message_temp.add_reaction(emoji="🇦")
    await message_temp.add_reaction(emoji="🇧")
  elif message.content=="ספר לי עובדה" or message.content=="tell me a fact":
    url = 'https://bestlifeonline.com/animal-facts/'
    random_facts=[]
    x = requests.get(url)
    text=x.text
    soup=BeautifulSoup(text,'lxml')
    for heading in soup.find_all(["h2"])[:75]:
      head=heading.text.strip().strip("0123456789").strip()
      random_facts.append(head)
    fact=random.choice(random_facts)

    if message.content=="ספר לי עובדה":
      translator=Translator()
      await message.channel.send(translator.translate(fact,dest='iw').text)
    else:
      await message.channel.send(fact)








async def save_audit_logs(guild,channel):
  
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
    except Exception as e:
      print(e)
      break


@client.event
async def on_reaction_add(reaction,user):
  print(reaction.emoji)
  print("hey")
  if user.id!=reaction.message.author.id and reaction.message.id==messg[0].id and reaction.emoji=='👍':
    try:
      role=discord.utils.get(user.guild.roles , name="verified")
      await user.add_roles(role)
    except Exception as e:
      print(e)

keep_alive()
client.run(TOKEN)
