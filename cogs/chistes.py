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
		file_object = open('acudits.txt', 'a')
		file_object.write('\n' + acudit)
		file_object.close()
		await ctx.send(ok)
		print('S\'ha afegit l\'acudit ' + acudit)

	@commands.command()
	async def chiste(self, ctx):
		file1 = open('acudits.txt', 'r') 
		Lines = file1.readlines()
		file1.close()
 
		c = '_'
		symbol = ' '
		random.shuffle(Lines)
		Chis = (Lines[0])
		modified_str = Chis.replace(c,symbol)
		await ctx.send(modified_str)
		print('S\'ha executat acudit')

def setup(client):
	client.add_cog(acudits(client))