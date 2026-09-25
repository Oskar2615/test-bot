import os
import discord
from discord import app_commands
from discord.ext import commands

TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True  # notwendig, damit .ping (Text-Command) funktioniert

bot = commands.Bot(
    command_prefix=".",
    intents=intents
)

@bot.event
async def on_ready():
    print(f"Online als {bot.user}")
    try:
        synced = await bot.tree.sync()
        print(f"{len(synced)} Slash-Commands synchronisiert")
    except Exception as e:
        print(f"Fehler beim Sync: {e}")

# Slash-Command: /ping
@bot.tree.command(
    name="ping",
    description="Zeigt den Bot-Ping"
)
async def ping_slash(interaction: discord.Interaction):
    latency_ms = round(bot.latency * 1000)
    await interaction.response.send_message(f"🏓 Pong! ({latency_ms}ms)")

# Text-Command: .ping
@bot.command(name="ping")
async def ping_text(ctx):
    latency_ms = round(bot.latency * 1000)
    await ctx.send(f"🏓 Pong! ({latency_ms}ms)")

bot.run(TOKEN)