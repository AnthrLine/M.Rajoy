import discord
import sys
from discord.ext import commands, tasks
import time
import os
from itertools import cycle

role = os.getenv('SECRET_ROLE')

class principals(commands.Cog):


	def __init__(self, client):
		self.client = client

	#EVENTS
	@commands.Cog.listener()
	async def on_ready(self):
		print('Mariano online! El suyo beneficio!')

	@commands.command()
	async def comandos(self, ctx):
		await ctx.send('!comandos, !expulsa (usuario) (motivo) (Sólo para administradores), !frase, !chiste, !limpiar [] (Sólo para rol MOD), !vota')

	@commands.command()
	async def vota(self, ctx):
		await ctx.send('¡Gracias por querer votar! :heart: Nuestro equipo te lo agradece! Puedes votar en este link: https://bit.ly/votaRajoy')

	@commands.command()
	@commands.has_role(role)
	async def devol_stop(self, ctx):
		sys.exit(await ctx.send('Capullos'))

	@commands.command(pass_context=True)
	async def ping(self, ctx):
		""" Pong! """
		before = time.monotonic()
		message = await ctx.send("Pong!")
		ping = (time.monotonic() - before) * 1000
		await message.edit(content=f"Pong!  `{int(ping)}ms`")
		print(f'Ping {int(ping)}ms')

def setup(client):
	client.add_cog(principals(client))