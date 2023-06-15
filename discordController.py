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


intents = discord.Intents.all()
#client = discord.Client(intents=intents)
#client.run('MTEwMzExMjE0OTg1OTA0MTMyMw.GdebuH.QyDdrHDUR8aTg1Ll-OvPd7l5Gv-_uF4vNrYnq4')

#guild = discord.Guild
botCode = 'MTEwMzExMjE0OTg1OTA0MTMyMw.GdebuH.QyDdrHDUR8aTg1Ll-OvPd7l5Gv-_uF4vNrYnq4'
changeChannelId = 1103118015526088804
promoAlertChannelId = 1104544342976233482
promoChannelId = 1103119812697268235

startTime = datetime.time(hour=5, minute=45)
endTime = datetime.time(hour=22, minute=0)
link = ''

bot = commands.Bot(command_prefix='!',intents=intents)


listExcelSheets = ['disclaimer.topstocktipsAA.xlsx','secretstockalerts.xlsx']

async def excelController():
    print("Testing!")

    dfStockTips = pd.read_excel(listExcelSheets[0], sheet_name='Sheet1')
    dfSecretStockAlerts = pd.read_excel(listExcelSheets[1], sheet_name='Sheet1')
    index = 0
    
    interrupt = False

    #check to see if the time is right to run
    currentTime = datetime.datetime.now().time()
    if currentTime >= startTime and currentTime <= endTime:
        #run the loop
        ########################################################################################
        while(interrupt == False):

            if(index == 676):
                index = 0

            linkStockTips = dfStockTips.iloc[index,0]
            linkSecertAlerts = dfSecretStockAlerts.iloc[index,0]

            ## TEMP ####################################
            #responseStockTips = requests.get(linkStockTips)
            #responseSecretStockAlerts = requests.get(linkSecertAlerts)
            responseStockTips = 404
            responseSecretStockAlerts = 404

            if(linkStockTips == 'https://www.disclaimer.topstocktips.com/jf'):
                responseStockTips = 200
            else:
                responseStockTips = 404

            
            ## TEMP ####################################
            

            #time.sleep(0.05)
            await asyncio.sleep(0.05)

            if(responseStockTips == 200 or responseSecretStockAlerts == 200):
                #sendPromoAlert()
                if(responseStockTips == 200):
                    if(stringInFile(linkStockTips, 'listKnownHits.txt') == False):
                        writeToFile(linkStockTips, 'listKnownHits.txt')
                        print(f"We got a hit on {linkStockTips}")

                        process = await asyncio.create_subprocess_exec()

                        await sendPromoAlert("test!!!")
                        interrupt = True
                elif(responseSecretStockAlerts == 200):
                    if(stringInFile(linkSecertAlerts, 'listKnownHits.txt') == False):
                        writeToFile(linkSecertAlerts, 'listKnownHits.txt')
                        print(f"We got a hit on {linkSecertAlerts}")
                        await sendPromoAlert("test!!!!")
                        interrupt = True
            else:
                index+=1
                print(f"Miss on {linkStockTips}, {linkSecertAlerts}, index = {index}")
            ########################################################################################
    else:
        # wait until tomorrow
        tomorrow = datetime.datetime.now() + datetime.timedelta(days = 1)
        tomorrowStartTime = datetime.datetime.combine(tomorrow.date(), startTime)
        time.sleep((tomorrowStartTime - datetime.datetime.now()).seconds)

    

        

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
    



async def sendPromoAlert(text):
    promoChannel = bot.get_channel(1104544342976233482)
    await promoChannel.send(f"ALERT! New Promo: {text}")

    

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



# Convert all commands to lowercase before processing them
bot.case_insensitive = True

# Enable command suggestions
bot.remove_command('help')
@bot.event
async def on_command_error(context, error):
    if isinstance(error, commands.CommandNotFound):
        await context.send('Command not found. Type !help for a list of available commands.')



async def botController():
    await bot.start(botCode)



async def excelRunner():
    await excelController()



async def main():
    #discordTask = asyncio.create_task(botController())
    #excelTask = asyncio.create_task(excelRunner())
    #await asyncio.gather(discordTask, excelTask)
    await asyncio.gather(botController(), excelRunner())




if __name__ == '__main__':
    asyncio.run(main())