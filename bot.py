import discord 
from discord.ext import commands 

client = commands.bot(command_prefix=">")

@client.event
async def on_ready():
	print ("I am ON")

@client.command()
async def hello(ctx):
	await ctx.send("hello")
client.run("NzU5MDI4MDMyODcwMjg1NDA1.X23h8Q.AzEK2pn6_CCRwFmQlOUiWNyDsVM")