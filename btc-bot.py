import os
import sys
import json
import discord
import asyncio
import requests
import aiohttp
from discord.ext import commands

with open('config.json') as f:
    config = json.load(f)

token = config.get('token')
prefix = config.get('prefix')
address = config.get('address')

bot = discord.Client()
bot = commands.Bot(command_prefix=prefix, self_bot=True)

@bot.event
async def on_ready():
    print("[>] Invoice Bot is online.")

@bot.event
async def on_command_error(ctx, error):
    print(f'Error: {error}')

@bot.command()
async def btc(ctx, amount):
    await ctx.message.delete()
    try:
        amountToSend = requests.get(f'https://blockchain.info/tobtc?currency=USD&value={amount}').text
        embed = discord.Embed(title = "Pay Skeleton", color = 0xFC2C54)
        embed.add_field(name='Address', value=f'``{address}``', inline=False)
        embed.add_field(name='Amount', value=f'``{amountToSend}``', inline=False)
        embed.set_thumbnail(url='https://terror.win/thumbnail.png')
        await ctx.send(embed=embed)
    except:
        print("[>] Cannot send embeds here.")

try:
    bot.run(token, bot=False, reconnect=True)
except Exception as E:
    print(f'[>] Error: {E}')
