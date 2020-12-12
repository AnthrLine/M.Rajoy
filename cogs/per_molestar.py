import discord
from discord.ext import commands
import time
import random

class molestar(commands.Cog):


	def __init__(self, client):
		self.client = client

#	@commands.command()
#	async def Jan(self, ctx):
#		await ctx.send(':rat:')

	@commands.command()
	async def helloworld(self, ctx):
		await ctx.send('Hello World!')

	@commands.command()
	async def tula(self, ctx):
		mida = ''
		message = await ctx.send('Calculando tula... Espere')
		time.sleep(2)
		mida = random.randint(0, 100)
		midab = mida + .00
		if mida == 0:
			await message.edit(content=f"Calculando tula... Espere  `La tula de {ctx.author} mide 0cm, ¡inexistente!`") 
		elif midab >= 0.00 and midab <= 7.00:
			await message.edit(content=f"Calculando tula... Espere  `Tu tula mide {mida}cm, ¡microtula!`")
		else:
			await message.edit(content=f"Calculando tula... Espere  `Tu tula mide {mida}cm, ¡buena tula!`")

	@commands.command()
	async def mira_que_tengo(self, ctx):
		await ctx.send(':ok_hand:')

#	@commands.command()
#	async def xd(self, ctx):
#		i = 1000
#		while i >= 0:
#			await ctx.send("xd")
#			i -= 1

#@commands.command()   PER COMANDOS
def setup(client):
	client.add_cog(molestar(client))