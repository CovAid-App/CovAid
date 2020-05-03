# Cov-Aid Bot

Hello World, this is the repository for **CovAid** Bot. With mission to provide accurate information during COVID-19 Pandemic. This is a Discord bot that you can install to your server for free. 

## Getting Started

### Add to your own discord server
To install this Discord bot into your own Discord server, [click on this link](https://discordapp.com/oauth2/authorize?&client_id=701186191940255785&scope=bot&permissions=55296) to grant the authroization. You must be an administrator in order to add this bot. 

### Run this bot on your own bot.
First is clone this GitHub Repo:
```bash
git clone https://github.com/CovAid-App/CovAid.git
cd CovAid
```
then open `discord.py` and leave it aside for now.

First, make sure you have an discord account.

Then, go to [Discord Developer](https://discordapp.com/developers/applications), then click on "New Applications". Type a name and click "Create". Click in to the application, copy the client ID. Now click on the bot tab at the right side, click on "Create a Bot". Go ahead go to https://discordapp.com/oauth2/authorize?&client_id=[YOUR CLIENT ID]&scope=bot&permissions=55296 to add the discord bot to your own server. Navigate back to the bot tab, and copy the token.

Finally, navigate back `discord.py`, paste your token at the last line ( `client.run("YOUR TOKEN HERE")`).

To start this bot, you need to make sure you have `python3` and `pip` installed. (To install python, go to this [website](https://python.org), `pip` should come with `python`.) Then run following commands:
```bash
pip3 install -r requirements.txt
python3 discord_bot.py
```

First, in terminal, you should see the some green text and red text, that's the accuracy for the bot. Give it about 1 minutes or so to train the chatbot. And the bot should come online. 

### Use the bot
To use the bot, make sure to tag the bot (@CovAidBot), then type your question. You should receive the response within 10 seconds. If not, there might be some error happening. You can file an issue.

### Tests
To see all the tests available, you can go to `test.py`.

### Demo

## Features
Hello World! This is CovAid Bot! To ask me a question, please tag me then ask your question. There are a few feature included:
    1. **Just Chattin'** - You can ask some basic question about COVID-19, such as what is covid-19.
    2. **Country Data** - You can search for data in country. You must include country name and one of following keywords: NewConfirmed, TotalConfirmed, NewDeaths, TotalDeaths, NewRecovered, or TotalRecovered.
    3. **tips** -  Type `tips` you can see Public Announcement image made by Google/WHO about how to avoid getting COVID-19.
    4. **Where are the grocery near me?** - To search for the groceries near an address, you can type `grocery-<YOUR CITY NAME/ADDRESS>`. (Your Address will only be use for search grocery.)
    5. **When is the best time to visit grocery?** - To check the best time to visit a grocery, you can type `grocery-<YOUR CITY NAME/ADDRESS>-<GROCERY NAME>`.
    6. **Detect whether you have COVID-19?** - We also offered a few links to self-detect whether you have COVID-19 or not. Type detect to get the links.
Thanks for using this bot! We hope you get the info you need, and we will get through this unprecedented time together! :)

## Deployment

To Deploy this Discord bot, first see "Run this bot on your own bot".
Then go to [Heroku](https://heroku.com), login or register. Then create a new app, it's up to you the name for the app. Then make sure you have [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli#download-and-install) installed. Next, head back to your Terminal, then execute following command:
```bash
heroku login
heroku git:remote -a [YOUR APP NAME]
git add .
git commit -m "initial commit"
git push heroku master
```
Wait for about 1 or 2 minutes since there's a lot of packages to install. (trust me, a lot.) After it commited, go to [Heroku](https://heroku.com), open up your app, then click on the "Resource" tab on the top, you should see `worker python discord_bot.py`, click on the pencil button on the right, then toggle, click confirm. 

And now go to your server where your bot added, and about 1 minute or so, the bot should come back online, and you can ask your bot question!

## Built With

* [Discord.py](https://discordpy.readthedocs.io/en/latest/) - Discord Python Library
* [Google Maps API](https://developers.google.com/maps/documentation) - Dependency Management

## Contributing

Please read contribute.md for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/CovAid-App/CovAid/tags). 

## Authors

* **@boyuan12** - *Basic Chatbot, Country API, and tips features and popular time* - [boyuan12](https://github.com/boyuan12)
* **@GamingDevilsCC** - *String for detect* - [GamingDevilsCC](https://github.com/GamingDevilsCC)
* **@thafiona13** - *Worked on logo for this project and suggestobot* - [thafiona13](https://github.com/thafiona13)
* **@bornasadeghi** - *Worked on grocery w/Google Map API and popular time* - [bornasadeghi](https://github.com/bornasadeghi)

See also the list of [contributors](https://github.com/CovAid-App/CovAid/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the LICENSE file for details


## Acknowledgments

* Please, humanity, learn the lesson from nature, this disease won't just leave us, but let's work together to solve. Our planet is in danger, because we all know why this pandemic happened in the first place. And please, NASA, don't try to find another planet, because we will just destroy that planet like we did to Earth.