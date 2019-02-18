import discord
import os

def What_Is(message):
    FileName = message.content
    FileName = FileName.replace('!WhatIs ', '')
    FileName = 'BotFiles\\bin\\' + FileName + '.txt'
    File = open(FileName, 'r')
    FileText = File.read()
    msg = FileText.format(message)
    return msg