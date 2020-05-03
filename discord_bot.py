import discord
from bot import get_response, country_data
from test import test_bot
from termcolor import colored
from track import get_grocery, best_time
import os
from datetime import datetime as date
import requests
from detect import test_string

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

        elif 'help' in resp:
            await message.channel.send(
            """
            Hello World! This is CovAid Bot! To ask me a question, please tag me then ask your question. There are a few feature included:
            1. **Just Chattin'** - You can ask some basic question about COVID-19, such as what is covid-19.
            2. **Country Data** - You can search for data in country. You must include country name and one of following keywords: NewConfirmed, TotalConfirmed, NewDeaths, TotalDeaths, NewRecovered, or TotalRecovered.
            3. **tips** Type `tips` you can see Public Announcement image made by Google/WHO about how to avoid getting COVID-19.
            4. **Where are the grocery near me?** - To search for the groceries near an address, you can type `grocery-<YOUR CITY NAME/ADDRESS>`. (Your Address will only be use for search grocery.)
            5. **When is the best time to visit grocery?** - To check the best time to visit a grocery, you can type `grocery-<YOUR CITY NAME/ADDRESS>-<GROCERY NAME>`.
            6. **Detect whether you have COVID-19?** - We also offered a few links to self-detect whether you have COVID-19 or not. Type `detect` to get the links.
            Thanks for using this bot! We hope you get the info you need, and we will get through this unprecedented time together! :)
            """)

        elif "detect" in resp:
            await message.channel.send(test_string)

        # if it none of these, use regular ChatBot
        else:
            await message.channel.send(str(get_response(resp)))


# return the client using this client id
client.run("NzAxMTg2MTkxOTQwMjU1Nzg1.Xq42IA.k30GI9Fm40xb9UHUR3G__r2SJIs")