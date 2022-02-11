from typing import Type
import discord
from discord.ext import commands
from ethermine import Ethermine

description = '''BOT ETH PRICE 1 HOURS TIME'''
intents = discord.Intents.default()
intents.members = True

client = commands.Bot(command_prefix='!', description=description, intents=intents)

@client.event
async def on_ready():
    ethermine = Ethermine()
    address = "0x7A9B050cd0875DBc5629851a61f339E2B07FC4BE"
    dashboard = ethermine.miner_current_stats(address)
    embed=discord.Embed(color=0xff6600)
    embed.add_field(name="UNPAID BALANCE FOR MINER '0x7A9B...'", value='__'+str(int(dashboard['unpaid'])/1000000000000000000)+' '+'ETH'+'__', inline=False)
    await client.get_channel(id=941774272404287538).send(embed=embed)


client.run('OTQxNzU1Nzg2NTcxNDE1NTUy.YgakbA.QlpzDT5rXz5yijmWJO8tMXp6nDs')
