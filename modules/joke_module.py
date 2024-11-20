import json
import random

def get_random_joke():
    try:
        print("Loading jokes from file...")
        with open('data/jokes.json', 'r') as file:
            jokes = json.load(file)
            print(f"Successfully loaded {len(jokes)} jokes.")
        return random.choice(jokes)
    except FileNotFoundError:
        print("Error: jokes.json file not found.")
        return "Sorry, I couldn't find any jokes right now."
    except json.JSONDecodeError as e:
        print(f"Error loading JSON: {e}")
        return "Sorry, there seems to be a problem with the jokes file."
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return "Sorry, something went wrong while fetching a joke."
