import discord
import random

# Replace with your bot token
TOKEN = "MTM3NzA3MTYzNzI3MDM2ODQwNg.Gt4FGK.aTwKc9HAR0CIvEowW121uQyWKbjtiOMyOIXVBc"
GUILD_ID = 1377074511945531452  # Replace with your test server's Guild ID

# Coin images
image_urls = {
    "cara": "https://media.discordapp.net/attachments/1377074512696443003/1377078455425958009/7c08bc7b-7057-48b8-ab72-7db4f3f30fd7_removalai_preview.png?ex=6837a7c0&is=68365640&hm=3e6bc93d5d31cd80d6db9b3c79c09608bcee037900c571b0eba313f9c62cd151&=&format=webp&quality=lossless",
    "cecca": "https://media.discordapp.net/attachments/1377074512696443003/1377078455040217199/0068937d-f98c-4b12-a2a8-47e1421cd836_removalai_preview.png?ex=6837a7c0&is=68365640&hm=1ef4760972c40ba7de692c13f440c8c741f02f06b20ff2e1d887529d9b8475b5&=&format=webp&quality=lossless"
}

# Intents and client
intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = discord.app_commands.CommandTree(client)

@client.event
async def on_ready():
    print(f"✅ Logged in as {client.user}")
    await tree.sync(guild=discord.Object(id=GUILD_ID))  # Sync slash commands to a test server
    print("🌐 Slash commands synced.")

@tree.command(name="tirar", description="Tirá la moneda para ver si sale Cara o Cecca!", guild=discord.Object(id=GUILD_ID))
async def cointoss(interaction: discord.Interaction):
    coin = random.choice(["cara", "cecca"])
    embed = discord.Embed(title=f"Es **{coin.capitalize()}**!")
    embed.set_image(url=image_urls[coin])
    await interaction.response.send_message(embed=embed)

client.run(TOKEN)



