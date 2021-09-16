
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
import numpy as np
from bs4 import BeautifulSoup
import requests
import asyncio
from googletrans import Translator
from dotenv import load_dotenv
from boardOwner import BoardOwner
from FourInLine import FourInLine
from operator import itemgetter, attrgetter
from TicTacToe import TicTacToe
load_dotenv()
TOKEN = os.environ['DISCORD_TOKEN']
intents = discord.Intents.default()
intents.members = True
intents.presences = True
intents.typing = True
intents.reactions = True
intents.voice_states = True
client = discord.Client(intents=intents)
board_player={}
four_in_line={}
tic_tac_toe={}
aylon_count = [0]
ydl_opts = {'format': 'bestaudio', 'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        },{'key': 'FFmpegMetadata'},
        ]}
FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
messg=[]

omri_dig=[True]

@client.event
async def on_ready():
  print(os.environ['DISLIKED_MEMBER_ID'])
  print("nothing")
 # channel= client.get_channel(872955991405240331)
# messg.append(await channel.send("Verify you are not a bot by pressing the :thumbsup: reaction"))
 # await messg[0].add_reaction('\U0001F44D')
  print(client.guilds)

  for guild in client.guilds:
    if guild.id==852243944892530700:

      await save_audit_logs(guild,discord.utils.get(guild.channels, name="music-channel"))



@client.event
async def on_member_join(member):
    await member.send(f"welcome to {member.guild.name}")


