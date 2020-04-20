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

url = "https://api.covid19api.com/summary"


headers = {}

covid19 = requests.request("GET", url, headers=headers)


chatbot = ChatBot(
    "CovAid",
    logic_adapters=[
        "chatterbot.logic.BestMatch"
    ]
)


trainer = ListTrainer(chatbot)


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



def get_response(message):
    response = chatbot.get_response(message)
    print(response)
    return response


def country_data(sentence):

    words = sentence.split()
    country = False
    keyword = False

    for i in list(pycountry.countries):
        if i.name in sentence:
            country = i.alpha_2

    for word in words:
        if word in ['NewConfirmed', 'TotalConfirmed', 'NewDeaths', 'TotalDeaths', 'NewRecovered', 'TotalRecovered']:
            keyword = word

    print(country, keyword)
    if country != False and keyword != False:
        url = "https://api.covid19api.com/summary"
        payload = {}
        headers= {}
        response = requests.request("GET", url, headers=headers, data = payload)
        for ctry in response.json()['Countries']:
            if ctry['CountryCode'] == country:
                return ctry[keyword], ctry['Date'], country, keyword
    return False
