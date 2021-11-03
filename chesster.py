from datetime import datetime
import discord
from chila import Chila
import command
import testCmd
import compare
import perfSearch

cmds = [testCmd.testCmd(), compare.compare(), perfSearch.perfSearch()]

class helpCmd(command.Command):
    def __init__(self):
        super().__init__(name="search", help="gay")

    async def execute(self, msg: discord.message.Message):
        timestamp = datetime.now()

        embed = discord.Embed(title="Rating Search", description="", color=0xff0000)
        embed.add_field(name=",help", value="Shows description of all commands", inline=True)
        for cmd in cmds:
            embed.add_field(name="," + cmd.name, value=cmd.help, inline=True)

        embed.set_footer(text=timestamp.strftime(r"%I:%M %p"))

        await msg.channel.send(embed=embed)

class Bot(discord.Client):
    

    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        # don't respond to ourselves
        
        if message.author == self.user:
            return
        
        if message.content == ",quit":
            await message.channel.send("bye bye")
            await self.logout()
        elif message.content == ",help":
            await helpCmd().execute(msg=message)
        else:
            for cmdName in cmds:
                name = cmdName.name
                msg = message.content.split(' ')[0]
                if msg == "," + name:
                    await cmdName.execute(message)

