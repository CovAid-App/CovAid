import discord
from bot import get_response, country_data
from test import test_bot
from termcolor import colored
import os

# start a new discord client
client = discord.Client()

# run the test first
tests = {'what is covid-19?': 'Coronavirus disease 2019 (COVID-19) is an infectious disease caused by severe acute respiratory syndrome coronavirus 2 (SARS-CoV-2). -- Wikipedia'}
correct, total = test_bot(tests)

correct = round(correct / total, 2)
print(colored('Correct: ' + str(correct) + '%', 'green'))
print(colored('Incorrect: ' + str(round(1 - correct, 2)) + '%', 'red'))

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
        resp = str(message.content).split("<@!701186191940255785>")[1]

        # if question is tips
        if resp == " tips":

            # send a message with tips.png
            await message.channel.send('Here are the 5 tips to avoid getting COVID-19', file=discord.File('tips.png'))

        # pass through country_data function and if not False
        elif country_data(resp) != False:

            # get the output from that function and send the message, and send the message
            value, date, country, keyword = country_data(resp)
            await message.channel.send(f'As of {date}, in {country}, {keyword} is {value}.')

        # if it none of these, use regelar ChatBot
        else:
            await message.channel.send(str(get_response(resp)))

# return the client using this client id
client.run("NzAxMTg2MTkxOTQwMjU1Nzg1.XqYd-w.UQBkrfHsS1s_6a7hNP1fpf5xrhw")