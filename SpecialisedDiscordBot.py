#In your Python terminal, add the directory path for BotFiles using:
#include sys
#sys.path.append('#path#//BotFiles')


import os
import importlib
import discord
import random
import ctypes
from BotFiles import DiceRoller
from BotFiles import GM
from BotFiles import Remember

client = discord.Client()


@client.event
#accept user text input
#output is handled in main because it requires a client interraction
async def  on_message(message) :
    Where = GM.Where(message)                       #Where works for any case

    if message.content.startswith('!roll '):        #special case for rolling a dice
        What = DiceRoller.Roll_Dice(message)
    if message.content.startswith('!WhatIs '):
        What = Remember.What_Is(message)
    if not (message.content.startswith('!roll ') or message.content.startswith('!WhatIs ')):    #for all other messages
        What = What(message)

    await client.send_message(Where, What)          #send reply

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('-------')

client.run('')