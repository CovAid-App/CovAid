import discord
from bot import get_response, country_data
from test import test_bot
from termcolor import colored
from track import get_grocery, best_time
import os
from datetime import datetime as date
import requests

# start a new discord client
client = discord.Client()

# run the test first
tests = {'what is covid-19?': 'Coronavirus disease 2019 (COVID-19) is an infectious disease caused by severe acute respiratory syndrome coronavirus 2 (SARS-CoV-2). -- Wikipedia'}
correct, total = test_bot(tests)

correct = round(correct / total, 2)
print(colored('Correct: ' + str(correct) + '%', 'green'))
print(colored('Incorrect: ' + str(round(1 - correct, 2)) + '%', 'red'))

day = date.today().strftime("%A")

# print in console of bot name
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

# do when receive a new message
@client.event
async def on_message(message):

    # if tagged the bot
    id = client.user.id
    if str(id) in message.content:

        # get the question
        resp = str(message.content).split("<@!701186191940255785> ")[1]

        # if question is tips
        if resp == "tips":

            # send a message with tips.png
            await message.channel.send('Here are the 5 tips to avoid getting COVID-19', file=discord.File('tips.png'))

        # pass through country_data function and if not False
        elif country_data(resp) != False:

            # get the output from that function and send the message, and send the message
            value, date, country, keyword = country_data(resp)
            await message.channel.send(f'As of {date}, in {country}, {keyword} is {value}.')

        elif 'grocery' in resp:
            import json
            place = str(resp).split("-")[1]
            geo = requests.get(f"https://api.opencagedata.com/geocode/v1/json?q={place}&key=485f61225dd041a9bae03a54cc0ef746").json()["results"][0]["geometry"]
            data, info = get_grocery(geo['lat'], geo['lng'])

            if resp.count('-') == 2:
                store = str(resp).split("-")[2]
                await message.channel.send(f'Best hour to visit: {best_time(info, data[store], day)}')
            elif resp.count('-') < 2:
                await message.channel.send(f"Here are the grocery store that is close to you: {data}. Which one do you like to go? ")

        # if it none of these, use regular ChatBot
        else:
            await message.channel.send(str(get_response(resp)))


# return the client using this client id
client.run("NzAxMTg2MTkxOTQwMjU1Nzg1.XqiXew.VU-Ou36jLBQJB9t1SIp7Y9tNWME")