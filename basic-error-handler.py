@bot.event
async def on_command_error(ctx, error):
    await ctx.send(f"<:cross:896786711995121745> An error occured: `{str(error)}`")   
