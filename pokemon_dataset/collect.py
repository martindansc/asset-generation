import requests
from os import path

f = open('./names.csv', 'r')

lines = f.readlines() 
  
count = 0
# Strips the newline character 
for line in lines:
    name = line.lower().rstrip()

    file_name = "./data/" + name + ".png"

    if not path.exists(file_name):
        url = "https://img.pokemondb.net/sprites/black-white/normal/" + name + ".png"
        
        picture_request = requests.get(url)
        if picture_request.status_code == 200:
            with open(file_name, 'wb') as f:
                f.write(picture_request.content)
        else:
            print("Could not get: " + name)

    