import discord
from discord.ext import commands
import libcurrency.libcurrency as libcurrency
import socket
import libcontainer.container as container

currency = libcurrency.Token()
host = socket.gethostname()

class Containers(commands.Cog, name="Container Plugin"):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='code')
    async def code(self, ctx, b:int, lang:str, *, code:str):
        """Use this command to execute your code."""
        c = currency.check_balance(ctx.message.author)
        if c >= b:
            a = b * 5
            r = container.run_code(lang, code, a)
            currency.remove_balance(ctx.message.author, b)
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
        else:
            if c != 0:
                await ctx.send("You don't have enough coins.\n You only have {} coins.".format(c))
            else:
                await ctx.send("You don't have enough coins.\n You don't have any coins.")


        

def setup(bot):
    bot.add_cog(Containers(bot))