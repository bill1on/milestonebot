'''
import discord
import asyncio
from discord.ext import commands, menus
import logging

class TestCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def TestCommand(self, ctx):
        pass

    @commands.command()
    async def TestCommand2(self, ctx):
        pass
    
    @commands.command()
    async def TestCommand3(self, ctx):
        pass

def setup(bot):
    bot.add_cog(TestCog(bot))'''


def song_decoder(song):
    newstr = ''
    temp = song.split('WUB')
    new = ''.join(temp)
    for o, i in enumerate(new):
        if o+1 == len(new):
            newstr += i 
        else:
            newstr += i + ' '
    return newstr

print(song_decoder('WUBAWUBBWUBCWUB'))