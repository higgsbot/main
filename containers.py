import discord
from discord.ext import commands
import libcurrency
import socket
import container

currency = libcurrency.Token()
host = socket.gethostname()

class Containers(commands.Cog, name="Container Plugin"):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='code')
    async def code(self, ctx, lang:str, *, code:str):
        c = currency.check_balance(ctx.message.author)

        r = container.run_code(lang, code)
        if r.ccr == "":
            embed=discord.Embed(title="{} Results".format(lang), color=0xee6d20)
            embed.add_field(name="Result:", value="```{}```".format(r.cr), inline=False)
            embed.set_footer(text="{} | {} | NOCHROOT".format(r.uuid, host))
        else:
            embed=discord.Embed(title="{} Results".format(lang), color=0xee6d20)
            embed.add_field(name="Compiler Result:", value="```{}```".format(r.ccr), inline=False)
            embed.add_field(name="Result:", value="```{}```".format(r.cr), inline=False)
            embed.set_footer(text="{} | {} | NOCHROOT".format(r.uuid, host))
        await ctx.send(embed=embed)


        

def setup(bot):
    bot.add_cog(Containers(bot))