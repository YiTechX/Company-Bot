import discord
import json
from discord.ext import commands, tasks

class UpdateText(bot.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.update_text.start()

    async def update_text_in_main_server(self):
        main_channel_id = config['mainchannel']
        main_channel = self.bot.get_channel(main_channel_id)
        if main_channel:
            with open('DataBase/database.json', 'r') as f:
                database = json.load(f)
            company_channel_text = '\n'.join([f'--- {company["server_name"]}---\n{company["server_link"]}' for company in database['companies']])
            await main_channel.send(company_channel_text)

    @tasks.loop(hours=1)
    async def update_text(self):
        await self.update_text_in_main_server()

    @update_text.before_loop
    async def before_update_text(self):
        print('Waiting for bot to be ready...')
        await self.bot.wait_until_ready()

def setup(bot):
    bot.add_cog(UpdateText(bot))
