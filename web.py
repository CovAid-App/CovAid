from flask import Flask, render_template
import datetime
import pycountry
import requests
import json

from termcolor import colored

app = Flask(__name__)

@app.route("/")
def index():
    pass


@app.route("/track")
def trackobot():
    """Top 4 countries that have the most cases"""
    render_template("loading.html")
    today = datetime.date.today()
    day_7 = today - datetime.timedelta(days=7)
    day_1 = today - datetime.timedelta(days=1)

    country_data = {}
    top = []
    alpha2_to_slug = {}

    data = requests.get("https://coronavirus-19-api.herokuapp.com/countries").json()

    for i in range(1, 6):
        top.append(data[i]["country"])

    for i in (list(pycountry.countries)):
        for j in top:
            if j == i.name or j == i.alpha_3:
                alpha2_to_slug[i.alpha_2] = None

    co = requests.get("https://api.covid19api.com/countries").json()
    for key, value in alpha2_to_slug.items():
        for c in co:
            if c['ISO2'] == key:
                alpha2_to_slug[c["ISO2"]] = c["Slug"]

    current = requests.get("https://api.covid19api.com/summary").json()["Countries"]

    for key, value in alpha2_to_slug.items():
        info = requests.get(f"https://api.covid19api.com/country/{value}/status/confirmed?from={day_7}T00:00:00Z&to={day_1}T00:00:00Z").json()
        cases_avg = 0
        for i in info:
            cases_avg += i["Cases"]

        cases_avg /= 7

        for c in current:
            if c["NewConfirmed"] > cases_avg:
                country_data[value] = False
            else:
                country_data[value] = True

    # {slug: True/False flatten the curve}
    # return str(country_data)
    return render_template("track.html")


@app.route("/chat")
def chat():
    pass


@app.route("/suggest")
def suggest():
    pass


@app.route("/info")
def info():
    pass

