#Imports
from webserver import al
import discord
from discord.ext import commands
import os
import time
import dotenv

#Variables
TOKEN = os.getenv('DISCORD_BOT_SECRET')
role = os.getenv('SECRET_ROLE')
#Prefixe
client = commands.Bot(command_prefix='!')

for filename in os.listdir('./cogs'):
	if filename.endswith('.py'):
		client.load_extension(f'cogs.{filename[:-3]}')

#Càrrega de comandaments
@client.command()
@commands.has_role(role)
async def carga(ctx, extension):
	client.load_extension(f'cogs.{extension}')
	await ctx.send('Extensión: ' + extension + ' cargada con éxito.')

#Descàrrega de comandaments
@client.command()
@commands.has_role(role)
async def descarga(ctx, extension):
	client.unload_extension(f'cogs.{extension}')
	await ctx.send('Extensión: ' + extension + ' descargada con éxito.')


# Fer que furuli
client.run(TOKEN)

# El keep Alive
al.keepalive()