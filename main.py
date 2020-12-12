# Imports
from webserver import al
import discord
from discord.ext import commands
import os
import time

# Variables
TOKEN = 'NzYxNTc0MjczNDk5OTIyNDcy.X3clUA.2WZlpmemnBVv9fOuNNj41On9qzY'

# Crear el bot
client = commands.Bot(command_prefix='!')

for filename in os.listdir('./cogs'):
	if filename.endswith('.py'):
		client.load_extension(f'cogs.{filename[:-3]}')

# Comandaments
# Secció underground

@client.command()
@commands.has_role('Don comedia')
async def carga(ctx, extension):
	client.load_extension(f'cogs.{extension}')
	await ctx.send('Extensión: ' + extension + ' cargada con éxito.')

@client.command()
@commands.has_role('Don comedia')
async def descarga(ctx, extension):
	client.unload_extension(f'cogs.{extension}')
	await ctx.send('Extensión: ' + extension + ' descargada con éxito.')


# Fer que furuli
client.run(TOKEN)

# El keep Alive
al.keepalive()