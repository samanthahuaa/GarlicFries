# get the key as a string

# love calculator
key = ""
with open("key_love_calculator.txt", "r") as file:
    key = file.read()

@app.route("/")
def display():
    url = f"={key}" # f string to append the required key
    disp = request.urlopen(url) # open the url, which is now a complete string with the required key
    #print(disp)
    dict = json.loads(disp.read()) # create python dict to store the JSON data presented on the NASA site
    
    return render_template('main.html', picture=dict['url'], explanation=dict['explanation']) # return the template and replace the required fields (picture's url and picture's explanation)