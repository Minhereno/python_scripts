import discord
import numpy as np
from discord.ext import commands


client = commands.Bot(command_prefix = "!")

@client.event
async def on_ready():
    print("Bot is ready!")


@client.event
async def on_message(message):
    #if message.author == client.user:
    #    return

    #brooklyn_99_quotes = [
    #    'I\'m the human form of the 💯 emoji.',
    #    'Bingpot!',
    #    (
    #        'Cool. Cool cool cool cool cool cool cool, '
    #        'no doubt no doubt no doubt no doubt.'
    #    ),
    #]

    if message.content == '99!':
        response = np.random.choice(brooklyn_99_quotes)
        await message.channel.send(response)
    #help command
    elif message.content.lower() == 'help':
        await message.channel.send('Use one of the following commands followed by a Summoner ID: Commands: -ftpchamps')

    elif message.content == 'raise-exception':
        raise discord.DiscordException



@client.command()
#ping command
async def ping(ctx):
    await ctx.send(f"Your ping is: {round(client.latency * 1000)}ms")

async def FTPChamps(ctx):    
    Champs = lol.get_champions(free_to_play=True)
    for Champ in Champs:
        await ctx.send(Champ['name'])