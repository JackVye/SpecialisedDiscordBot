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
        endsum = 0                      #the answer at the end
        constant = 0                    #the sum total of constants entered
        while x < len(msgList):
            rollFragment= msgList[x].split('d')			
            if len(rollFragment) == 1:
                #If the length of the list is 1, the calculation was + [int] so just add the given number
                endsum += int(msgList[x])
                constant += int(msgList[x])
            if len(rollFragment)== 2:
                #If length of list is 2, the operation was [int1]d[int2] so we roll [int2] sided dice [int1] times
                i=0
                while i < int(rollFragment[0]):
                    dice = random.randint(1,int(rollFragment[1]))
                    endsum += dice                  #add roll value to the final sum
                    display = str(dice) + '/' + str(rollFragment[1])
                    Score.append(display)           #and add the specific value to the list of rolls
                    i+=1
            x+=1
            if len(rollFragment)==3:
                #If the list length is 3, the operation was [int1]d[int2]d[int3]. roll [int1] dice [int2] times and drop the [int3] lowest
                i=0
                DiceDropper=[]                      #remember which dice were rolled sepirately

                while i < int(rollFragment[0]):     #roll [int1] dice
                    dice = random.randint(1,int(rollFragment[1]))
                    DiceDropper.append(dice)
                    i+=1
                i=0

                while i < int(rollFragment[2]):     #drop the lowest [int3] dice
                    DiceDropper.remove(min(DiceDropper))
                    i+=1
                i=0
                
                while i < len(DiceDropper):
                    display = str(DiceDropper[i]) +'/'+ str(rollFragment[1])
                    Score.append(display)
                    i+=1
     
                i=0
                while i < len(DiceDropper):
                    endsum+=DiceDropper[i]          #and add their values to the final sum
                    i+=1
        endCalc = 0
        msg = str(endsum) + ' ' + str(Score) + ' + ' + str(constant)
        msg = msg.replace("'",'') 
        msg = msg.replace(', ', '] [')
        msg = msg.format(message)
        return msg