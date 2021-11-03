import command
import discord
import chila

class compare(command.Command):

    def __init__(self):
        super().__init__(name="compare", help="Compare a record between 2 players")

    async def execute(self, msg: discord.message.Message):
        chilaObj = chila.Chila()
        userNames = msg.content.split(' ')

        await chilaObj.getUserRating('nsedler')

        if(await chilaObj.isUser(userNames[1]) == False):
            await msg.channel.send(userNames[1]+ " is not a valid user")
        elif(await chilaObj.isUser(userNames[2]) == False):
            await msg.channel.send(userNames[2]+ " is not a valid user")
        else:
            usrCrosstable = await chilaObj.getUserCrossTable(userNames[1], userNames[2])
            await msg.channel.send(usrCrosstable)