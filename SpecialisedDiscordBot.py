#In your Python terminal, add the directory path for BotFiles using:
#include sys
#sys.path.append('#path#//BotFiles')


import os
import importlib
import discord
import random
import ctypes
from BotFiles import DiceRoller

client = discord.Client()


@client.event
#accept user text input
async def  on_message(message) :
    if message.author == client.user:
        return
    if message.content.startswith('!hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)

    #Quote channel system
    if message.content.startswith('Quote: '):
        msg = message.content
        msg = msg.replace('Quote: ', '')
        await client.send_message(discord.Object(id=''), msg)

    #roll dice. Edit away from message object to string
    if message.content.startswith('!roll '):
        Score = DiceRoller.Roll_Dice(message)
        endsum = Score[len(Score)-1]
        Score.remove(endsum)
        await client.send_message(message.channel, str(endsum))
        await client.send_message(message.channel, str(Score))
        
        #add "import [module]" and unload commands
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('-------')

client.run('')