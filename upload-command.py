@bot.command()
async def upload(ctx, *, arg = None):
    if arg != None:
        msg = await ctx.send("<a:loading:900379618924716052> Processing")
        url = postbin.postSync(f"{arg}")
        await msg.delete()
        await ctx.send(f"<:tick:896786712049614948> Text uploaded: {url}")
    else:
        await ctx.send("<:cross:896786711995121745> Please provide some text to upload")
