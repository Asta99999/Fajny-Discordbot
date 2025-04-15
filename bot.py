import discord
import random
from botlogic import gen_emoji, flip_coin, gen_pass

# Zmienna intencje przechowuje uprawnienia bota
intents = discord.Intents.default()
# Włączanie uprawnienia do czytania wiadomości
intents.message_content = True
# Tworzenie bota w zmiennej klienta i przekazanie mu uprawnień
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Zalogowaliśmy się jako {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send('Cześć!')
    elif message.content.startswith('$usmiech'):
        await message.channel.send(gen_emoji())
    elif message.content.startswith('$moneta'):
        await message.channel.send(flip_coin())
    elif message.content.startswith('$haslo'):
        await message.channel.send(gen_pass(10))
    elif message.content.startswith('$random'):
        random_number = gen_random_number()  
        await message.channel.send(f'Losowa liczba: {random_number}')
    else:
        await message.channel.send("Nie rozumiem komendy.")


client.run("MTM1OTIxMzI1ODg4NzkyNTgzMA.G5U3Vf.9r2uxv_f8xQmF6loEkOj20wuRzKqXtbtAfOrI8")

