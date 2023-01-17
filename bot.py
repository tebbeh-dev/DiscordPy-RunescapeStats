# Version 1.0 simple Discord bot pulling Runescape stats 
# Did it for me and my friends to simply see in discord rest of Group Ironman stats
# Will pull every relevant data possible by commands

# Current commands is:
# /stats - Full skill table and progress

import os
import discord
from dotenv import load_dotenv
import requests

# To build a table, there is probably better ways but this suits me for now
from tabulate import tabulate

# Include players here with their exact name
players = ['Tebby%A0Tubby', 'LolaGIM', 'Instantkarma', 'Javlabillig']

url0 = 'https://secure.runescape.com/m=hiscore_oldschool/index_lite.ws?player='

list = []

for player in players:
    
    # To make for loop stop after players is done
    count = 0

    # Result fetching data from API with url0 variable + player to finish the url
    res = requests.get(url0+player)
    
    # Rewrite Playernames, not important but suits me
    if player == 'Tebby%A0Tubby':
        player = 'tebbeh'
    elif player == 'LolaGIM':
        player = 'Lola'
    elif player == 'Instantkarma':
        player = 'Xaillen'
    elif player == 'Javlabillig':
        player = 'Backi'

    # 0 to 24 is the actual skills, rest should be bosses and other stuff you dont want
    data = (res.text).split('\n')[0:24]

    # Build the skill tree
    Skills = [['Skill', 'Level'],
              ['Overall', data[0].split(',')[1]],
              ['Attack', data[1].split(',')[1]],
              ['Defence', data[2].split(',')[1]],
              ['Strength', data[3].split(',')[1]],
              ['Hitpoints', data[4].split(',')[1]],
              ['Ranged', data[5].split(',')[1]],
              ['Prayer', data[6].split(',')[1]],
              ['Magic', data[7].split(',')[1]],
              ['Cooking', data[8].split(',')[1]],
              ['Woodcutting', data[9].split(',')[1]],
              ['Fletching', data[10].split(',')[1]],
              ['Fishing', data[11].split(',')[1]],              
              ['Firemaking', data[12].split(',')[1]],
              ['Crafting', data[13].split(',')[1]],
              ['Smithing', data[14].split(',')[1]],
              ['Mining', data[15].split(',')[1]],
              ['Herblore', data[16].split(',')[1]],
              ['Agility', data[17].split(',')[1]],
              ['Thieving', data[18].split(',')[1]],
              ['Slayer', data[19].split(',')[1]],
              ['Farming', data[20].split(',')[1]],
              ['Runecrafting', data[21].split(',')[1]],
              ['Hunter', data[22].split(',')[1]],
              ['Construction', data[23].split(',')[1]]]
    
    # Append the skill tree to an array of objects
    list.append(Skills)

    # when all players is looped break and keep going
    if count == len(players):
        break

# list is built like this list[player][skill][level]
# should make this whole table dynamic depending on where in array player is listed etc
table = [['Skills', 'tebbeh', 'Lola','Xaillen','Backi'], 
         ['Overall', list[0][1][1], list[1][1][1], list[2][1][1], list[3][1][1]],
         ['Attack', list[0][2][1], list[1][2][1], list[2][2][1], list[3][2][1]],
         ['Defence', list[0][3][1], list[1][3][1], list[2][3][1], list[3][3][1]],
         ['Strength', list[0][4][1], list[1][4][1], list[2][4][1], list[3][4][1]],
         ['Hitpoints', list[0][5][1], list[1][5][1], list[2][5][1], list[3][5][1]],
         ['Ranged', list[0][6][1], list[1][6][1], list[2][6][1], list[3][6][1]],
         ['Prayer', list[0][7][1], list[1][7][1], list[2][7][1], list[3][7][1]],
         ['Magic', list[0][8][1], list[1][8][1], list[2][8][1], list[3][8][1]],
         ['Cooking', list[0][9][1], list[1][9][1], list[2][9][1], list[3][9][1]],
         ['Woodcutting', list[0][10][1], list[1][10][1], list[2][10][1], list[3][10][1]],
         ['Fletching', list[0][11][1], list[1][11][1], list[2][11][1], list[3][11][1]],
         ['Fishing', list[0][12][1], list[1][12][1], list[2][12][1], list[3][12][1]],
         ['Firemaking', list[0][13][1], list[1][13][1], list[2][13][1], list[3][13][1]],
         ['Crafting', list[0][14][1], list[1][14][1], list[2][14][1], list[3][14][1]],
         ['Smithing', list[0][15][1], list[1][15][1], list[2][15][1], list[3][15][1]],
         ['Mining', list[0][16][1], list[1][16][1], list[2][16][1], list[3][16][1]],
         ['Herblore', list[0][17][1], list[1][17][1], list[2][17][1], list[3][17][1]],
         ['Agility', list[0][18][1], list[1][18][1], list[2][18][1], list[3][18][1]],
         ['Thieving', list[0][19][1], list[1][19][1], list[2][19][1], list[3][19][1]],
         ['Slayer', list[0][20][1], list[1][20][1], list[2][20][1], list[3][20][1]],
         ['Farming', list[0][21][1], list[1][21][1], list[2][21][1], list[3][21][1]],
         ['Runecrafting', list[0][22][1], list[1][22][1], list[2][22][1], list[3][22][1]],
         ['Hunter', list[0][23][1], list[1][23][1], list[2][23][1], list[3][23][1]],
         ['Construction', list[0][24][1], list[1][24][1], list[2][24][1], list[3][24][1]]]

# Get secret keys for running the bot in a .env file located in same folder as .py file
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

# Setting for letting bot answer with message
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

# Logs that bot actually running
@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} is connected!'
    )

# Command to pull the table when someone say /stats
# sendres is probably horribly made but best I could get for now to send the whole table
@client.event
async def on_message(message):
    if message.content == '/stats':   
        sendres = "```"+tabulate(table, headers='firstrow')+"```"
        await message.channel.send(sendres)
        
client.run(TOKEN)

