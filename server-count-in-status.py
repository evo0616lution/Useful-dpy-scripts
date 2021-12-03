@tasks.loop(seconds=300.0)
async def refresh():
  await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=f"{len(bot.guilds)} servers | +help"))

@bot.event
async def on_ready():
  time.sleep(1)
  print(f"Ready on {len(bot.guilds)} servers!")
  await bot.wait_until_ready()
  refresh.start()