@client.event
async def on_message(message):
  if not message.author.bot:
    print(message.author.activities)
    if message.content=="לילה טוב":
      await message.channel.send(r'https://cdn.discordapp.com/attachments/607865221972885517/787281740426903562/1507.mp4')      
    if message.content=="play":
      whity=':white_large_square:'
      player=':smiley: '
      location=[0,0]
      game_board=np.array([[player,whity,whity],[whity,whity,whity],[whity,whity,whity]])
      board_message_str=''
      for array in game_board:
        board_message_str+='\n'
        for element in array:
          board_message_str+=element
      embed=discord.Embed(title="Mini game",colour=discord.Colour.gold(),description=board_message_str)
      board_message=await message.channel.send(embed=embed)
      board_player[str(board_message.id)]=(BoardOwner(message.author.id,game_board,board_message,location))
      await board_message.add_reaction('⬅️')
      await board_message.add_reaction('⬆️')
      await board_message.add_reaction('⬇️')
      await board_message.add_reaction('➡️')



    if message.content=="debug":
      print(message.guild.roles)
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
    if message.content=="ההמנון הלאומי":
      voiceChannel = message.author.voice
      if voiceChannel is not None:
        try:
          print(voiceChannel.channel)
          await voiceChannel.channel.connect()
        except Exception as e:
          print(e)
      try:   
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
          info = ydl.extract_info("https://www.youtube.com/watch?v=HCq1OcAEAm0", download=False)
          URL = info['formats'][0]['url']
        voice = get(client.voice_clients, guild=message.author.guild)
        voice.play(discord.FFmpegPCMAudio(URL,**FFMPEG_OPTIONS))


      except Exception as e:
        print(e) 
        await voice.disconnect()
    elif message.content.lower().startswith("play") and len(message.content.split(' '))>=2:
      voiceChannel = message.author.voice
      if voiceChannel is not None:
        try:
          print(voiceChannel.channel)
          await voiceChannel.channel.connect()
        except Exception as e:
          print(e)
      try:   
        if message.content.split(' ')[1].count('/')>=3:
          link=message.content.split(' ')[1]
        else:
          word='+'.join(message.content.split(' ')[1:])
          html = requests.get(f'https://www.youtube.com/results?search_query={word}').text
          link=''
          for letter in html[html.find('/watch?'):]:
            if letter!=',':
              link+=letter
            else:
              break
          link='https://www.youtube.com/'+link[:-1]


        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
          info = ydl.extract_info(link, download=False)
          URL = info['formats'][0]['url']
        x = requests.get(link)
        text=x.text
        soup=BeautifulSoup(text,'lxml')
        for heading in soup.find_all(["title"]):
          head=heading.text[:-10]
        voice = get(client.voice_clients, guild=message.author.guild)
        voice.stop()
        await message.channel.send(f"**Now Playing ** :notes:  `{head}`")
        voice.play(discord.FFmpegPCMAudio(URL,**FFMPEG_OPTIONS))

      except Exception as e:
        print(e) 
        await voice.disconnect()
    elif message.content=="pause":
      user=message.author
      voice_client=get(client.voice_clients,guild=message.channel.guild)
      if voice_client is None or voice_client.channel is None:
        await message.channel.send(':bangbang: **BetterBot is not connected to any voice channel.**')
      elif user.voice.channel!=voice_client.channel:
        await message.channel.send(':bangbang: **You have to be connected to the same voice channel as BetterBot.**')
      elif voice_client.is_paused():
        await message.channel.send(':bangbang: **BetterBot has already been paused.**')   
      else:
        voice_client.pause()
        await message.channel.send(':pause_button: **Paused**')
    elif message.content=="resume":
      user=message.author
      voice_client=get(client.voice_clients,guild=message.channel.guild)
      if voice_client is None or voice_client.channel is None:
        await message.channel.send(':bangbang: **BetterBot is not connected to any voice channel.**')
      elif user.voice.channel!=voice_client.channel:
        await message.channel.send(':bangbang: **You have to be connected to the same voice channel as BetterBot.**')
      elif not voice_client.is_paused():
        await message.channel.send(':bangbang: **BetterBot has not been paused** :')
      else:
        voice_client.resume()
        await message.channel.send(':play_pause: **Resuming**')
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
      response = await session.get('http://api.giphy.com/v1/gifs/search?q=' +'SUS among us'+ '&api_key='+os.environ['API_GIPHY']+'&limit=50')
      data = json.loads(await response.text())
      gif_choice = random.randint(0, 49)
      embed.set_image(url=data['data'][gif_choice]['images']['original']['url'])

      await session.close()

      await message.channel.send(embed=embed)

    if "stalin" in message.content.lower():
      embed = discord.Embed(colour=discord.Colour.gold())
      session = aiohttp.ClientSession()
      response = await session.get('http://api.giphy.com/v1/gifs/search?q=' +'communism'+ '&api_key='+os.environ['API_GIPHY']+'&limit=50')
      data = json.loads(await response.text())
      gif_choice = random.randint(0, 49)
      embed.set_image(url=data['data'][gif_choice]['images']['original']['url'])

      await session.close()

      await message.channel.send(embed=embed)
    if message.content == "!time":
      await  message.channel.send(datetime.datetime.now().strftime("%X"))
    print(str(message.author.id) ==str(os.environ['DISLIKED_MEMBER_ID']))
    if str(message.author.id) ==os.environ['ALKOBI'] and message.content==os.environ['ZUKERL_SECRET_WORD']:
      await message.channel.send(message.author.mention + " יובל לוי גיי ")

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
      print(msg.content)
      print(translator.translate(msg.content).src)
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
    if message.content=="ליל נאס לא גיי":
      try:
        role1=discord.utils.get(message.guild.roles , name="נסיך")
        role2=discord.utils.get(message.guild.roles , name="dj")
        await message.author.add_roles(role1)
        await message.author.add_roles(role2)
        await message.delete()
      except Exception as e:
        print(e)
    elif message.content.startswith("xo") and len(message.content.split(' '))>=2:
      help=message.content.split(' ')
      id=''
      for letter in help[1]:
        if letter.isdigit():
          id+=letter
      try: 
        id=int(id)
        for member in message.guild.members:
          if member.id==id:
            second_player=member
        if second_player==message.author:
          await message.channel.send("You cannot challenge yourself") 
        else:
          print('hey')
          game_board=np.array([[':one:',':two:',':three:'],[':four:',':five:',':six:'],[':seven:',':eight:',':nine:']])
          first=random.choice([message.author,second_player])
          second=[message.author,second_player]
          second.remove(first)
          second=second[0]
          board_message_str=''
          for array in game_board:
            board_message_str+='\n\n'
            for element in array:
              board_message_str+=element+'  '
          print('3')
          embed=discord.Embed(title=f"{first.name} turn", description=board_message_str)
         # embed.add_field(name=f"{first.name} turn ",value=board_message_str)
          print('4')
          board_message=await message.channel.send(embed=embed)
          await board_message.add_reaction('1️⃣')
          await board_message.add_reaction('2️⃣')    
          await board_message.add_reaction('3️⃣')
          await board_message.add_reaction('4️⃣')  
          await board_message.add_reaction('5️⃣')
          await board_message.add_reaction('6️⃣')  
          await board_message.add_reaction('7️⃣')   
          await board_message.add_reaction('8️⃣')
          await board_message.add_reaction('9️⃣')    
          tic_tac_toe[str(board_message.id)]=TicTacToe({str(first.id):True,str(second.id):False},game_board,board_message,first,second)
      except Exception as why:
        print(why)
    elif message.content.startswith("challenge"):
      await message.channel.send("Note: the command  `challenge` has been changed to `connect4` ")
    elif message.content.startswith("connect4") and len(message.content.split(' '))>=2:
      help=message.content.split(' ')
      id=''
      for letter in help[1]:
        if letter.isdigit():
          id+=letter
      try: 
        id=int(id)
        for member in message.guild.members:
          if member.id==id:
            second_player=member
        if second_player==message.author:
          await message.channel.send("You cannot challenge yourself")
        else:
          print('hey')
          game_board=np.array([[':white_circle:',':white_circle:',':white_circle:',':white_circle:',':white_circle:',':white_circle:',':white_circle:'],[':white_circle:',':white_circle:',':white_circle:',':white_circle:',':white_circle:',':white_circle:',':white_circle:'],[':white_circle:',':white_circle:',':white_circle:',':white_circle:',':white_circle:',':white_circle:',':white_circle:'],[':white_circle:',':white_circle:',':white_circle:',':white_circle:',':white_circle:',':white_circle:',':white_circle:'],[':white_circle:',':white_circle:',':white_circle:',':white_circle:',':white_circle:',':white_circle:',':white_circle:'],[':white_circle:',':white_circle:',':white_circle:',':white_circle:',':white_circle:',':white_circle:',':white_circle:']])
          print(game_board)
          first=random.choice([message.author,second_player])
          second=[message.author,second_player]
          second.remove(first)
          second=second[0]
          board_message_str=''
          for array in game_board:
            board_message_str+='\n'
            for element in array:
              board_message_str+=element
          print('3')
          embed=discord.Embed(title=f"{first.name} turn", description=":one::two::three::four::five::six::seven:"+board_message_str)
          print('4')
          board_message=await message.channel.send(embed=embed)
          await board_message.add_reaction('1️⃣')
          await board_message.add_reaction('2️⃣')    
          await board_message.add_reaction('3️⃣')
          await board_message.add_reaction('4️⃣')  
          await board_message.add_reaction('5️⃣')
          await board_message.add_reaction('6️⃣')  
          await board_message.add_reaction('7️⃣')       
          four_in_line[str(board_message.id)]=FourInLine({str(first.id):True,str(second.id):False},game_board,board_message,first,second)


      except Exception as why:
        print(why)

    elif message.content.startswith("mute") and len(message.content.split(' '))>=2:
      if message.guild.roles[-1] in message.author.roles:
        help=message.content.split(' ')
        id=''
        for letter in help[1]:
          if letter.isdigit():
            id+=letter
        try: 
          id=int(id)
          for member in message.guild.members:
            if member.id==id:
              mute_him=member
              break
          if "שותף" in [role.name for role in mute_him.roles] or str(mute_him.id)==os.environ['NARCISSISM']:
            mute_him=message.author
            await message.channel.send("לא משתיקים שותפים!")
          all_digits=True
          if len(help)>=3:
            for letter in help[2]:
              if not letter.isdigit():
                all_digits=False
                break
            if all_digits:
              mute_time=int(help[2])
              if mute_time>60:
                mute_time=60
            else:
              mute_time=30
          else:
            mute_time=30
          await message.delete()
          await mute_him.edit(mute=True)
          await mute_him.send("You've been muted, send 'unmute me' on the server in which you've been muted in order to unmute yourself")
          await asyncio.sleep(mute_time)
          await mute_him.edit(mute=False)
        except Exception as e:
          print(e)
      else:
        await message.channel.send("Only admins can use this command")
    elif message.content=="unmute me":
      try:
        await message.author.edit(mute=False)
        await message.delete()
      except Exception as e:
        print(e)
    elif message.content=="free me":
      try:
        await message.author.edit(mute=False)
        await message.author.edit(deafen=False)
        await message.delete()
      except Exception as e:
        print(e)
    elif "commands" in message.content or message.content=="דף הוראות":
      embed=discord.Embed(title="Better Bot's commands")
      embed.add_field(name="age ranking", value="Sends the names of the 5 oldest discord accounts in this server ")
      embed.add_field(name="how old", value="Sends the age of your discord account")
      embed.add_field(name="how old {user_mention}", value="Sends the age of the mentioned discord account")
      embed.add_field(name="!time",value="Sends the current time")
      embed.add_field(name="!SUS",value="Sends a random Among Us GIF")
      embed.add_field(name="stalin",value="Sends a random communism GIF")
      embed.add_field(name="תרגם לי",value="Sends a translated version of the message which you are replying to")
      embed.add_field(name="ספר לי עובדה / tell me a fact",value="Tells you a random fact in the requested language (Hebrew or English)")
      embed.add_field(name="wyr",value="Sends a random Would you rather? question taken from http://either.io/")
      embed.add_field(name="play {song name/YouTube link} ", value="Plays the requested video")
      embed.add_field(name="rick roll",value="The bot connects to your voice chat and plays the eternal song 'Never gonna give you up' sung by our savior Rick Astley")
      embed.add_field(name="connect4 {user_mention}", value="Starts a game of Connect4 with the requested user")
      embed.add_field(name="xo {user_mention}", value="Starts a game of Tic Tac Toe with the requested user")
      await message.channel.send(embed=embed)
  
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
async def on_member_update(before, after):
  try:
    if before.nick!=after.nick and before.id!=338128429067010050:
      await after.send(f"Congrats on your new name, although for me you'll always stay {before.nick}")
    elif after.activity is not None and after.activity!=before.activity and after.activity.name=="Among Us" and after.activity.details is None and before.activity is None:
      voice=after.voice
      if voice is not None:
        print(after.activity)
        print(after.activity.small_image_url)
        guild=voice.channel.guild
        for channel in guild.channels:
          try: 
            if str(channel.type)=='text':
              embed=discord.Embed(title="Looking for players",description=f"{after.mention} is playing Among Us, come and join him")
              embed.set_image(url = "https://cdn.cloudflare.steamstatic.com/steam/apps/945360/capsule_616x353.jpg?t=1625742109")
              await channel.send(embed=embed)
              break
          except Exception as e:
            print(e)
  except Exception as e:
    print (e)


