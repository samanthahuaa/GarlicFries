from flask import Flask, session, render_template, request, redirect
from datetime import datetime, timedelta
# from urllib import request # can not do "import request"
import requests
import random
import json

app = Flask(__name__)

# NBA PLAYER STATS
# WARNING: Not all players will have height_feet, height_inches, or weight_pounds. --> very few do
def player_stats():
    player_id = random.randint(1,3092) # the api only has 3092 products. the exact number is important for the link (the first item is 1)
    url = f"https://www.balldontlie.io/api/v1/players/{player_id}"
    data = requests.get(url) #gets data from the website
    fname = json.loads(data.text)["first_name"] # data.text turns data into a string, json.loads converts json string to dictionary
    lname = json.loads(data.text)["last_name"]
    name = fname + " " + lname
    position = json.loads(data.text)["position"] # not all players have position either
    if len(position) == 0:
        position = "Position of player is not available"
    teamname = json.loads(data.text)["team"]["name"]

    avg_games_played = player_stats_helper(player_id)
    # average_games_played = player_stats_helper(player_id)
    return [name, position, teamname, avg_games_played]

# average games played per season
def player_stats_helper(id): # want id to be an argument so that we can use this for a specific player
    res = requests.get(f"https://www.balldontlie.io/api/v1/season_averages?player_ids[]={id}")
    res = res.json()
    data = res.get("data")
    if len(data) != 0:
        return data[0]["games_played"]
    return "No data on player"

# print(player_stats())

if __name__ == "__main__":
    app.debug = True
    app.run()
