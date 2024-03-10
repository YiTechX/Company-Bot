import discord
import json
from discord.ext import commands

class Companies(bot.Cog):
    def __init__(self, bot):
        self.bot = bot

    @bot.command(name="top")
    async def companies(self, ctx):
        with open('DataBase/database.json', 'r') as f:
            database = json.load(f)
        sorted_companies = sorted(database['companies'], key=lambda x: len(self.bot.get_guild(int(x['server_id'])).members), reverse=True)[:10]
        
        embed = discord.Embed(title="Top 10 Companies", color=discord.Color.green())
        for index, company in enumerate(sorted_companies):
            guild = self.bot.get_guild(int(company['server_id']))
            if guild:
                embed.add_field(name=f"{index+1}. {company['server_name']}", value=f"Server Link: {company['server_link']}\nMember Count: {len(guild.members)}", inline=False)

        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Companies(bot))
