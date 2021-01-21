import discord
from discord.ext import commands
import time
import os
import datetime
import fitxer
from discord.utils import get

client = commands.Bot(command_prefix='!')

class encuesta(commands.Cog):


	def __init__(self, client):
		self.client = client

	@commands.command()
	@commands.has_permissions(manage_channels=True)
	async def comprobar_ganador(self, ctx, messageid):
		await ctx.channel.purge(limit=1)
		message = await ctx.fetch_message(messageid)
		reaction = get(message.reactions, emoji='🔺')
		reaction1 = get(message.reactions, emoji='🔻')
		num_reactions = reaction.count
		num_reactions1 = reaction1.count
		if num_reactions == num_reactions1:
			embed = discord.Embed(title="¡Resultados!", colour=discord.Colour(0x3e038c))

			embed.add_field(name='Ha habido un empate:', value=f'La primera reacción ha tenido {num_reactions} reacciones y la segunda reacción ha tenido {num_reactions1} reacciones.')

			await ctx.send(embed=embed)
		elif num_reactions < num_reactions1:
			embed = discord.Embed(title="¡Resultados!", colour=discord.Colour(0x3e038c))

			embed.add_field(name='Ha ganado la segunda reacción', value=f'La segunda reacción ha ganado y ha obtenido {num_reactions1} reacciones.')

			await ctx.send(embed=embed)
		elif num_reactions > num_reactions1:
			embed = discord.Embed(title="¡Resultados!", colour=discord.Colour(0x3e038c))

			embed.add_field(name='Ha ganado la primera reacción', value=f'La primera reacción ha ganado y ha obtenido {num_reactions} reacciones.')

			await ctx.send(embed=embed)

	@commands.command()
	@commands.has_permissions(manage_channels=True)
	async def encuesta(self, ctx, pregunta='NaN'):
		c = '_'
		symbol = ' '
		pregunta1 = pregunta.replace(c,symbol)
		'''Haz una encuesta con todos los miembros del servidor.'''
		if pregunta == 'NaN':
			await ctx.send('Añade una pregunta, !encuesta {pregunta_aquí}')
		else:
			embed = discord.Embed(title="¡Es momento de tomar una encuesta!", colour=discord.Colour(0x3e038c))
			embed.add_field(name='Autor de la encuesta', value=f'{ctx.author}')
			embed.add_field(name='Pregunta:', value=f'{pregunta1}')
			msg = await ctx.send(embed=embed)
			await msg.add_reaction(str('🔺'))
			await msg.add_reaction(str('🔻'))
			usr = ctx.author
			await usr.send(f'Id de la encuesta: {msg.id}')

def setup(client):
	client.add_cog(encuesta(client))