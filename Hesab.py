from config import token
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True


client = commands.Bot(command_prefix="$", intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')
        
        
    await client.process_commands(message)
        
@client.command()
async def add(ctx, left: int, right: int):
    await ctx.send(left + right)

client.run(token)
