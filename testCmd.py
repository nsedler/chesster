import command
import discord

class testCmd(command.Command):

    def __init__(self):
        super().__init__(name="who", help="gay")

    async def execute(self, msg: discord.message.Message):
        await msg.channel.send("<@394930557076897804> is a gay loser HAHAHAHA")