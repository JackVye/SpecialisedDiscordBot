    def General_Messages(string):
	if message.author == client.user:
        return
    if message.content.startswith('!hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
    #Quote channel system
    if message.content.startswith('Quote: '):
        msg = message.content
        msg = msg.replace('Quote: ', '')
        await client.send_message(discord.Object(id='335883609690996736'), msg)
