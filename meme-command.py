@bot.command()
async def meme(ctx):
    msg = await ctx.send("<a:loading:900379618924716052> Processing")
    r = requests.get('https://meme-api.herokuapp.com/gimme')
    x = r.text
    y = json.loads(x)
    title = y["title"]
    url = y["url"]
    author = y["author"]
    embed = discord.Embed(title=f"{title}", color=0x01f960)
    embed.set_image(url=url)
    embed.set_footer(text=f"Provided by {author}")
    await ctx.send(embed=embed)
    await msg.delete()
