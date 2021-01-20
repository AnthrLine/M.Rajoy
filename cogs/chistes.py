import discord
from discord.ext import commands
import random

class acudits(commands.Cog):


	def __init__(self, client):
		self.client = client

	@commands.command()
	@commands.has_role('Don comedia')
	async def afegiracudit(self, ctx, acudit):
		ok = ':white_check_mark: ACUDIT AFEGIT AMB ÈXIT :white_check_mark:'
		f = open('acudits.txt', 'a')
		f.write('\n' + acudit)
		f.close()
		await ctx.send(ok)
		print('S\'ha afegit l\'acudit ' + acudit)

	@commands.command()
	async def chiste(self, ctx):
		f = open('acudits.txt', 'r') 
		Acudits = f.readlines()
		f.close()
 
		c = '_'
		symbol = ' '
		random.shuffle(Acudits)
		Chis = (Acudits[0])
		Acudit_final = Chis.replace(c,symbol)
		embed = discord.Embed(title="Chiste", colour=discord.Colour(0x42ff68))

		embed.add_field(name='Su chiste es:', value=f'{Acudit_final}')
		await ctx.send(embed=embed)
		print('S\'ha executat acudit')

def setup(client):
	client.add_cog(acudits(client))