import discord
import random
import string
import json
from discord.ext import commands

class CreateCompany(bot.Cog):
    def __init__(self, bot):
        self.bot = bot

    @bot.command()
    async def createcompany(self, ctx, channel: discord.TextChannel):
        if ctx.author.guild_permissions.administrator:
            company_code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
            await ctx.send(f"Company başarıyla oluşturuldu! Katılım kodu: `{company_code}`")
            # Save company info to database
            with open('DataBase/database.json', 'r') as f:
                database = json.load(f)
            database['companies'].append({
                'server_name': ctx.guild.name,
                'server_link': str(ctx.guild),
                'channel_id': channel.id,
                'code': company_code
            })
            with open('DataBase/database.json', 'w') as f:
                json.dump(database, f, indent=4)
            # Set main channel
            config['mainchannel'] = channel.id
            with open('config.json', 'w') as f:
                json.dump(config, f, indent=4)
        else:
            await ctx.send("Bu komutu kullanma izniniz yok.")

def setup(bot):
    bot.add_cog(CreateCompany(bot))
