import asyncio
import discord
from discord.ext import commands
import traceback
import sys
sys.path.insert(0, '../libcurrency')
import libcurrency.libcurrency as libcurrency

try:
    tkn = open("token.txt","r").readline()
except:
    print("Token file does not exist!")
    open("token.txt","w+")
    print("Token file created. Add your token to it.")
    exit()

botToken = tkn.strip()
bot = commands.Bot(case_insensitive=True, command_prefix='$', description='Higgsbot')
currency = libcurrency.Token()

extensions = ['money',
              'general',
              'containers']

if __name__ == '__main__':
    for extension in extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            print(f'Failed to load extension {extension}.', file=sys.stderr)
            traceback.print_exc()

@bot.event
async def on_ready():
	await currency.start(bot)
	print('Logged in as {}, {}'.format(bot.user.name, bot.user.id))
	await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="$help for help"))
	print('login success')
	print('...')

@bot.listen
async def on_member_join(member):
	currency.join(member)

bot.run(botToken, bot=True, reconnect=True)