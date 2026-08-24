import discord
from discord.ext import commands
import random
import datetime
import os
intents = discord.Intents.default()
intents.message_content = True
intents.members = True  # necesario para algunos comandos

bot = commands.Bot(command_prefix="!", intents=intents)
bot.remove_command("help")
# ==================== LISTA DE INSULTOS Y RESPUESTAS ====================
insultos = [
    "pendejo", "idiota", "retrasado", "imbécil", "estupido", "estúpido",
    "tonto", "gilipollas", "cabron", "cabrón", "puto", "puta", "maricón",
    "marica", "subnormal", "mongolo", "down", "retras", "inútil", "basura",
    "mierda", "asco", "fracasado", "perdedor", "hijo de puta", "hdp",
    "cagon", "cagón", "lloron", "llorón", "pajero", "virgen", "nerd",
    "friki", "autista", "mongólico", "tarado", "loco", "enfermo"
]

respuestas = [
    "soy un pendejo con down",
    "Si señor me gusta el yupi",
    "soy un retrasado mental de mierda",
    "tengo el IQ de una piedra mojada",
    "soy un inútil que no sirve para nada",
    "me gusta que me digan pendejo",
    "sí señor, soy un mongolo",
    "tengo síndrome de down nivel dios",
    "soy la vergüenza de mi familia",
    "me chupo el dedo y me gusta",
    "soy un autista sin talento",
    "mi cerebro es un vacío absoluto",
    "soy más tonto que un saco de piedras",
    "me gusta el yupi y el jugo de naranja",
    "soy un pendejo certificado",
    "sí, soy un subnormal profundo",
    "tengo el coeficiente de un limón",
    "soy un fracaso ambulante",
    "me gusta que me humillen",
    "soy un idiota con gorra",
    "mi existencia es un error",
    "soy más inútil que un cenicero en moto",
    "sí señor, soy un retrasado",
    "tengo down y me enorgullezco",
    "soy un basura humana",
    "me gusta el yupi con pajita",
    "soy un pendejo de primera",
    "mi cerebro se quedó en el útero",
    "soy un mongólico funcional",
    "sí, soy un tarado total",
    "tengo menos neuronas que un gusano",
    "soy un desperdicio de oxígeno",
    "me gusta que me digan inútil",
    "soy un autista sin filtro",
    "mi IQ es negativo",
    "soy un pendejo con título",
    "sí señor me gusta el yupi y la mierda",
    "soy un retrasado con orgullo",
    "tengo el cerebro de un huevo frito",
    "soy más tonto que una puerta",
    "me gusta ser el payaso del grupo",
    "soy un fracaso total",
    "sí, soy un subnormal de manual",
    "tengo down y no me da vergüenza",
    "soy un pendejo que se cree inteligente",
    "mi existencia molesta a todos",
    "me gusta el yupi caliente",
    "soy un idiota con internet",
    "tengo menos sentido común que una piedra",
    "soy un basura que respira",
    "sí señor soy un mongolo feliz",
    "soy un retrasado mental profesional",
    "mi cerebro es papel mojado",
    "soy más inútil que un tenedor en sopa",
    "me gusta que me insulten",
    "soy un pendejo de élite",
    "tengo el IQ de un calcetín",
    "soy un autista que no entiende nada",
    "sí, soy un tarado de libro",
    "mi vida es un chiste malo",
    "me gusta el yupi con hielo",
    "soy un desperdicio de espacio",
    "tengo menos inteligencia que un tomate",
    "soy un pendejo orgulloso",
    "sí señor me gusta ser humillado",
    "soy un retrasado con wifi",
    "mi cerebro se fue de vacaciones",
    "soy más tonto que un sándwich",
    "me gusta el yupi y los insultos",
    "soy un subnormal con diploma",
    "tengo down nivel experto",
    "soy un fracaso que camina",
    "sí, soy un idiota completo",
    "mi coeficiente es el de una planta",
    "soy un pendejo que no se cansa",
    "me gusta que me digan basura",
    "soy un mongólico contento",
    "tengo el cerebro de un huevo",
    "soy un inútil de categoría",
    "sí señor soy un retrasado feliz",
    "me gusta el yupi y ser pendejo",
    "soy un autista sin esperanza",
    "mi existencia es irrelevante",
    "soy más tonto que un ladrillo",
    "tengo menos neuronas que un pez",
    "soy un pendejo con estilo",
    "sí, soy un tarado profesional",
    "me gusta ser el más tonto del chat",
    "soy un basura que habla",
    "tengo el IQ de un limón podrido",
    "soy un retrasado con ganas",
    "sí señor me gusta el yupi mucho",
    "mi cerebro es un desierto",
    "soy un fracaso con discord",
    "me gusta que me llamen mongolo",
    "soy un pendejo de alta gama",
    "tengo down y me río de ello",
    "soy un subnormal que responde",
    "sí, soy un idiota sin remedio",
    "me gusta el yupi y la humillación",
    "soy un desperdicio de bytes",
    "mi inteligencia es ficción",
    "soy más inútil que un cargador roto",
    "tengo el cerebro de un caracol",
    "soy un pendejo eterno",
    "sí señor soy un retrasado total",
    "me gusta ser insultado todos los días",
    "soy un autista que solo dice tonterías",
    "mi vida es un error de programación",
    "soy un mongolo con acceso a internet",
    "tengo menos sentido que un calcetín suelto",
    "soy un pendejo que nunca aprende",
    "sí, me gusta el yupi y ser down",
    "soy un tarado de categoría mundial",
    "mi existencia sobra",
    "me gusta que me digan que soy basura",
    "soy un retrasado con personalidad",
    "tengo el IQ de una tostadora",
    "soy un idiota que se lo cree",
    "sí señor soy un pendejo con down y me gusta"
]

