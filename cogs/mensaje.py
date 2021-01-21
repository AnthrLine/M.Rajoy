import discord
from discord.ext import commands
import time
import os
import datetime
import fitxer
from discord.utils import get

client = commands.Bot(command_prefix='!')

class mensaje(commands.Cog):


	def __init__(self, client):
		self.client = client

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
	client.add_cog(mensaje(client))