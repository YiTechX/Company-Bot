import discord
import json
from discord.ext import commands

class LeaveCompany(bot.Cog):
    def __init__(self, bot):
        self.bot = bot

    @bot.command()
    async def leavecompany(self, ctx):
        if ctx.author.guild_permissions.administrator:
            await ctx.send("Company sunucudan ayrılmak istediğinizden emin misiniz? (Eminseniz 'evet' yazın)")

            def check(m):
                return m.author == ctx.author and m.channel == ctx.channel

            try:
                msg = await self.bot.wait_for('message', timeout=30.0, check=check)
            except asyncio.TimeoutError:
                await ctx.send("Zaman aşımı! İşlem iptal edildi.")
                return

            if msg.content.lower() == 'evet':
                # Remove company from database
                with open('DataBase/database.json', 'r') as f:
                    database = json.load(f)

                for company in database['companies']:
                    if company['server_id'] == str(ctx.guild.id):
                        database['companies'].remove(company)
                        with open('DataBase/database.json', 'w') as f:
                            json.dump(database, f, indent=4)
                        break

                # Notify all owners of other companies
                for company in database['companies']:
                    guild = self.bot.get_guild(int(company['server_id']))
                    if guild:
                        owner = guild.owner
                        try:
                            await owner.send(f"Company sunucusundan {ctx.guild.name} ayrıldı! Detaylı bilgi için sunucunuzu kontrol edin.")
                        except:
                            print(f"Couldn't send DM to {owner}.")

                # Your code to leave company goes here
                await ctx.send("Company sunucudan başarıyla ayrıldı.")
            else:
                await ctx.send("İşlem iptal edildi.")
        else:
            await ctx.send("Bu komutu kullanma izniniz yok.")

def setup(bot):
    bot.add_cog(LeaveCompany(bot))
