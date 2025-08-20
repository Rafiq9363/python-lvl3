from config import token
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(command_prefix="!", intents=intents)


class Car:
    def __init__(self, color, brand):
        self.color = color
        self.brand = brand

    def info(self):
        return f"Bu araba {self.color} renginde {self.brand} markalıdır."

@client.event
async def on_ready():
    print(f"Giris yapti: {client.user}")
    
    
@client.event
async def on_message(message):
    if message.author == client.user:
        return 
    
     
    await client.process_commands(message)


@client.command()
async def car(ctx, color: str, brand: str):
    my_car = Car(color, brand)   
    text = my_car.info()           
    await ctx.send(text)         

client.run(token)
