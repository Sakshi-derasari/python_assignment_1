# 1. Write a Python script to fetch a random joke from an API and display it on the console.
import requests

def get_random_joke():
    url = "https://official-joke-api.appspot.com/random_joke"
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad status codes
        joke = response.json()
        
        print("\nHere's a random joke for you:\n")
        print(joke["setup"])
        print(joke["punchline"])
    except requests.exceptions.RequestException as e:
        print("Error fetching joke:", e)

if __name__ == "__main__":
    get_random_joke()