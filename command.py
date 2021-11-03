import discord

class Command():

    def __init__(self, name: str, help: str) -> None:
        self.name = name
        self.help = help

    def execute(self, msg: discord.message.Message):
        pass

    # Getter for commands name
    def getName(self):
        return self.name

    # Getter for commands help
    def getHelp(self):
        return self.help