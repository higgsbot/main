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

    @balance.error
    async def balance_error(self, ctx, error):
        error = getattr(error, 'original', error)
        if isinstance(error, commands.BadArgument):
            embed=discord.Embed(title="Error!", description="Unknown argument type or bad argument.", color=0xfd0000)
            embed.add_field(name="Proper usage:", value="```{}balance [user]```".format(ctx.prefix), inline=True)
            embed.set_footer(text="HiggsBot - A code executing Discord bot!")
        await ctx.send(embed=embed)

    @commands.command(name='remove')
    async def remove(self, ctx, user:discord.Member, nr:int):
        """Removes currency from a user. Owner only"""
        if owner(ctx) is 1:
            currency.remove_balance(user, nr)
            await ctx.send("{} CodeToken(s) has been removed from user {}!".format(nr, user.display_name))
        else:
            await ctx.send("You are not my owner.")

    @remove.error
    async def remove_error(self, ctx, error):
        error = getattr(error, 'original', error)
        if isinstance(error, commands.BadArgument):
            embed=discord.Embed(title="Error!", description="Unknown argument type or bad argument.", color=0xfd0000)
            embed.add_field(name="Proper usage:", value="```{}remove <user> <amount>```".format(ctx.prefix), inline=True)
            embed.set_footer(text="HiggsBot - A code executing Discord bot!")
        if isinstance(error, commands.MissingRequiredArgument):
            embed=discord.Embed(title="Error!", description="Missing argument.", color=0xfd0000)
            embed.add_field(name="Proper usage:", value="```{}remove <user> <amount>```".format(ctx.prefix), inline=True)
            embed.set_footer(text="HiggsBot - A code executing Discord bot!")
        await ctx.send(embed=embed)

    @commands.command(name='set')
    async def set(self, ctx, user:discord.Member, nr:int):
        """Sets a user's currency. Owner only"""
        if owner(ctx) is 1:
            currency.set_balance(user, nr)
            await ctx.send("CodeTokens has been set to {} for user {}!".format(nr, user.display_name))
        else:
            await ctx.send("You are not my owner.")

    @set.error
    async def set_error(self, ctx, error):
        error = getattr(error, 'original', error)
        if isinstance(error, commands.BadArgument):
            embed=discord.Embed(title="Error!", description="Unknown argument type or bad argument.", color=0xfd0000)
            embed.add_field(name="Proper usage:", value="```{}set <user> <amount>```".format(ctx.prefix), inline=False)
            embed.set_footer(text="HiggsBot - A code executing Discord bot!")
        if isinstance(error, commands.MissingRequiredArgument):
            embed=discord.Embed(title="Error!", description="Missing argument.", color=0xfd0000)
            embed.add_field(name="Proper usage:", value="```{}set <user> <amount>```".format(ctx.prefix), inline=False)
            embed.set_footer(text="HiggsBot - A code executing Discord bot!")
        await ctx.send(embed=embed)

def owner(ctx):
    if str(ctx.message.author.id) in str(check()):
        a = 1
    else:
        a = 0
    return a

def check():
    try:
        f = open("owner.txt", "r").readline().split(",")
    except:
        print("Owner file does not exist!") 
        open("owner.txt","w+")
        print("Owner file created. Add your owner user ID to it.")
        exit()
    return f

def setup(bot):
    check()
    bot.add_cog(Money(bot))