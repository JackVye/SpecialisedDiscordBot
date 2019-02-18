import discord
import random
import ctypes

def Roll_Dice(message):
		#the command accepts the parameter !roll and then any combination of [int], [int]d[int] and [int]d[int]d[int]
		#additions will include subtraction and [int]d[int]r[int]
        msg = message.content
        msg = msg.replace('!roll', '')  #remove the command line
        msg = msg.replace(' ', '')      #remove any spaces
        msgList = msg.split('+')        #split the string into sepirate commands
        Score = []                      #create the sepirate dice results box						
        x=0
        endsum = 0
        while x < len(msgList):
            rollFragment= msgList[x].split('d')			
            if len(rollFragment) == 1:
                endsum += int(msgList[x])
                Score.append(int(msgList[x]))
            if len(rollFragment)== 2:
                i=0
                while i < int(rollFragment[0]):
                    dice = random.randint(1,int(rollFragment[1]))
                    endsum += dice
                    Score.append(dice)
                    i+=1
            x+=1
            if len(rollFragment)==3:
                i=0
                DiceDropper=[]
                while i < int(rollFragment[0])-int(rollFragment[2]):
                    dice = random.randint(1,int(rollFragment[1]))
                    DiceDropper.append(dice)
                    i+=1
                i=0
                while i < int(rollFragment[2]):
                    dice = random.randint(1,int(rollFragment[1]))
                    if min(DiceDropper) < dice:
                        DiceDropper.remove(min(DiceDropper))
                        DiceDropper.append(dice)
                    i+=1
                Score.append(DiceDropper)
                i=0
                while i < len(DiceDropper):
                    endsum+=DiceDropper[i]
                    i+=1
        endCalc = 0
        Score.append(endsum)
        return Score