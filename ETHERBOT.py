from typing import Type
import discord
from discord.ext import commands
from ethermine import Ethermine
import yfinance as yf
import time

description = '''SEND EVERY 30min ETH PRICE AND ETHERMINE STATS'''
intents = discord.Intents.default()
intents.members = True

client = commands.Bot(command_prefix='!', description=description, intents=intents)

@client.event
async def on_ready():
    while True:
        ethermine = Ethermine()
        address = "YOUR ADRESS"
        dashboard = ethermine.miner_current_stats(address)
        embed=discord.Embed(color=0xff6600)
        embed.add_field(name="UNPAID BALANCE FOR MINER 'YOUR ADRESS...'", value='__'+str(int(dashboard['unpaid'])/1000000000000000000)+' '+'ETH'+'__', inline=False)
        await client.get_channel(id=YOUR CHANNEL ID).send(embed=embed)
        data=yf.download(tickers='ETH-USD', period= '1d', interval='1d')
        embed=discord.Embed()
        embed.add_field(name="PRICE ETH/USD", value='__'+str(data['Close'])+'__', inline=False)
        await client.get_channel(id=YOUR CHANNEL ID).send(embed=embed)
        time.sleep(1800)


client.run('YOUR BOT TOKEN')