# ==================== EVENTOS ====================
@bot.event
async def on_ready():
    print(f"Skull está online como {bot.user}")
    await bot.change_presence(activity=discord.Game(name="siendo un pendejo"))

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    contenido = message.content.lower()

    if "skull" in contenido or any(insulto in contenido for insulto in insultos):
        await message.channel.send(random.choice(respuestas))

    await bot.process_commands(message)

# ==================== 10 COMANDOS ÚTILES ====================

# 1. !ping → Muestra la latencia del bot
@bot.command()
async def ping(ctx):
    latencia = round(bot.latency * 1000)
    await ctx.send(f"Pong! Latencia: **{latencia}ms**\n(aunque soy un pendejo, al menos respondo rápido)")

# 2. !ayuda → Lista de comandos
@bot.command(aliases=["help", "comandos"])
async def ayuda(ctx):
    embed = discord.Embed(
        title="Comandos de Skull (el pendejo)",
        description="Aquí tienes lo poco útil que sé hacer:",
        color=discord.Color.dark_grey()
    )
    embed.add_field(name="!ping", value="Muestra la latencia", inline=False)
    embed.add_field(name="!dado [número]", value="Tira un dado (por defecto 6 caras)", inline=False)
    embed.add_field(name="!moneda", value="Cara o cruz", inline=False)
    embed.add_field(name="!decir <texto>", value="Hago que diga lo que quieras", inline=False)
    embed.add_field(name="!avatar [@usuario]", value="Muestra el avatar de alguien", inline=False)
    embed.add_field(name="!usuario [@usuario]", value="Info de un usuario", inline=False)
    embed.add_field(name="!server", value="Info del servidor", inline=False)
    embed.add_field(name="!insultame", value="Me insulto a mí mismo", inline=False)
    embed.add_field(name="!yupi", value="Confirmo que me gusta el yupi", inline=False)
    embed.add_field(name="!iq", value="Muestra mi IQ (spoiler: es bajo)", inline=False)
    embed.set_footer(text="Soy un pendejo con down, úsame con cuidado")
    await ctx.send(embed=embed)

# 3. !dado → Tira un dado
@bot.command()
async def dado(ctx, caras: int = 6):
    if caras < 2:
        await ctx.send("Ni yo soy tan pendejo como para tirar un dado de menos de 2 caras.")
        return
    resultado = random.randint(1, caras)
    await ctx.send(f"Tiraste un dado de {caras} caras y salió: **{resultado}**")

# 4. !moneda → Cara o cruz
@bot.command()
async def moneda(ctx):
    resultado = random.choice(["Cara", "Cruz"])
    await ctx.send(f"La moneda cayó en: **{resultado}**")

# 5. !decir → El bot repite lo que le digas
@bot.command()
async def decir(ctx, *, texto: str):
    await ctx.message.delete()
    await ctx.send(texto)

# 6. !avatar → Muestra el avatar de alguien
@bot.command()
async def avatar(ctx, miembro: discord.Member = None):
    miembro = miembro or ctx.author
    embed = discord.Embed(title=f"Avatar de {miembro.display_name}", color=miembro.color)
    embed.set_image(url=miembro.display_avatar.url)
    await ctx.send(embed=embed)

# 7. !usuario → Info de un usuario
@bot.command(aliases=["user", "info"])
async def usuario(ctx, miembro: discord.Member = None):
    miembro = miembro or ctx.author
    embed = discord.Embed(title=f"Info de {miembro}", color=miembro.color)
    embed.set_thumbnail(url=miembro.display_avatar.url)
    embed.add_field(name="ID", value=miembro.id, inline=True)
    embed.add_field(name="Nombre", value=str(miembro), inline=True)
    embed.add_field(name="Apodo", value=miembro.display_name, inline=True)
    embed.add_field(name="Cuenta creada", value=miembro.created_at.strftime("%d/%m/%Y"), inline=True)
    embed.add_field(name="Se unió", value=miembro.joined_at.strftime("%d/%m/%Y") if miembro.joined_at else "Desconocido", inline=True)
    embed.add_field(name="Roles", value=", ".join([r.mention for r in miembro.roles[1:]]) or "Ninguno", inline=False)
    await ctx.send(embed=embed)

# 8. !server → Info del servidor
@bot.command(aliases=["servidor"])
async def server(ctx):
    guild = ctx.guild
    embed = discord.Embed(title=f"Info de {guild.name}", color=discord.Color.blue())
    if guild.icon:
        embed.set_thumbnail(url=guild.icon.url)
    embed.add_field(name="Dueño", value=guild.owner.mention if guild.owner else "Desconocido", inline=True)
    embed.add_field(name="Miembros", value=guild.member_count, inline=True)
    embed.add_field(name="Canales", value=len(guild.channels), inline=True)
    embed.add_field(name="Creado el", value=guild.created_at.strftime("%d/%m/%Y"), inline=True)
    embed.add_field(name="ID", value=guild.id, inline=True)
    await ctx.send(embed=embed)

# 9. !insultame → El bot se insulta a sí mismo
@bot.command()
async def insultame(ctx):
    await ctx.send(random.choice(respuestas))

# 10. !yupi y !iq → Comandos temáticos del bot
@bot.command()
async def yupi(ctx):
    await ctx.send("Sí señor, me gusta el yupi~~\nSoy un pendejo con down y lo admito.")

@bot.command()
async def iq(ctx):
    iq_falso = random.randint(15, 55)
    await ctx.send(f"Mi IQ actual es: **{iq_falso}**\n(confirmado: soy un retrasado)")

# ==================== EJECUTAR ====================
bot.run(os.getenv("DISCORD_TOKEN"))
