import discord

class Perm:
    def __init__(self):
        self.balance = 5
        return
    
    def is_owner(self, ctx):
        if ctx.message.author.id in str(open("data/bot/owner.txt", "r").readline().split(",")):
            return True
        else:
            return False