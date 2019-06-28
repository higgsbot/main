import asyncio
import discord
import sys
sys.path.insert(0, '../libcurrency')
import stub as libcurrency

botToken = '' # Insert bot token here
currency = libcurrency.Token()
client = discord.Client()

@client.event


async def on_ready():
	print("Higgsbot ready")
	await currency.start()

@client.event
async def on_message(message):
	if message.author == client.user:
		return

	if message.content.startswith('higgs'):
		msgstr = message.content
		x = msgstr.split()
		# Command 0: Main higgs code
		if x[1] == "code":
			try:
				spend = int(x[2]) # Some god awful typecasting hack that kicks you out if x[2] isn't an integer 
				try: # Code execution happens in this block. Will send the entire code as a string to the correct container I guess...?
					currency.remove_tokens(message.author.id, int(x[2]))
					await message.channel.send("Used "+x[2]+" Codetokens.")
					await message.channel.send(x[3]+" is the language of this code")
					msgstr = msgstr.replace(x[0]+" "+x[1]+" "+x[2]+" "+x[3], '') # rids the other parameters from msgstr, which gives us code, which might or might not be encased with that fancy ``` box
					msgstr = msgstr.replace("```"+x[3], '') # This removes the fancy box
					msgstr = msgstr.replace("```", '') # This removes the fancy box
					await message.channel.send(msgstr)
				except Exception as e:
					await message.channel.send(e)
				return
			except:
				await message.channel.send("Invalid/Unknown command. Do `higgs help` for help")
				return
		# Command 1: Hello World
		if x[1] == "hello":
			await message.channel.send("Hello World")
			return
		# Command 2: sends content of a help file
		if x[1] == "help":
			f = open("help.txt", "r")
			await message.channel.send(f.read())
			f.close()
			return
		# Command 3: Codetoken management
		if x[1] == "codetoken": 
			if x[2] == "check":
				if int(currency.check_balance(message.author.id)) > 10:  # I'll add checking for mod privies later, but if deadline reaches, this rudimentary anti-abuse thing will do
					await message.channel.send(str(message.author)+" has more than 10 Codetokens. Rudimentary anti-abuse mechanism called to limit to 10 tokens. Sorry!")
					currency.set_balance(message.author.id, 10)
				await message.channel.send(str(message.author)+" has "+str(currency.check_balance("message.author"))+" Codetokens")
				return
			if x[2] == "add":
				try:
					currency.set_balance(message.author.id, currency.check_balance(message.author)+int(x[3]))
					await message.channel.send(str(message.author) +" now has "+str(currency.check_balance("message.author"))+" Codetokens")
				except:
					await message.channel.send("Failed to add tokens. Do `higgs help` for help")
				if int(currency.check_balance("message.author.id")) > 10:  # I'll add checking for mod privies later, but if deadline reaches, this rudimentary anti-abuse thing will do
					await message.channel.send(str(message.author)+" has more than 10 Codetokens. Rudimentary anti-abuse mechanism called to limit to 10 tokens. Sorry!")
					currency.set_balance(message.author, 10)
			else:
				await message.channel.send("Invalid/Unknown command. Do `higgs help` for help")
				return
		# Generic error message
		else:
			await message.channel.send("Invalid/Unknown command. Do `higgs help` for help")

client.run(botToken)
