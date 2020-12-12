import discord
import sys
from discord.ext import commands

class principals(commands.Cog):


	def __init__(self, client):
		self.client = client


	@commands.command()
	@commands.has_permissions(manage_channels=True)
	async def limpiar(self, ctx, quantitat=10):
		if quantitat <= 1:
			await ctx.send('Ingresa un valor válido')
		else:
			await ctx.channel.purge(limit=quantitat)

	@commands.command()
	@commands.has_permissions(administrator=True)
	async def expulsa(self, ctx, member: discord.Member, *, why=None):
		await member.kick(reason=why)
		await ctx.channel.send(f"**{member} ha sido expulsado por {ctx.author}**")

def setup(client):
	client.add_cog(principals(client))