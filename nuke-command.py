#Nuke command
@bot.command()
@commands.guild_only()
@commands.bot_has_permissions(manage_channels=True)
async def nuke(ctx): 
  if ctx.message.author.guild_permissions.manage_channels:
    nuke_channel = ctx.message.channel
    nuker = ctx.message.author
    pos = ctx.message.channel.position
    new_channel = await nuke_channel.clone(reason=f"Nuked by {nuker}")
    await new_channel.edit(position=pos)
    await nuke_channel.delete()
    embed=discord.Embed(title="Channel has been nuked :fire:", color=0xff8800)
    embed.set_image(url="https://cdn.discordapp.com/attachments/866029434744864789/884424908803817562/ezgif.com-gif-maker_1.gif")
    await new_channel.send(embed=embed)
  else:
    await ctx.send("<:cross:896786711995121745> You don't have the permission to use this command") 
