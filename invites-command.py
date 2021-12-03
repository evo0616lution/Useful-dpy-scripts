@bot.command()
async def invites(ctx, usr: discord.Member=None):
    if usr == None:
       user = ctx.author
    else:
       user = usr
    total_invites = 0
    for i in await ctx.guild.invites():
        if i.inviter == user:
            total_invites += i.uses
    await ctx.send(f"<:tick:896786712049614948> {user.mention} has {total_invites} invite{'' if total_invites == 1 else 's'}")    
