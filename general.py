import discord
from discord.ext import commands

class General(commands.Cog, name="General Commands"):
	def __init__(self, bot):
		self.bot = bot

	@commands.command(name='hello')
	async def hello(self, ctx):
		"Hello World!"
		await ctx.send('Hello World!')

	@commands.command(name='spitback')
	async def spitback(self, ctx, arg: str):
		"Responds with your text."
		await ctx.send(arg)

	@commands.command(name='readme')
	async def readme(self,ctx):
		"Print a simple readme"
		f = open("help.txt", "r")
		await ctx.send(f.read())
		f.close()

def setup(bot):
	bot.add_cog(General(bot))