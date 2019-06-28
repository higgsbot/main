import asyncio
import discord
from discord.ext import commands
import traceback
import sys
sys.path.insert(0, '../libcurrency')
import libcurrency.libcurrency as libcurrency

botToken = 'NTkzNTYxNTY3MjE2NTMzNTI4.XRPrxg.4wSQ6ghm3ITje8F2nrezOR3Y-nU' # Insert bot token here

bot = commands.Bot(command_prefix='$', description='Higgsbot')

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

@bot.event
async def on_ready():
	await currency.start(bot)
	print('Logged in as {}, {}'.format(bot.user.name, bot.user.id))
	print('login success')
	print('...')

@bot.listen
async def on_member_join(member):
	currency.join(member)

bot.run(botToken, bot=True, reconnect=True)