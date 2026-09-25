import discord
from discord import app_commands
from discord.ext import commands


TOKEN = os.getenv("DISCORD_TOKEN")


bot = commands.Bot(
    commands_prefix=".",

    intents=discord.Intents.default()
)


@bot.event
async def on_ready():
    print(f"online als {bot.user}")
    await bot.tree.sync()


@bot.tree.command(name="ping",
description="zeigt den bot ping")
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message("🏓 Pong!")



   bot.run(TOKEN)
