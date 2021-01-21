import discord
from discord.ext import commands
import time
import random

class molestar(commands.Cog):


	def __init__(self, client):
		self.client = client

	

	@commands.command()
	async def tula(self, ctx):
		await ctx.send('Calculando tula... Espere')
		time.sleep(2)
		mida = tulam()
		embed = discord.Embed(title="Tula", colour=discord.Colour(0x42ff68))

		embed.add_field(name='Tula', value=f'Tu tula mide {mida}cm, ¡espectacular!')

		await ctx.send(embed=embed)

	@commands.command()
	async def mira_que_tengo(self, ctx):
		await ctx.send(':ok_hand:')

def setup(client):
	client.add_cog(molestar(client))

def tulam():
	probabilitat = random.randint(0,25)
	if probabilitat == 0 or probabilitat == 4 or probabilitat == 5:
		mida = random.randint(9, 99)
		return(mida)
	elif probabilitat == 1:
		mida1 = 0
		return(mida1)
	elif probabilitat == 2:
		mida2 = 100
		return(mida2)
	else:
		midae = random.randint(1, 8)
		return(midae)