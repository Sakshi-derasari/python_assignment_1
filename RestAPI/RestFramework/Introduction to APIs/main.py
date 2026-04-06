import requests

def get_joke():
    url = "https://official-joke-api.appspot.com/random_joke"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        print("\n😂 Random Joke:\n")
        print(data["setup"])
        print(data["punchline"])
    else:
        print("Failed to fetch joke 😢")

# Run function
get_joke()