import discord
from discord.ext import commands
from model import get_class

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def check(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            file_name = attachment.filename
            file_url = attachment.url
            await attachment.save(f"./{attachment.filename}")
            await ctx.send(f"Guarda la imagen en ./{attachment.filename}")
                      
            try:
                clase = get_class (model_path="keras_model.h5", labels_path="labels.txt", image_path=f"./{file_name}")
                if clase[0] == "Palomas":
                    await ctx.send(f"Esto es una paloma, con porcentaje de probabilidad del {clase[1]*100}%")
                    await ctx.send("Las palomas pueden comer: Garbanzo, semillas, frutos ...")
                    await ctx.send("Las palomas suelen habitar en las ciudades y en montones")
                
                elif clase[0] == "Gorriones":
                    await ctx.send(f"Esto es una gorriones, con porcentaje de probabilidad del {clase[1]*100}%")
                    await ctx.send("Las palomas pueden comer: Semillas y granos ...")
                    await ctx.send("Las palomas suelen habitar en los campos y son solitarios")                
            
            except:
                await ctx.sent("Ha ocurrido un error en la clasificación")



    else:
        await ctx.send("Olvidaste subir la imagen :(")

bot.run("TU token")