@bot.command()
@commands.guild_only()
@commands.bot_has_permissions(manage_messages=True)
async def say(ctx, *, arg):
  if ctx.message.author.guild_permissions.administrator:
    if arg == None:
      await ctx.send("<:cross:896786711995121745> Please define what you want to say")
    else:
      quote_text = '{}'.format(arg)
      await ctx.send(quote_text)
      await ctx.message.delete()
