import asyncio
import discord
from discord.ext import commands
import traceback
import sys
sys.path.insert(0, '../libcurrency')
import libcurrency

botToken = '' # Insert bot token here

bot = commands.Bot(command_prefix='$', description='Higgsbot')

currency = libcurrency.Token()


if __name__ == '__main__':
    try:
        bot.load_extension("money")
    except Exception as e:
        print(f'Failed to load extension.', file=sys.stderr)
traceback.print_exc()

if __name__ == '__main__':
    try:
        bot.load_extension("general")
    except Exception as e:
        print(f'Failed to load extension.', file=sys.stderr)
traceback.print_exc()

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