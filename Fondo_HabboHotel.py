import discord
from discord.ext import commands
from urllib.request import urlopen

from PIL import Image, ImageDraw, ImageFont
import io
import requests
from datetime import datetime
 
 
bot = commands.Bot(command_prefix='!', description="ayuda bot") #Comando
bot.remove_command("help") # Borra el comando por defecto !help
 
 
@bot.command()
async def fondo(ctx):
    data = urlopen(f"https://www.habbo.es/gamedata/external_variables/bdc1f0fb26a966d366ce784882eb9bfb450dbe75").read().decode('utf-8')
    for linea in data.split('\n'):
        if linea.startswith(f"landing.view.background_left.uri") or linea.startswith(f"landing.view.background_left.uri"):
            k,fondohabbo = linea.split(f"=")

            imagen = Image.open(io.BytesIO(requests.get(fondohabbo).content))
            with io.BytesIO() as imagen_binary:
                imagen.save(imagen_binary, 'PNG')
                imagen_binary.seek(0)

                embed=discord.Embed(title="Fondo habbo Hotel", description=f"Imagen", timestamp=datetime.utcnow(), color=discord.Colour.random())

    
                embed.set_image(url=f"attachment://fondo_HabboHotel.png")
                embed.set_footer(text="BOT Programado Por Jose89fcb")
                await ctx.send(embed=embed, file=discord.File(fp=imagen_binary, filename=f"fondo_HabboHotel.png"))


       
       

    
 
 
 
@bot.event
async def on_ready():
    print("BOT listo!")
    
 
    
bot.run('') #OBTEN UN TOKEN EN: https://discord.com/developers/applications

