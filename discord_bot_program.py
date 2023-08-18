import discord
import asyncio
import openpyxl
import requests
import time
from discord.ext import commands
import pandas as pd
import datetime
import threading
#from requestHandler import requestHandler

queue = None
intents = discord.Intents.all()
#client = discord.Client(intents=intents)
#client.run('MTEwMzExMjE0OTg1OTA0MTMyMw.GdebuH.QyDdrHDUR8aTg1Ll-OvPd7l5Gv-_uF4vNrYnq4')

#guild = discord.Guild
botCode = 'MTEwMzExMjE0OTg1OTA0MTMyMw.GdebuH.QyDdrHDUR8aTg1Ll-OvPd7l5Gv-_uF4vNrYnq4'
changeChannelId = 1103118015526088804
#promoAlertChannelId = 1104544342976233482
promoChannelId = 1103119812697268235
promoAlertChannelId = 1140813460993736704


startTime = datetime.time(hour=5, minute=45)
endTime = datetime.time(hour=22, minute=0)
link = ''

bot = commands.Bot(command_prefix='!',intents=intents)
bot.case_insensitive = True

listExcelSheets = ['disclaimer.topstocktipsAA.xlsx','secretstockalerts.xlsx']


@bot.event
async def on_ready():
    print('Logged in as {0.user}'.format(bot))


def run_discord_bot(queue_ref):
    global queue
    queue = queue_ref

    loop = asyncio.get_event_loop()
    loop.create_task(discord_background_task())
    loop.run_until_complete(bot.start(botCode))



async def discord_background_task():
    while True:
        if not queue.empty():
            text = queue.get()
            await send_promo_alert(text)

        await asyncio.sleep(1)  #adjust this duration as needed



async def send_promo_alert(text):
    promoChannel = bot.get_channel(promoAlertChannelId)
    await promoChannel.send(text)





#@bot.event
#async def on_message(message):
#    #Ignore messages sent by bot itself
#    if message.author.bot:
#        return
#    
#    if message.content.startswith(bot.command_prefix):
#        # Convert the command to lowercase before processing it
#        command = message.content.split()[0].lower()
#        # Remove the command prefix to get the command name
#        command_name = command[len(bot.command_prefix):]
#        # Get the command object from the bot
#        command_obj = bot.commands.get(command_name)
#        # If the command exists, invoke it with the message context
#        if command_obj:
#            await bot.invoke(command_obj, message)
#
#    # Let the bot process other messages as usual
#    await bot.process_commands(message)

    
@bot.command(name='changeLink')
async def changeLink(context):
    def check(m):
        return m.channel == context.channel and m.author == context.author

    try:
        global link
        await context.send("Enter a new link you'd like to add. Put a $ instead of the two letter code. E.x. https://www.disclaimer.topstocktips.com/$")
        link = await bot.wait_for('message', timeout=30.0, check=check)
        newLink= link.content
        writeToFile(newLink, 'linkList.txt')
        await context.send(f'Link has been updated to: {newLink}')
    except asyncio.TimeoutError:
        context.send('Timeout has occured. Try again')
        # Save the link to a file
        #newLink = link.content
        #await context.send(f'Link has been updated to: {newLink}')



@bot.command()
async def viewCurrentLinks(context):
    def check(m):
        return m.channel == context.channel and m.author == context.author
    



    

def writeToFile(text, filename):
    with open(filename, 'a+') as file:
        file.seek(0)
        content = file.read()
        if text not in content:
            file.write('\n' + text)


def stringInFile(text, filename):
    with open(filename, 'r') as file:
        content = file.read()
        if text in content:
            return True
        else:
            return False





# Enable command suggestions
bot.remove_command('help')
@bot.event
async def on_command_error(context, error):
    if isinstance(error, commands.CommandNotFound):
        await context.send('Command not found. Type !help for a list of available commands.')



