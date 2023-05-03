import discord

from discord.ext import commands


intents = discord.Intents.all()
#client = discord.Client(intents=intents)
#client.run('MTEwMzExMjE0OTg1OTA0MTMyMw.GdebuH.QyDdrHDUR8aTg1Ll-OvPd7l5Gv-_uF4vNrYnq4')

#guild = discord.Guild

changeChannelId = 1103118015526088804
promoChannelId = 1103119812697268235
link = ''

bot = commands.Bot(command_prefix='!', intents=intents)




@bot.event
async def on_ready():
    print('bot is ready!')
    

#@bot.event
#async def on_message(message):


    


@bot.command(name='changeLink')
async def changeLink(context):
    def check(m):
        return m.channel == context.channel and m.author == context.author


    try:
        global link
        await context.send("Enter a new link you'd like to add. Instead of putting a two letter code, put a $ instead:")
        link = await bot.wait_for('message', timeout=30.0, check=check)
    except asyncio.TimeoutError:
        # Save the link to a file
        newLink = link.content
        await context.send(f'Link has been updated to: {newLink}')


@bot.command(name='viewLinks')
async def viewCurrentLinks(context):
    def check(m):
        return m.channel == context.channel and m.author == context.author
    





bot.run('MTEwMzExMjE0OTg1OTA0MTMyMw.GdebuH.QyDdrHDUR8aTg1Ll-OvPd7l5Gv-_uF4vNrYnq4')