import discord
from discord.ext import commands
import time
import os
import datetime
import fitxer
from discord.utils import get

client = commands.Bot(command_prefix='!')

class jocs(commands.Cog):


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
		'''Haz una encuesta con todos los miembros del servidor.'''
		if pregunta == 'NaN':
			await ctx.send('Añade una pregunta, !encuesta {pregunta_aquí}')
		else:
			embed = discord.Embed(title="¡Es momento de tomar una encuesta!", colour=discord.Colour(0x3e038c))
			embed.add_field(name='Autor de la encuesta', value=f'{ctx.author}')
			embed.add_field(name='Pregunta:', value=f'{pregunta}')
			msg = await ctx.send(embed=embed)
			await msg.add_reaction(str('🔺'))
			await msg.add_reaction(str('🔻'))


	@commands.command()
	async def mensaje(self, ctx, mensaje='NaN'):
			if mensaje == 'NaN':
				embed = discord.Embed(title='Error', colour=discord.Colour(0xff0f0f))

				embed.add_field(name='Añade un mensaje!', value=f'Añade un mensaje así `!mensaje <Frase_aquí>`')
				await ctx.send(embed=embed)
			else:
				await ctx.channel.purge(limit=1)
				f = open('mensajes.txt', 'a')
				# Afegeix el missatge
				f.write('\n' + mensaje)
				# Tanca
				f.close()
				f1 = open('horas.txt', 'a')
				# Afegeix el missatge
				f1.write('\n')
				f1.write(str(datetime.datetime.now()))
				# Tanca
				f1.close()
				embed = discord.Embed(title='¡Mensaje añadido con éxito!', colour=discord.Colour(0x42ff68))

				embed.add_field(name='¡Gracias por añadir tu mensaje!', value=f'¡Ahora qualquier persona podrá ver tu mensaje!')
				await ctx.send(embed=embed)
				time.sleep(5)
				await ctx.channel.purge(limit=1)

	@commands.command()
	async def leermensaje(slf, ctx):
		c = '_'
		symbol = ' '
		mensajem = fitxer.get_last_n_lines("mensajes.txt", 1)
		hora = fitxer.get_last_n_lines('horas.txt', 1)
		mensaje = mensajem[0]
		mensajeb = mensaje.replace(c,symbol)
		embed = discord.Embed(title='Leer mensaje:', colour=discord.Colour(0x42ff68))

		embed.add_field(name='El mensaje es:', value=f'{mensajeb}'),

		embed.add_field(name='Este mensaje fue escrito en:', value=f'{hora[0]}')
		await ctx.send(embed=embed)

def setup(client):
	client.add_cog(jocs(client))