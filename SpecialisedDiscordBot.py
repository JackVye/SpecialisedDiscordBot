
import discord
import random
import ctypes

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

    #roll dice
    if message.content.startswith('!roll '):
        result = 0
        msg = message.content
        msg = msg.replace('!roll ', '')
        msgList = msg.split('+')
        Score = []
        ScoreTicker = 0
        x=0
        endsum = 0
        while x < len(msgList):
            rollFragment= msgList[x].split('d')
            if len(rollFragment) == 1:
                endsum += int(msgList[x])
                Score.append(int(msgList[x]))
                ScoreTicker+=1
            if len(rollFragment)== 2:
                i=0
                while i < int(rollFragment[0]):
                    dice = random.randint(1,int(rollFragment[1]))
                    endsum += dice
                    Score.append(dice)
                    ScoreTicker+=1
                    i+=1
            if len(rollFragment)==3:
                i=0
                while i < int(rollFragment[0])-int(rollFragment[2]):
                    dice = random.randint(1,int(rollFragment[1]))
                    endsum += dice
                    Score.append(dice)
                    ScoreTicker+=1
                    i+=1
                i=0
                while i < int(rollFragment[2]):
                    dice = random.randint(1,int(rollFragment[1]))
                    dropped=false
                    while j < int(rollFragment[0])-int(rollFragment[2]):
                        if dice > Score[ScoreTicker-int(rollFragment[0])+j]&dropped==false:
                            Score[ScoreTicker-int(rollFragment[0])+j]=dice
                            dropped = true
                    i+=1
        endCalc = 0
        while endCalc < ScoreTicker:
            msg = msg + str(Score) + ' ' 
            endCalc+=1
        print = msg.format(message)
        await client.send_message(message.channel, print)
        print = 'Total: ' + string(endsum)
        print = msg.format(message)
        await client.send_message(message.channel, print)
        x+=1

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('-------')

client.run('')