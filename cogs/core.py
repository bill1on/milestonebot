import discord
import asyncio
from discord.ext import commands, menus
import logging


class HelpSource(menus.ListPageSource):
    def __init__(self, cmds, url):
        super().__init__(entries = cmds, per_page=1)
        self.commands = cmds
        self.url = url

    def format(self, commands):
        page = []
        for i in commands:
            if i.description: 
                value = i.name + ' | ' + i.description
                page.append(value)
            else:
                value = i.name + ' | ' + 'No description available...'
                page.append(value)
        return page
    
    async def format_page(self, menu, cogs):
        for cog in cogs.keys():
            if cog.startswith('desc'):
                tinfo = cogs.get(cog)
                info = info + tinfo
                embed = discord.Embed(title = 'Milestone | Help', description = info, color = 0x52ffa0)
            elif cog:
                value = self.format(commands)
                new = '\n'.join(value)
                embed = discord.Embed(title = 'Milestone | Commands', color = 0x52ffa0)
                embed.add_field(name = cog.qualified_name, value = new, inline = False)
        
        maximum = self.get_max_pages()
        embed.set_footer(text = f'Made by billion#2126 • Page {menu.current_page + 1}/{maximum}', icon_url = self.url)

        return embed

class Help(commands.HelpCommand):

    async def send_bot_help(self, mapping):
        ctx = self.context
        bot = ctx.bot
        test = {
            'ffg': 'Milestone is an easy to use bot, written in Python by:\n`billion#2126`\n\n',
            'xcz': 'For more help and resources visit:\n[Support Server](https://discord.gg/APNfTvW)\n\n',
            'vcx': f'Use `{ctx.prefix}help <command>` for more information on a command.\nUse `{ctx.prefix}help <category>` for more information on a category.\n\n',
            'xzc': 'For a list of all commands just navigate using the reactions below.'
        }

        for cog in bot.cogs:
            print(cog)
        
        url = bot.get_user(147840568897044480).avatar_url
        pages = menus.MenuPages(source = HelpSource(test, str(url)), clear_reactions_after = True)
        await pages.start(ctx)

    async def send_command_help(self, command):
        print('ok')

class Help_Category(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot
        bot.help_command = Help()
        bot.help_command.cog = self

    
def setup(bot):
    bot.add_cog(Help_Category(bot))