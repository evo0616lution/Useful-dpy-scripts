@bot.command(aliases=['8ball'])
async def _8ball(ctx, *, question):
  responses = [
  discord.Embed(title='It is certain.'),
  discord.Embed(title='It is decidedly so.'),
  discord.Embed(title='Without a doubt.'),
  discord.Embed(title='Yes - definitely.'),
  discord.Embed(title='You may rely on it.'),
  discord.Embed(title='Most likely.'),
  discord.Embed(title='Outlook good.'),
  discord.Embed(title='Yes.'),
  discord.Embed(title='Signs point to yes.'),
  discord.Embed(title='Reply hazy, try again.'),
  discord.Embed(title='Ask again later.'),
  discord.Embed(title='Better not tell you now.'),
  discord.Embed(title='Cannot predict now.'),
  discord.Embed(title='Concentrate and ask again.'),
  discord.Embed(title="Don't count on it."),
  discord.Embed(title='My reply is no.'),
  discord.Embed(title='My sources say no.'),
  discord.Embed(title='Outlook not very good.'),
  discord.Embed(title='Not at all.'),
  discord.Embed(title='Are you kidding me? Never!'),
  discord.Embed(title='Yes, Indeed!'),
  discord.Embed(title='Of course!'),
  discord.Embed(title='Nope'),
  discord.Embed(title="I don't want to answer this question."),
  discord.Embed(title='Very doubtful.')
    ]
  responses = random.choice(responses)
  await ctx.send(embed=responses)
