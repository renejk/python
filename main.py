import discord
from discord.ext import commands
import random

TOKEN = 'ODg1MTg1MzIyNjkzMDU4NjAw.YTjXEg.RVJM8ArDKeLA94r6Fkeqdsh_4j0'


cliente = commands.Bot(command_prefix='s!')

estado = True


@cliente.event
async def on_ready():
    print('Connected to bot: {}'.format(cliente.user.name))
    print('Bot ID: {}'.format(cliente.user.id))


@cliente.command()
async def helloworld(ctx):
    lista = [1500555555555555555555555, 400047777866444444444865,
             344444466666656666874, 77854122233544]
    while estado:
        numero = random.choice(lista)
        await ctx.send(numero)
    # await ctx.send("entro")

cliente.run(TOKEN)
