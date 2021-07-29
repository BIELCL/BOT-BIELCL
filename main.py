import discord
from discord import member 
from discord.ext import commands
import random

client = discord.Client()

@client.event
async def on_ready():
    print('ONLINE')
    print(client.user.name)
    print(client.user.id)

client = commands.Bot(command_prefix=".")

@client.command()
async def ajuda(ctx):
        await ctx.send(f'Ola, {ctx.author.mention} Para saber nossos comandos digite b/comandos')


@client.command()
async def peu(ctx):
        await ctx.message.delete()
        await ctx.send(f'https://cdn.discordapp.com/attachments/868329586436476959/869059221705084928/unknown.png')


@client.command()
async def zazel(ctx):
        await ctx.message.delete()
        await ctx.send(f'https://cdn.discordapp.com/attachments/868329586436476959/869060815955828806/0933fad6-310a-44b7-85bf-d8529dcde003.png')


@client.command()
async def bot(ctx):
    await ctx.send(
        f'{ctx.author.mention}  https://discord.com/oauth2/authorize?client_id=857612391393787914&permissions=8&scope=bot'
    )


@client.command()
async def comandos(ctx):
    await ctx.send(f'{ctx.author.mention} Comandos do bot:bot,say,ban,kick,limpar,dm.')


@client.command(aliases=['falar'])
async def say(ctx,  *, mensagem=None):
 if ctx.author.guild_permissions.administrator:
    if mensagem is None:
        await ctx.send(f'{ctx.author.mention} Eu não posso enviar uma mensagem em branco!')
    else:
        await ctx.message.delete()
        await ctx.send(f' {mensagem}')
 else:
     await ctx.send(f' :no_entry_sign: **|** {ctx.author.mention} Você não tem permissão para usar esse comando. ')




@client.command()
async def kick(ctx, membro: discord.Member, *, motivo=None):
    if ctx.author.guild_permissions.kick_members:
        msg = f'{ctx.author.mention} expulsou {membro.mention} por {motivo}'
        await membro.kick()
        await ctx.send(msg)
    else:
     await ctx.send(f' :no_entry_sign: **|** {ctx.author.mention} Você não tem permissão para usar esse comando. ')

@client.command()
async def ban(ctx, membro: discord.Member, *, motivo=None):
    if ctx.author.guild_permissions.ban_members:
        msg = f'{ctx.author.mention} baniu {membro.mention} por {motivo}'
        await membro.ban()
        await ctx.send(msg)
    else:
     await ctx.send(f' :no_entry_sign: **|** {ctx.author.mention} Você não tem permissão para usar esse comando. ')

@client.command()
async def limpar(ctx, quantidade=0):
  if ctx.author.guild_permissions.administrator:
    await ctx.channel.purge(limit=quantidade + 1)
    await ctx.send(f' :x: **|** {quantidade} Mensagens foram limpas por {ctx.author.mention}.')
  else:
   await ctx.send(f' :no_entry_sign: **|** {ctx.author.mention} Você não tem permissão para usar esse comando. ')


@client.event
async def on_ready():
    activity = discord.Game(name='BCL BOT', type=3)
    await client.change_presence(status=discord.Status.online,
                                 activity=activity)


@client.command()
async def ping(ctx):
    await ctx.send(f'{ctx.author.mention} :chart_with_upwards_trend: Ping! {round(client.latency * 1000)} ms :chart_with_downwards_trend:')


@client.command()
async def pv(ctx, member: discord.Member, *, content):
    channel = await member.create_dm()  
    await channel.send(content)  
    await ctx.message.delete()



@client.command()
async def dm(ctx, member: discord.Member, *, content):
    if ctx.author.guild_permissions.administrator:
        channel = await member.create_dm()  
        await ctx.send(f':incoming_envelope: **|** {ctx.author.mention} Sua Dm foi enviada para {member.mention}: {content} ')
        await channel.send(f"** ** {content}")  
    else:
     await ctx.send(f' :no_entry_sign: **|** {ctx.author.mention} Você não tem permissão para usar esse comando. ')


@client.command()
async def serverinfo(ctx):
    name = str(ctx.guild.name)
    description = str(ctx.guild.description)

    owner = str(ctx.guild.owner)
    id = str(ctx.guild.id)
    region = str(ctx.guild.region)
    memberCount = str(ctx.guild.member_count)
    voice_channels = len(ctx.guild.voice_channels)
    text_channels = len(ctx.guild.text_channels)
    channels = text_channels + voice_channels

    icon = str(ctx.guild.icon_url)

    embed = discord.Embed(
        title=" Informações do Servidor " + name,
        color=discord.Color.blue()
    )
    embed.set_thumbnail(url = str(ctx.guild.icon_url))
    embed.add_field(name="Dono", value=owner, inline=True)
    embed.add_field(name="Server ID", value=id, inline=True)
    embed.add_field(name="Membros", value=memberCount, inline=True)
    embed.add_field(name="Canais", value=channels, inline=True)
    embed.add_field(name="Texto", value=text_channels, inline=True)
    embed.add_field(name="Voz", value=voice_channels, inline=True)
    embed.add_field(name="Region", value=region, inline=True)

    await ctx.send(embed=embed)

@client.command()
@commands.has_permissions(administrator=True)
async def addcargo(ctx, member : discord.Member, role : discord.Role):
    await member.add_roles(role)
    await ctx.send(f" Cargo {role.mention} foi adicionado  para {member.mention}.")

@client.command()
@commands.has_permissions(administrator=True)
async def removercargo(ctx, member : discord.Member, role : discord.Role):
    await member.remove_roles(role)
    await ctx.send(f"Cargo {role.mention} foi removido de {member.mention}.")




