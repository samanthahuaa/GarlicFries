from flask import Flask, session, render_template, request, redirect
from datetime import datetime, timedelta
# from urllib import request # can not do "import request"
import requests
import random
import json

app = Flask(__name__)

# LOVE CALC
def calculate_love(fname, sname, result):
    key = ""
    with open("keys/key_love_calculator.txt", "r") as f:
        key = f.read()
    url = "https://love-calculator.p.rapidapi.com/getPercentage"
    querystring = {"fname":fname, "sname":sname}
    headers = {
        "X-RapidAPI-Key": key,
        "X-RapidAPI-Host": "love-calculator.p.rapidapi.com"
    }
    data = requests.get(url, headers=headers, params=querystring) #gets data from the website

    if result == "yes":
        multiplier = 1.2
    else:
        multiplier = 0.8

    percentage = float(json.loads(data.text)["percentage"]) * multiplier #data.text turns data into a string, json.loads converts json string to dictionary
    text_result = json.loads(data.text)["result"]

    return [percentage, text_result]
    ############################ do we even need the text_result?
    # render_template("main.html", url=url, e=explanation)

# print(calculate_love("John", "Alice", False))
# print(calculate_love("John", "Alice", True))

# SUNSET SUNRISE
def sunset_sunrise():
    rand = random.randint(0,1)
    sun = ""
    if rand == 0:
        sun = "sunset"
    else:
        sun = "sunrise"
    days = random.randint(7,14)
    date = str(datetime.now() + timedelta(days))
    # date looks like this 2022-12-22 17:06:16.372884 so we need to truncate it
    date = date[:10]
    url = f"https://api.sunrise-sunset.org/json?date={date}&lat=40.7699&long=-73.9753" # lat long is for the central park carousel
    data = requests.get(url) #gets data from the website
    # percentage = json.loads(data.text)["percentage"] #data.text turns data into a string, json.loads converts json string to dictionary
    time = json.loads(data.text)["results"][sun]
    img_date = ""
    
    if "PM" in time:
        time = "Sunset"
        img_date = "https://secretnyc.co/wp-content/uploads/2022/03/New-Project-9.png"
    else:
        time = "Sunrise"
        img_date = "https://media.timeout.com/images/101886667/750/422/image.jpg"
    return [date, time, img_date]

# print(sunset_sunrise())

# YES/NO
def yes_no():
    url = "https://yesno.wtf/api"
    data = requests.get(url) #gets data from the website
    answer = json.loads(data.text)["answer"] #data.text turns data into a string, json.loads converts json string to dictionary
    image = json.loads(data.text)["image"]

    if answer == "no":
        answer = "Uh oh, the gift was not well received..."
    else:
        answer = "LETS GOOOOOOOO. The gift was well received!"
    return [answer, image]

# print(yes_no())

# FAKE STORE
# title and description are kind of wonky.
def get_item():
    x = random.randint(1,20) # the api only has 20 products. the exact number is important for the link (the first item is 1)
    url = f"https://fakestoreapi.com/products/{x}"
    data = requests.get(url) #gets data from the website
    title = json.loads(data.text)["title"] # data.text turns data into a string, json.loads converts json string to dictionary
    price = json.loads(data.text)["price"]
    description = json.loads(data.text)["description"]
    image = json.loads(data.text)["image"]
    return [title, price, description, image]

# print(get_item())
    

if __name__ == "__main__":
    app.debug = True
    app.run()
