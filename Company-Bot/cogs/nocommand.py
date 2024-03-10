import discord
from discord.ext import commands

class NoCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def no_command(self, ctx, command_name):
        command_name = command_name.lower()
        similar_commands = [command.name for command in self.bot.commands if command_name in command.name.lower()]
        if similar_commands:
            await ctx.send(f"Üzgünüm, `{command_name}` adında bir komutum yok. Ancak, benzer komutlar şunlar olabilir: {', '.join(similar_commands)}")
        else:
            await ctx.send(f"Üzgünüm, `{command_name}` adında bir komutum yok.")

def setup(bot):
    bot.add_cog(NoCommand(bot))
