import json
import random

def get_mood_response(mood):
    try:
        print(f"Loading mood responses for mood: {mood}")
        with open('data/moods.json', 'r') as file:
            mood_responses = json.load(file)
            print(f"Successfully loaded mood responses for {mood}.")
        
        if mood in mood_responses:
            return random.choice(mood_responses[mood])
        else:
            print(f"No responses found for mood: {mood}.")
            return "Sorry, I don't have any responses for that mood."
    except FileNotFoundError:
        print("Error: moods.json file not found.")
        return "Sorry, I couldn't find any mood responses right now."
    except json.JSONDecodeError as e:
        print(f"Error loading JSON: {e}")
        return "Sorry, there seems to be a problem with the mood responses file."
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return "Sorry, something went wrong while fetching a mood response."