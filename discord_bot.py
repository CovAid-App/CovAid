import discord
from bot import get_response, country_data

client = discord.Client()

step = 0
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    # print(message.author.id)
    if message.content.startswith('<@!701186191940255785>'):
        resp = str(message.content).split("<@!701186191940255785>")[1]
        if resp == " tips":
            await message.channel.send('Here are the 5 tips to avoid getting COVID-19', file=discord.File('tips.png'))
        elif country_data(resp) != False:
            value, date, country, keyword = country_data(resp)
            await message.channel.send(f'As of {date}, in {country}, {keyword} is {value}.')
        else:
            await message.channel.send(str(get_response(resp)))

client.run("NzAxMTg2MTkxOTQwMjU1Nzg1.Xput_Q.RfYNIL_rXjfYa0Or2D7LsHfcSD8")