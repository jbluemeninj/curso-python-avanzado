import webbrowser

import requests
import json

BASE_URL = "https://pokeapi.co/api/v2/pokemon/"

def get_pokemon_info(pokemon_name):
    api_url = BASE_URL + pokemon_name.lower()
    response = requests.get(api_url)

    try:
        pokemon_data = json.loads(response.text)
        sprites  = pokemon_data["sprites"]
        pokemon_image = sprites['front_default']
        webbrowser.open(pokemon_image)
    except:
        print("Error: Pokemon not found")

if __name__ == "__main__":
    pokemon_name = input("Enter a Pokemon name: ")
    get_pokemon_info(pokemon_name)