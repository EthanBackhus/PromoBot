import discord


intents = discord.Intents.all()
client = discord.Client(intents=intents)
guild = discord.Guild


@client.event
async def on_ready():
    query_v2(tickers)
    print('bot is ready!')
    #default_channel = discord.utils.get(client.guilds[0].channel, name='mastersheetbot')
    #await  default_channel.channel.send("Data synced to Mastersheet")


@client.event
async def on_message(message):
    #default_channel = discord.utils.get(client.guilds[0].channel, name='mastersheetbot')

    channel = client.get_channel(1074828421781274727)

    if message.author == client.user:
        return
    else:
        message_str = str(message.content)
        current_tickers = get_tickers()
        #print(f'message_str is: {message_str}')
        possibleTickers = four_letters(message_str)
        tickersToAdd = []
        for possibleTicker in possibleTickers:
            if possibleTicker not in current_tickers:
                tickersToAdd.append(possibleTicker)


        #print(f'tickers to add: {tickersToAdd}')
        if(len(tickersToAdd) != 0):
            queryTicker(tickersToAdd)
            await channel.send(f"Added data for {tickersToAdd}")


            client.run('MTA3NDgxNTAzOTEyODc1MjE3MA.G9jMeg.jpAj-JS_NCWZYEce4XsezF27bYCPSxF8s6h1Ic')