from datetime import datetime
import command
import discord
import chila

class perfSearch(command.Command):

    def __init__(self):
        super().__init__(name="search", help="Search for a users rating")

    async def execute(self, msg: discord.message.Message):
        chilaObj = chila.Chila()
        msgArgs = msg.content.split(' ')

        if await chilaObj.isUser(msgArgs[1]) == False:
            await msg.channel.send(msgArgs[1]+ " is not a valid user")
        
        usrRating: dict = await chilaObj.getUserRating(msgArgs[1], True)
        timestamp = datetime.now()

        embed = discord.Embed(title="Rating Search", description=msgArgs[1], color=0xff0000)

        for k, v in usrRating.items():
            embed.add_field(name=k, value=v, inline=True)

        embed.set_footer(text=timestamp.strftime(r"%I:%M %p"))

        await msg.channel.send(embed=embed)