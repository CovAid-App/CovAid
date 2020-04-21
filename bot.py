import os
try:
    os.remove("db.sqlite3")
    os.remove("sentence_tokenizer.pickle")
except FileNotFoundError:
    pass

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from datetime import date
import json
import requests
import pycountry

# use covid19api to get data
covid19 = requests.request("GET", "https://api.covid19api.com/summary")

# create a new ChatBot using chatterbot
chatbot = ChatBot(
    "CovAid",
    logic_adapters=[
        "chatterbot.logic.BestMatch"
    ]
)

# create a ListTrainer
trainer = ListTrainer(chatbot)

# List of item that need to trained
trainer.train(['covid death global', f'As of {date.today()}, there are {covid19.json()["Global"]["TotalDeaths"]} deaths caused by COVID-19 worldwide'])
trainer.train(['covid confirmed global', f'As of {date.today()}, there are {covid19.json()["Global"]["TotalConfirmed"]} confirmed cases of COVID-19 worldwide.'])
trainer.train(['covid tips', f'1. STAY home as much as you can; 2. KEEP a safe distance; 3. WASH hands often 4. COVER your cough 5. SICK? Call ahead'])
trainer.train(['what is covid-19?', f'Coronavirus disease 2019 (COVID-19) is an infectious disease caused by severe acute respiratory syndrome coronavirus 2 (SARS-CoV-2). -- Wikipedia'])
trainer.train(['definition for covid19', f'Coronavirus disease 2019 (COVID-19) is an infectious disease caused by severe acute respiratory syndrome coronavirus 2 (SARS-CoV-2). -- Wikipedia'])
trainer.train(['info', f'For absolute emergency, please dial **9-1-1** immediately, or your countries\' emergercy hotline. Please visit https://cdc.gov and https://who.int for accurate information.'])
trainer.train(['symptoms', f"Common symptoms: fever. tiredness. dry cough.\nSome people may experience: aches and pains. nasal congestion. runny nose. sore throat. diarrhoea."])
trainer.train(['who are you?', f"I'm CovAid Bot! With responsibility to provide accurate information during this COVID-19 Pandemic. To ask a question, <@!701186191940255785> with your question!"])
trainer.train(['What language are you programmed in?', f"I'm programmed in Python!"])
trainer.train(['donate', f"Thanks for your generosity, and no matter how much did you contribute, your contribution will fully go to COVID-19 fund. Go to this website to donate: https://covid19responsefund.org/"])
trainer.train(['is covid-19 present in animals?', f"According to multiple science research paper, they predict that it come from bat."])


# get response from the chatbot
def get_response(message):
    """
    Get response from the chatbot

    Args:
        message (str): the message that you want to get the response

    Returns:
        answer (str): the message responded from the chatbot
    """
    response = chatbot.get_response(message)
    print(response)
    return response


# get the country data
def country_data(sentence):
    """
    Check a sentence see if it ask for any country's data

    Args:
        sentence (str): the sentence that you want to check

    Returns:
        bool (False) if sentence doesn't contain data
        Tuple (value, date, country, keyword) if sentence does contain data
    """

    # split the word based on the single-space
    words = sentence.split()

    # setup country, keyword variable for later use
    country = False
    keyword = False

    # loop through the list of country from pycountry.countries
    for i in list(pycountry.countries):

        # see if each individual country name is in the sentence, if so, country variable equal to country code (2)
        if i.name in sentence:
            country = i.alpha_2

    # check if any word matches with keyword
    for word in words:
        if word in ['NewConfirmed', 'TotalConfirmed', 'NewDeaths', 'TotalDeaths', 'NewRecovered', 'TotalRecovered']:
            keyword = word

    # if both country and keyword variable are not False, proceed
    if country != False and keyword != False:

        # get response from covid19api (summary route)
        url = "https://api.covid19api.com/summary"
        response = requests.request("GET", url)

        # loop through each individual countries dict
        for ctry in response.json()['Countries']:

            # if country code matches country
            if ctry['CountryCode'] == country:

                # return info
                return ctry[keyword], ctry['Date'], country, keyword

    # return False by default
    return False
