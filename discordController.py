import discord
import asyncio
import openpyxl
import requests
import time

from discord.ext import commands


intents = discord.Intents.all()
#client = discord.Client(intents=intents)
#client.run('MTEwMzExMjE0OTg1OTA0MTMyMw.GdebuH.QyDdrHDUR8aTg1Ll-OvPd7l5Gv-_uF4vNrYnq4')

#guild = discord.Guild

changeChannelId = 1103118015526088804
promoChannelId = 1103119812697268235
link = ''

bot = commands.Bot(command_prefix='!',intents=intents)

listExcelSheets = ['disclaimer.topstocktipsAA.xlsx','secretstockalerts.xlsx']

async def excelController():
    stockTipsLink = openpyxl.load_workbook(listExcelSheets[0])
    secretStockAlerts = openpyxl.load_workbook(listExcelSheets[1])
    counter = 0
    while True:
        responseStockTips = requests.get(stockTipsLink)
        responseSecretStockAlerts = requests.get(secretStockAlerts)

    





@bot.event
async def on_ready():

    print('bot is ready!')
    


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
    


# Convert all commands to lowercase before processing them
bot.case_insensitive = True

# Enable command suggestions
bot.remove_command('help')
@bot.event
async def on_command_error(context, error):
    if isinstance(error, commands.CommandNotFound):
        await context.send('Command not found. Type !help for a list of available commands.')




async def main():
    await bot.start('MTEwMzExMjE0OTg1OTA0MTMyMw.GdebuH.QyDdrHDUR8aTg1Ll-OvPd7l5Gv-_uF4vNrYnq4')
    await excelController()



asyncio.run(main())