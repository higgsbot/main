import discord
from discord.ext import commands
import libcurrency.libcurrency as libcurrency

currency = libcurrency.Token()

class Money(commands.Cog, name="Cash Test"):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='balance')
    async def balance(self, ctx, user:discord.Member = None):
        "Shows the balance of the member mentioned, or message creator."
        if user is None:
            user = ctx.message.author
        await ctx.send("The balance of user {} is {}.".format(user.display_name, currency.check_balance(user)))

    @commands.command(name='remove')
    async def remove(self, ctx, user:discord.Member, nr:int):
        """Removes currency from a user. Owner only"""
        currency.remove_balance(user, nr)
        await ctx.send("{} CodeTokens has been removed from user {}!".format(nr, user.display_name))

    @commands.command(name='set')
    async def set(self, ctx, user:discord.Member, nr:int):
        """Sets a user's currency. Owner only"""
        currency.set_balance(user, nr)
        await ctx.send("CodeTokens has been set to {} for user {}!".format(nr, user.display_name))

def setup(bot):
    bot.add_cog(Money(bot))