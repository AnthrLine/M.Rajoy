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
			file_object = open('frases.txt', 'a')
			# Afegeix la frase
			file_object.write('\n' + frase)
			# Tanca i envia la confirmació
			file_object.close()
			await ctx.send(ok)
			print('S\'ha afegit la frase ' + frase)

	@commands.command()
	async def frase(self, ctx):
		file1 = open('frases.txt', 'r') 
		Lines = file1.readlines()
		file1.close()
 
		c = '_'
		symbol = ' '
		random.shuffle(Lines)
		Chis = (Lines[0])
		modified_str = Chis.replace(c,symbol)

		await ctx.send(modified_str)
		print('S\'ha executat frase')


def setup(client):
	client.add_cog(frases(client))