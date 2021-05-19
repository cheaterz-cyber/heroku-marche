import os

import discord
from dotenv import load_dotenv

load_dotenv (dotenv_path="config")

default_intents = discord.Intents.default ()
default_intents.members = True
client = discord.Client (intents=default_intents)


@client.event
async def on_ready():
    print ("Le bot est pret.")


@client.event
async def on_message(message):
    if message.content.startswith ("!delete"):
        number = int (message.content.split ()[1])
        messages = await message.channel.history (limit=number + 1).flatten ()

        for each_message in messages:
            await each_message.delete ()


@client.event
async def on_member_join(member):
    general_channel: discord.TextChannel = client.get_channel (844293059859447808)
    await general_channel.send (content=f"Bienvenue à toi sur le serveur Yadso @{member} ! Bonne amusement ! ")
    member.roles.add("831665246292279306")


client.login(process.env.CLÉE)
