import discord
from discord.ext import commands
from keep_alive import keep_alive
import random
import os

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

# URLs de las imágenes
IMAGES = {
    "Cara": "https://media.discordapp.net/attachments/1377074512696443003/1377078455425958009/7c08bc7b-7057-48b8-ab72-7db4f3f30fd7_removalai_preview.png?ex=6837a7c0&is=68365640&hm=3e6bc93d5d31cd80d6db9b3c79c09608bcee037900c571b0eba313f9c62cd151&=&format=webp&quality=lossless",
    "Cecca": "https://media.discordapp.net/attachments/1377074512696443003/1377078455040217199/0068937d-f98c-4b12-a2a8-47e1421cd836_removalai_preview.png?ex=6837a7c0&is=68365640&hm=1ef4760972c40ba7de692c13f440c8c741f02f06b20ff2e1d887529d9b8475b5&=&format=webp&quality=lossless"
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