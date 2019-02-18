import discord

def What(message):
    if message.content.startswith('!hello') or message.content.startswith('!Hello'): #User used hello command
        What = hello(message)
    if message.content.startswith('Quote: '):                                        #User used Quote command
        What = Quote(message)
    return What


def Where(message):                                                                 #Allows specific channel replies
    if message.content.startswith('Quote: '):
        Where = discord.Object(id='')                                               #Quotes go into a special channel
    if not message.content.startswith('Quote: '):
        Where = message.channel                                                     #All other messages reply in the same channel
    return Where

def hello(message):                                                                 #Reply to a user with Hello [user name]
    msg = 'Hello {0.author.mention}'.format(message)
    return msg

def Quote(message):                                                                 #Replies the message sent, but in a different channel
    msg = message.content
    msg = msg.replace('Quote: ', '')
    return msg
