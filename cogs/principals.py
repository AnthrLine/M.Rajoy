import discord
import sys
from discord.ext import commands
import time
import os

role = os.getenv('SECRET_ROLE')

class principals(commands.Cog):


	def __init__(self, client):
		self.client = client

	#EVENTS
	@commands.Cog.listener()
	async def on_ready(self):
		print('Mariano online! El suyo beneficio!')

	@commands.command()
	async def vota(self, ctx):

		embed = discord.Embed(title="Vota", colour=discord.Colour(0x42ff68))

		embed.add_field(name='Votar:', value='¡Gracias por querer votar! :heart: Nuestro equipo te lo agradece! Puedes votar en este link: https://bit.ly/votaRajoy')
		await ctx.send(embed=embed)

	@commands.command()
	async def vote(self, ctx):
		embed = discord.Embed(title="Vota", colour=discord.Colour(0x42ff68))

		embed.add_field(name='Votar:', value='¡Gracias por querer votar! :heart: Nuestro equipo te lo agradece! Puedes votar en este link: https://bit.ly/votaRajoy')
		await ctx.send(embed=embed)


	@commands.command()
	@commands.has_role(role)
	async def devol_stop(self, ctx):
		sys.exit()

	@commands.command(pass_context=True)
	async def ping(self, ctx):
		""" Pong! """
		before = time.monotonic()
		message = await ctx.send("Pong!")
		ping = (time.monotonic() - before) * 1000
		await message.edit(content=f"Pong!  `{int(ping)}ms`")
		print(f'Ping {int(ping)}ms')

	@commands.command()
	async def comandos(self, ctx):
		usr = ctx.author
		embed = discord.Embed(title="Lista de comandos de M. Rajoy", colour=discord.Colour(0x42ff68))

		embed.add_field(name='Limpiar:',value=f'`!limpiar` o `!limpiar <Cantidad de mensajes>` se necesita gestionar canales.', inline=False),

		embed.add_field(name='Frase:', value=f'`!frase`', inline=False),

		embed.add_field(name='Tula:', value=f'`!tula`', inline=False),

		embed.add_field(name='Ping:', value=f'`!ping`', inline=False),

		embed.add_field(name='Chiste:', value=f'`!chiste`', inline=False),

		embed.add_field(name='Vota:', value=f'`!vota`', inline=False),

		embed.add_field(name='Añadir mensaje:', value=f'`!mensaje <Mensaje_aquí>`', inline=False),

		embed.add_field(name='Leer mensaje:', value=f'`!leermensaje`', inline=False),

		embed.add_field(name='Expulsa', value=f'`!expulsa <@Nombre> <Motivo>` Se necesita administrador', inline=False)

		embed.add_field(name='Encuesta', value=f'`!encuesta <Frase_aquí>` se necesita gestionar canales.', inline=False),

		embed.add_field(name='Encuesta (comprobar ganador)', value=f'`!comprobar_ganador <Id encuesta>` se necesita gestionar canales.', inline=False)

		await usr.send(embed=embed)
		await ctx.send(f'Md enviado! {ctx.author}')

def setup(client):
	client.add_cog(principals(client))