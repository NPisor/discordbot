import discord
from random import randrange
from discord.ext import commands

from settings import token

TOKEN = token

client = commands.Bot(command_prefix=".")


@client.event
async def on_ready():
    print("Bot is ready.")

@client.command(pass_context=True)
async def roll(ctx, *, sides):
    if sides == "d20":
        rollside = randrange(1,21)
        if rollside == 20:
            await client.say("You rolled a 20! Critical hit!")
        elif rollside == 1:
            await client.say("You rolled a 1! Critical miss!")
        else:
            await client.say("You rolled a " + str(rollside))
    if sides == "d12":
        await  client.say("You rolled a " + str(randrange(1,13)))
    if sides == "d6":
        await  client.say("You rolled a " + str(randrange(1,7)))
    if sides == "d4":
        await  client.say("You rolled a " + str(randrange(1,5)))

@client.command(pass_context=True)
async def lookup(ctx, *, item):
    if item == "switch":
        await client.say("https://www.nowinstock.net/videogaming/consoles/nintendoswitch/")
    if item == "ringfit":
        await  client.say("https://www.nowinstock.net/videogaming/games/ringfitadventure/")
    if item == "covid19":
        await client.say("Here are some recent COVID stats:  https://apify.com/covid-19")

@client.command(pass_context=True)
async def eat(ctx, *, food):
    await client.say("Let's all sit down and eat some " + food + "!")

client.run(TOKEN)