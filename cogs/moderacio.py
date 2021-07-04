import discord
import sys
from discord.ext import *

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
		await ctx.send('Expulsando...')
		await member.kick(reason=why)

		embed = discord.Embed(title="Expulsión", colour=discord.Colour(0x42ff68))

		embed.add_field(name='Detalles de la expulsión:', value=f'**{member} ha sido expulsado por {ctx.author}**')

		await ctx.channel.send(embed=embed)

	@commands.command(pass_context = True)
	@commands.has_permissions(manage_channels=True)
	async def mutear(self, ctx, member: discord.Member, role: discord.Role):
		await member.add_roles(role)
		embed=discord.Embed(title="Usuario muteado", description=f"**{member}** ha sido muteado por **{ctx.author}**!", color=0xff00f6)
		await ctx.channel.send(embed=embed)

	@commands.command(pass_context = True)
	@commands.has_permissions(manage_channels=True)
	async def desmutear(self, ctx, member: discord.Member, role: discord.Role):
		await member.remove_roles(role)
		embed=discord.Embed(title="Usuario desmuteado", description=f"**{member}** ha sido desmuteado por **{ctx.author}**!", color=0xff00f6)
		await ctx.channel.send(embed=embed)

def setup(client):
	client.add_cog(principals(client))
