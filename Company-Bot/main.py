import discord
import discord
import json
from discord.ext import commands

with open('config.json', 'r') as f:
    config = json.load(f)

intents = discord.Intents.default()
intents.members = True  

bot = commands.Bot(command_prefix='w!', intents=intents)


@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

bot.load_extension('createcompany')
bot.load_extension('entercompany')
bot.load_extension('leavecompany')
bot.load_extension('companies')
bot.load_extension('update')

bot.run(config['token'])


