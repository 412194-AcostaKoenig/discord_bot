import os
import sys
import random
import discord
from discord.ext import commands
from keep_alive import keep_alive  # Solo si usas Replit
from dotenv import load_dotenv

intents = discord.Intents.default()
intents.message_content = True  # Habilitar lectura de mensajes
bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    print(f"✅ Bot conectado como {bot.user}")


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    print(f"Mensaje recibido: {message.content}")
    await bot.process_commands(message)


@bot.command()
async def cointoss(ctx):
    resultado = random.choice(["Cara", "Cecca"])

    imagen_cara = os.getenv("IMG_CARA")
    imagen_cecca = os.getenv("IMG_CECCA")
    imagen_url = imagen_cara if resultado == "Cara" else imagen_cecca

    embed = discord.Embed(title=f"Resultado: {resultado}", color=0x00ff00)
    embed.set_image(url=imagen_url)
    await ctx.send(embed=embed)


keep_alive()
load_dotenv()
token = os.getenv("DISCORD_BOT_TOKEN")

if token is None:
    print(
        "❌ ERROR: La variable de entorno DISCORD_BOT_TOKEN no está definida.")
    sys.exit(1)

bot.run(token)
