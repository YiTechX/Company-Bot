import discord
import json
from discord.ext import commands

class EnterCompany(bot.Cog):
    def __init__(self, bot):
        self.bot = bot

    @bot.command(name="entercompany")
    async def entercompany(self, ctx):
        with open('config.json', 'r') as f:
            config = json.load(f)

        with open('DataBase/database.json', 'r') as f:
            database = json.load(f)

        if ctx.guild.owner_id == int(config['ownerid']):
            if ctx.guild:
                if len(ctx.guild.members) >= config['minmembercount'] and len(database['companies']) < config['maxpartner']:
                    # Create company channel
                    company_channel = await ctx.guild.create_text_channel('company')
                    
                    # Update database
                    database['companies'].append({
                        'server_name': ctx.guild.name,
                        'server_link': str(ctx.guild),
                        'channel_id': company_channel.id
                    })
                    with open('DataBase/database.json', 'w') as f:
                        json.dump(database, f, indent=4)

                    # Update main server's text
                    main_server = self.bot.get_guild(config['mainserverlink'])
                    company_channel_text = '\n'.join([f'--- {company["server_name"]}---\n{company["server_link"]}' for company in database['companies']])
                    company_channel_id = config['companychannelid']
                    channel = main_server.get_channel(company_channel_id)
                    await channel.edit(name=f'company-{len(database["companies"])}')
                    await channel.send(company_channel_text)
                else:
                    await ctx.send('Şartlar sağlanmadığı için company oluşturulamadı.')
        else:
            await ctx.send("Bu komutu kullanma izniniz yok.")

def setup(bot):
    bot.add_cog(EnterCompany(bot))
