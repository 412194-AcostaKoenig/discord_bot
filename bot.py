import os
import sys
import random
import discord
from discord.ext import commands
from keep_alive import keep_alive  # Solo si estás usando Replit

# Intents necesarios
intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

# Mensaje cuando el bot se conecta
@bot.event
async def on_ready():
    print(f"✅ Bot conectado como {bot.user}")

# Comando !cointoss
@bot.command()
async def cointoss(ctx):
    resultado = random.choice(["Cara", "Cecca"])

    # URLs de las imágenes
    imagen_cara = "https://media.discordapp.net/attachments/1377074512696443003/1377078455425958009/7c08bc7b-7057-48b8-ab72-7db4f3f30fd7_removalai_preview.png?ex=6837a7c0&is=68365640&hm=3e6bc93d5d31cd80d6db9b3c79c09608bcee037900c571b0eba313f9c62cd151&=&format=webp&quality=lossless"
    imagen_cecca = "https://media.discordapp.net/attachments/1377074512696443003/1377078455040217199/0068937d-f98c-4b12-a2a8-47e1421cd836_removalai_preview.png?ex=6837a7c0&is=68365640&hm=1ef4760972c40ba7de692c13f440c8c741f02f06b20ff2e1d887529d9b8475b5&=&format=webp&quality=lossless"
    imagen_url = imagen_cara if resultado == "Cara" else imagen_cecca

    # Crear el embed
    embed = discord.Embed(title=f"Resultado: {resultado}", color=0x00ff00)
    embed.set_image(url=imagen_url)
    await ctx.send(embed=embed)

# Mantener vivo en Replit
keep_alive()

# Obtener el token desde las variables de entorno
token = os.getenv("DISCORD_BOT_TOKEN")
if token is None:
    print("❌ ERROR: La variable de entorno DISCORD_BOT_TOKEN no está definida.")
    sys.exit(1)

# Iniciar el bot
bot.run(token)