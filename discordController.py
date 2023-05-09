import discord
import asyncio
import openpyxl
import requests
import time
from discord.ext import commands
import pandas as pd
#from requestHandler import requestHandler


intents = discord.Intents.all()
#client = discord.Client(intents=intents)
#client.run('MTEwMzExMjE0OTg1OTA0MTMyMw.GdebuH.QyDdrHDUR8aTg1Ll-OvPd7l5Gv-_uF4vNrYnq4')

#guild = discord.Guild

changeChannelId = 1103118015526088804
promoAlertChannelId = 1104544342976233482
promoChannelId = 1103119812697268235
link = ''

bot = commands.Bot(command_prefix='!',intents=intents)

listExcelSheets = ['disclaimer.topstocktipsAA.xlsx','secretstockalerts.xlsx']

async def excelController():
    dfStockTips = pd.read_excel(listExcelSheets[0], sheet_name='Sheet1')
    dfSecretStockAlerts = pd.read_excel(listExcelSheets[1], sheet_name='Sheet1')
    index = 0
    
    interrupt = False
    while(interrupt == False):
        if(index == 676):
            index = 0

        linkStockTips = dfStockTips.iloc[index,0]
        linkSecertAlerts = dfSecretStockAlerts.iloc[index,0]

        temp = index
        duplicate = False

        # check to see if link has already been hit
        if(stringInFile(linkStockTips, 'listKnownHits.txt')):
            temp +=1

        responseStockTips = requests.get(linkStockTips)
        responseSecretStockAlerts = requests.get(linkSecertAlerts)
        time.sleep(0.05)

        if(responseStockTips.status_code == 200 or responseSecretStockAlerts.status_code == 200):
            sendPromoAlert()
            if(responseStockTips.status_code == 200):
                writeToFile(linkStockTips, 'listKnownHits.txt')
                print(f"We got a hit on {linkStockTips}")
            elif(responseSecretStockAlerts.status_code == 200):
                print(f"We got a hit on {linkSecertAlerts}")
            interrupt = True
        else:
            index+=1
            print(f"Miss on {linkStockTips}, index = {index}")

        

@bot.event
async def on_ready():

    print('bot is ready!')
    await excelController()
    


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
    



async def sendPromoAlert():
    promoChannel = bot.get_channel(1104544342976233482)
    await promoChannel.send("ALERT!")

    

async def writeToFile(text, filename):
    with open(filename, 'a+') as file:
        file.seek(0)
        content = file.read()
        if text not in content:
            file.write('\n' + text)


async def stringInFile(text, filename):
    with open(filename, 'r') as file:
        content = file.read()
        if text in content:
            return True
        else:
            return False



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



asyncio.run(main())

#asyncio.run(writeToFile('https://www.secretstockalerts.com/AA', 'listKnownHits.txt'))