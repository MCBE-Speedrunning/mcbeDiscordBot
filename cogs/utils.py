from discord.ext import commands
from discord.ext import tasks
import discord
import requests
import json
import asyncio
import datetime
from datetime import timedelta


async def reportStuff(self, ctx, message):
	channel = self.bot.get_channel(715549209998262322)

	embed = discord.Embed(
				title=f"Report from {ctx.message.author.mention}",
				description=f"{message}", 
				color=16711680, timestamp=ctx.message.created_at)

	await channel.send(embed=embed)
	await ctx.send("Report has been submitted")

class Utils(commands.Cog):

	def __init__(self, bot):
		self.bot = bot

	@commands.command(description="Pong!", help="Tells the ping of the bot to the discord servers", brief="Tells the ping")
	async def ping(self, ctx):
		await ctx.send(f'Pong! {round(self.bot.latency*1000)}ms')

	@commands.cooldown(1, 25, commands.BucketType.guild)
	@commands.command()
	async def findseed(self, ctx):
		if ctx.message.channel.id != 684787316489060422:
			ctx.message.delete()
			return
		totalEyes = 0
		for i in range(12):
			randomness = random.randint(1,10)
			if randomness == 1:
				totalEyes += randomness
			else:
				continue
				
		# haha sneaky sneaky
		Thomas = self.bot.get_user(280428276810383370)
		if ctx.message.author == Thomas:
			totalEyes == 12
		
		await ctx.send(f"{ctx.message.author.display_name} -> your seed is a {totalEyes} eye")

	@findseed.error
	async def findseed_handler(self,ctx,error):
		if isinstance(error, commands.CommandOnCooldown):
			if ctx.message.channel.id != 684787316489060422:
				ctx.message.delete()
			return
			#await ctx.send(f"{ctx.message.author.display_name}, you have to wait {round(error.retry_after, 7)} seconds before using this again.")

	@commands.Cog.listener()
	async def on_message(self, message):
		if message.channel.id != 589110766578434078:
			return
		if message.author.bot:
			return
		badWords = ["fair", "f a i r", "ⓕⓐⓘⓡ", "ⓕ ⓐ ⓘ ⓡ"]
		count = 0
		
		coolKids = [
			['Cameron', self.bot.get_user(468262902969663488), datetime.date(2020, 10, 8)],
			['Indy', self.bot.get_user(274923326890311691), datetime.date(2020, 9, 10)],
			['Murray', self.bot.get_user(400344183333847060), datetime.date(2020, 11, 10)],
			# idk if she goes by her irl name but I'm sticking with it for the sake of uniformity
			# also idk how to pronounce prakxo
			['Samantha', self.bot.get_user(226312219787264000), datetime.date(2020, 6, 25)],
			['Scott', self.bot.get_user(223937483774230528), datetime.date(2020, 6, 23)],
			['Thomas', self.bot.get_user(280428276810383370), datetime.date(2020, 9, 29)]
		]
		
		
		# Luca plz dont remove the bottom code (just incase the new code doesnt work,
		# and also for me to laugh at how bad my code is)
		
		# brb while I write ugly and inefficient code in my
		# conquest to make Steve the Bot bloated and unworkable
		
		#if datetime.date.today() == datetime.date(2020, 6, 23):
		#	await scott.send('Happy Birthday Scott. You\'re a boomer now! :mango:')
		#elif datetime.date.today() == datetime.date(2020, 6, 25):
		#	await samantha.send('Happy Birthday Prakxo. You\'re a boomer now! :mango:')
		#elif datetime.date.today() == datetime.date(2020, 5, 28):
		#	await thomas.send('Testy Test :mango:')
		#elif datetime.date.today() == datetime.date(2020, 9, 29):
		#	await thomas.send('Now you know how the others felt :mango:')
		#elif datetime.date.today() == datetime.date(2020, 10, 8):
		#	await cameron.send('Happy Birthday Cameron. You\'re a boomer now! :mango:')
		#elif datetime.date.today() == datetime.date(2020, 11, 10):
		#	await murray.send('Happy Birthday Murray. You\'re a boomer now! :mango:')
		#elif datetime.date.today() == datetime.date(2020, 9, 10):
		#	await indy.send('Happy Birthday Indy. You\'re a boomer now! :mango:)
		
		# Ignore the above message. I got sick and tired of looking at trash code
		
		for coolKid in coolKids:
			if datetime.date.today() == coolKid[2]:
				await coolKid[1].send(f'Happy Birthday {coolKid[0]}! You\'re a boomer now! :mango:')
			
		for word in badWords:
			if word in message.content.lower():
				count += 1;
				fair = 'Fair '*count
		await message.channel.send(fair)

	@commands.cooldown(1, 60, commands.BucketType.member)
	@commands.command()
	async def report(self, ctx, *, message=None):
		if message == None:
			await ctx.send("Please type a report to report (hehe, sounds funny)")
		else:
			await reportStuff(self, ctx, message)

def setup(bot):
	bot.add_cog(Utils(bot))