@client.event
async def on_raw_reaction_add(payload):
  print(four_in_line)
  print(payload.emoji)
  print("hey")
  print(payload.message_id)
  if payload.message_id==872956871605096468 and payload.emoji.name=='👍':
    try:
      print("why")
      role=discord.utils.get(payload.member.guild.roles , name="verified")
      await payload.member.add_roles(role)
    except Exception as e:
      print(e)
      
  elif str(payload.message_id) in board_player and payload.user_id ==board_player[str(payload.message_id)].id:
    if payload.emoji.name=='⬇️':
      message_str=board_player[str(payload.message_id)].down()
      embed=discord.Embed(title="Mini game",colour=discord.Colour.gold(),description=message_str)
      await board_player[str(payload.message_id)].board_message.edit(embed=embed)
    elif payload.emoji.name=='⬆️':
      message_str=board_player[str(payload.message_id)].up()
      embed=discord.Embed(title="Mini game",colour=discord.Colour.gold(),description=message_str)
      await board_player[str(payload.message_id)].board_message.edit(embed=embed)
    elif payload.emoji.name=='⬅️':
      message_str=board_player[str(payload.message_id)].left()
      embed=discord.Embed(title="Mini game",colour=discord.Colour.gold(),description=message_str)
      await board_player[str(payload.message_id)].board_message.edit(embed=embed)
    elif payload.emoji.name=='➡️':
      message_str=board_player[str(payload.message_id)].right()
      embed=discord.Embed(title="Mini game",colour=discord.Colour.gold(),description=message_str)
      await board_player[str(payload.message_id)].board_message.edit(embed=embed)
    await board_player[str(payload.message_id)].board_message.remove_reaction(payload.emoji,payload.member)
  elif str(payload.message_id) in four_in_line.keys() and str(payload.user_id) in four_in_line[str(payload.message_id)].players.keys():
    print("shapahn")
    if four_in_line[str(payload.message_id)].players[str(payload.user_id)]:
      actions=four_in_line[str(payload.message_id)]
      legal=False
      if payload.emoji.name=='1️⃣':
        board_str,played=actions.playing(0)
        legal=True
      elif payload.emoji.name=='2️⃣': 
        board_str,played=actions.playing(1)  
        legal=True
      elif payload.emoji.name=='3️⃣':
        board_str,played=actions.playing(2)
        legal=True
      elif payload.emoji.name=='4️⃣':   
        board_str,played=actions.playing(3)  
        legal=True     
      elif payload.emoji.name=='5️⃣':
        board_str,played=actions.playing(4)
        legal=True
      elif payload.emoji.name=='6️⃣':
        board_str,played=actions.playing(5) 
        legal=True 
      elif payload.emoji.name=='7️⃣':  
        board_str,played=actions.playing(6)
        legal=True
      if legal:
        if played:
          if actions.check_if_over()=='no':
            name=actions.swap().name
            embed=discord.Embed(title=f"{name} turn",description=":one::two::three::four::five::six::seven:"+board_str)
            print(actions.board_message.created_at)
            game_time=datetime.datetime.now()-actions.board_message.created_at
            embed.add_field(name="Game length",value=f"{game_time.seconds//60} minutes and {game_time.seconds%60} seconds" )
            await actions.board_message.edit(embed=embed)
          elif actions.check_if_over()=='red':
            actions.over()
            embed=discord.Embed(title=f' {payload.member.name} WINS',description=":one::two::three::four::five::six::seven:"+board_str)
            game_time= datetime.datetime.now()-actions.board_message.created_at
            embed.add_field(name="Game length",value=f"{game_time.seconds//60} minutes and {game_time.seconds%60} seconds" )
            await actions.board_message.edit(embed=embed)
          elif actions.check_if_over()=='green':
            actions.over()
            embed=discord.Embed(title=f'{payload.member.name} WINS',description=":one::two::three::four::five::six::seven:"+board_str)
            game_time=datetime.datetime.now()-actions.board_message.created_at
            embed.add_field(name="Game length",value=f"{game_time.seconds//60} minutes and {game_time.seconds%60} seconds" )
            await actions.board_message.edit(embed=embed)
      await four_in_line[str(payload.message_id)].board_message.remove_reaction(payload.emoji,payload.member)
          
  elif str(payload.message_id) in tic_tac_toe.keys() and str(payload.user_id) in tic_tac_toe[str(payload.message_id)].players.keys():
    if tic_tac_toe[str(payload.message_id)].players[str(payload.user_id)]:
      actions=tic_tac_toe[str(payload.message_id)]
      legal=False
      all_emojis=['1️⃣','2️⃣', '3️⃣' , '4️⃣' , '5️⃣' , '6️⃣' , '7️⃣', '8️⃣' , '9️⃣']
      if payload.emoji.name in all_emojis:
        legal=True
        i=0
        for emoji in all_emojis:
          if payload.emoji.name==emoji:
            board_str,played=actions.playing(i)
          i+=1
      if legal:
        if played:
          
          if actions.check_if_over()=='no':
            name=actions.swap().name
            embed=discord.Embed(title=f"{name} turn",description=board_str)
            await actions.board_message.edit(embed=embed)
          elif actions.check_if_over()=='yes':
            embed=discord.Embed(title=f"TIE",description=board_str)
            await actions.board_message.edit(embed=embed)           
          elif actions.check_if_over()=='o':
            actions.over()
            embed=discord.Embed(title=f' {payload.member.name} WINS',description=board_str)
            await actions.board_message.edit(embed=embed)
          elif actions.check_if_over()=='x':
            actions.over()
            embed=discord.Embed(title=f'{payload.member.name} WINS',description=board_str)
            await actions.board_message.edit(embed=embed)
      await tic_tac_toe[str(payload.message_id)].board_message.remove_reaction(payload.emoji,payload.member)

@client.event
async def on_voice_state_update(member,before,after):
  if member.id==290227755415502849 and before.channel is None and after.channel is not None:
    print("a")
   # await member.send("https://www.youtube.com/watch?v=fGDQ9IukMOc")
@client.event
async def on_typing(channel, user, when):
  if str(user.id)==os.environ['OMRI'] and omri_dig[0]:
    await channel.send("עמרי מקליד אז סתמו")
    omri_dig[0]=False
    await asyncio.sleep(30)
    omri_dig[0]=True


keep_alive()
client.run(TOKEN)





