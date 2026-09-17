import discord 
from discord.ext import commands
import psutil
import time

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@bot.event
async def on_ready():
    print("bot hazır!")

@bot.command()
async def islemci(ctx):
    await ctx.send("CPU ölçülüyor..")
    cpu = psutil.cpu_percent(interval=10)
    await ctx.send(f"CPU kullanımı: %{cpu}")

@bot.command()
async def ram(ctx):
    ram = psutil.virtual_memory()
    await ctx.send(f"RAM kullanımı: %{ram.percent} ")

@bot.command()
async def sistem(ctx):
    cpu = psutil.cpu_percent(interval=1)
    ram = psutil.virtual_memory().percent
    await ctx.send(f"CPU: %{cpu}\nRAM: %{ram}")


bot.run("")
