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

	@spitback.error
	async def spitback_error(self, ctx, error):
		error = getattr(error, 'original', error)
		if isinstance(error, commands.BadArgument):
			embed=discord.Embed(title="Error!", description="Unknown argument type or bad argument.", color=0xfd0000)
			embed.add_field(name="Proper usage:", value="```{}spitback <message>```".format(ctx.prefix), inline=True)
			embed.set_footer(text="HiggsBot - A code executing Discord bot!")
		if isinstance(error, commands.MissingRequiredArgument):
			embed=discord.Embed(title="Error!", description="Missing argument.", color=0xfd0000)
			embed.add_field(name="Proper usage:", value="```{}spitback <message>```".format(ctx.prefix), inline=True)
			embed.set_footer(text="HiggsBot - A code executing Discord bot!")
		await ctx.send(embed=embed)

	@commands.command(name='readme')
	async def readme(self,ctx):
		"Print a simple readme"
		f = open("help.txt", "r")
		await ctx.send(f.read())
		f.close()

def setup(bot):
	bot.add_cog(General(bot))