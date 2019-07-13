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
    #async def code(self, ctx, b:int, lang:str, *, code:str):
    async def code(self, ctx, lang:str, *, code:str):
        """Use this command to execute your code."""
        c = currency.check_balance(ctx.message.author)
        if c > 0:
            r = container.run_code(lang, code)
            currency.remove_balance(ctx.message.author, 1)
            if r.chroot == False:
                chr = "NOCHROOT"
            else:
                chr = "CHROOT"
            if r.cr == "":
                clr = 0xff0000
            else:
                clr = 0x25df20
            if r.ccr == "":
                embed=discord.Embed(title="Results of language {}".format(lang), color=clr)
                embed.set_author(name=self.bot.user.display_name, url=self.bot.user.avatar_url, icon_url=self.bot.user.avatar_url)
                embed.add_field(name="Compiled using:", value="```{}```".format(r.cc), inline=False)
                embed.add_field(name="Result:", value="```{}```".format(r.cr), inline=False)
                embed.set_footer(text="{} | {} | {}".format(r.uuid, host, chr))
            else:
                embed=discord.Embed(title="Results of language {}".format(lang), color=clr)
                embed.set_author(name=self.bot.user.display_name,url=self.bot.user.avatar_url,icon_url=self.bot.user.avatar_url)
                embed.add_field(name="Compiled using:", value="```{}```".format(r.cc), inline=False)
                embed.add_field(name="Compiler Result:", value="```{}```".format(r.ccr), inline=False)
                if r.cr == "":
                    embed.add_field(name="Result:", value="No output binary could be found.".format(r.cr), inline=False)
                else:
                    embed.add_field(name="Result:", value="```{}```".format(r.cr), inline=False)
                embed.set_footer(text="{} | {} | {}".format(r.uuid, host, chr))
            await ctx.send(embed=embed)
        else:
            if c != 0:
                await ctx.send("You don't have enough coins.\n You only have {} coins.".format(c))
            else:
                await ctx.send("You don't have enough coins.\n You don't have any coins.")

    @code.error
    async def code_error(self, ctx, error):
        error = getattr(error, 'original', error)
        if isinstance(error, commands.BadArgument):
            embed=discord.Embed(title="Error!", description="Unknown argument type or bad argument.", color=0xfd0000)
            embed.add_field(name="Proper usage:", value="```{}code <amount CodeTokens> <language> <code>```".format(ctx.prefix), inline=True)
            embed.set_footer(text="HiggsBot - A code executing Discord bot!")
        if isinstance(error, commands.MissingRequiredArgument):
            embed=discord.Embed(title="Error!", description="Missing argument.", color=0xfd0000)
            embed.add_field(name="Proper usage:", value="```{}code <amount CodeTokens> <language> <code>```".format(ctx.prefix), inline=True)
            embed.set_footer(text="HiggsBot - A code executing Discord bot!")
        await ctx.send(embed=embed)


        

def setup(bot):
    bot.add_cog(Containers(bot))