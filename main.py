import discord
from discord.ext import commands
import logging
import os
import datetime
#from datetime import date
from custommsg.welcomemessage import getwelcomemsg
from custommsg.helpmsg import gethelpmsg
from logger.loggerfunctions import startlogger
#startlogger(logging.DEBUG)
startlogger()

intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix="$", intents = intents)

############
# Commands #
############
pingbrief = "Useless, unless your a developer who likes crashing your own program :p"
@bot.command(brief=pingbrief)
async def ping(context): #for testing
  await context.channel.send('pong')

scuttlebrief = "Scuttle (verb): to sink or attempt to sink a ship, wreck, destroy"
@bot.command(brief=scuttlebrief)
async def scuttlethebot(context): #
  await context.channel.send('HAHAHAHA! Nice try. Come back when you know what sudo means. \n-Archer')

##########
# Events #
##########
@bot.event
async def on_ready():
  print('Logged in as {0.user}'.format(bot))
  #today = date.today()
  #print('{0}'.format(today))

"""
@client.event
async def on_reminder(channel_id, author_id, text):
    channel = client.get_channel(channel_id)

    await channel.send("Hey, <@{0}>, remember to: {1}".format(author_id, text))
"""

@bot.event
async def on_member_join(member):
  channel = member.guild.system_channel
  if channel is not None:
    greeting = getwelcomemsg(member)
    await channel.send('{0}'.format(greeting))

#@bot.event
#async def on_message(message):
#  if message.author == bot.user:
#    return
#
#  if message.content.startswith('hello {0}'.format(bot.user)):
#    await message.channel.send('Hello {0}!'.format(message.author.mention))
#  await bot.process_commands(message) # needed else discord.ext::commands breaks

bot.run(os.getenv('TOKEN'))