import discord
from discord.ext import commands
from keep_alive import keep_alive
import random
import os

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

# URLs de las imágenes
IMAGES = {
    "Cara": "https://i.imgur.com/XxCara.png",
    "Cecca": "https://i.imgur.com/XxCruz.png"
}

@bot.event
async def on_ready():
    print(f'✅ Bot conectado como {bot.user}')

@bot.slash_command(name="cointoss", description="Lanza una moneda")
async def cointoss(ctx: discord.ApplicationContext):
    result = random.choice(["Cara", "Cecca"])
    
    embed = discord.Embed(
        title="Resultado del lanzamiento:",
        description=f"🪙 ¡Salió **{result}**!",
        color=discord.Color.gold()
    )
    embed.set_image(url=IMAGES[result])
    
    await ctx.respond(embed=embed)

# Mantener el bot activo (Replit + UptimeRobot)
keep_alive()

# Ejecutar el bot con el token secreto (guardado en Replit)
bot.run(os.getenv("DISCORD_BOT_TOKEN"))