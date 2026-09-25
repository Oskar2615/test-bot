import os
import discord
from discord import app_commands
from discord.ext import commands

TOKEN = os.getenv("DISCORD_TOKEN")

bot = commands.Bot(
    command_prefix=".",
    intents=discord.Intents.default()
)

@bot.event
async def on_ready():
    print(f"Online als {bot.user}")
    await bot.tree.sync()

@bot.tree.command(
    name="ping",
    description="Zeigt den Bot-Ping"
)
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message("🏓 Pong!")

bot.run(TOKEN)