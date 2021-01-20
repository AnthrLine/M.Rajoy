import discord
from discord.ext import commands
import random

class frases(commands.Cog):


	def __init__(self, client):
		self.client = client

	@commands.command()
	@commands.has_role('m.')
	async def afegirfrase(self, ctx, frase='NaN'):
		if frase == 'NaN':
			await ctx.send('Afegeix alguna cosa, si us plau.')
		else:
			ok = ':white_check_mark: FRASE AFEGIDA AMB ÈXIT :white_check_mark:'
			# Obre el fitxer
			f = open('frases.txt', 'a')
			# Afegeix la frase
			f.write('\n' + frase)
			# Tanca i envia la confirmació
			f.close()
			await ctx.send(ok)
			print('S\'ha afegit la frase ' + frase)

	@commands.command()
	async def frase(self, ctx):
		f = open('frases.txt', 'r') 
		Frases = f.readlines()
		f.close()
 
		c = '_'
		symbol = ' '
		random.shuffle(Frases)
		Frasef = (Frases[0])
		Fraseenviar = Frasef.replace(c,symbol)

		embed = discord.Embed(title="Frase", colour=discord.Colour(0x42ff68))

		embed.add_field(name='Su frase es:', value=f'{Fraseenviar}')

		await ctx.send(embed=embed)
		print('S\'ha executat frase')


def setup(client):
	client.add_cog(frases(client))