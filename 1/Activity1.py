import requests

def get_random_joke():
    url="http://www.official-joke-api.appspot.com/random_joke"
    response=requests.get(url)

    if response.status_code==200:
        #One line to print the JSON response
        print(f"Full JSON response is {response.json()}")
        joke_data=response.json()
        return f"{joke_data["setup"]} - {joke_data["punchline"]}"
    
    else:
        return"Failed to retrive joke"
    
def main():
    print("Welcome to random joke genarator")
    while True:
        user_input=input("Press enter key to get new jok or type q to quit").strip().lower()
        if user_input in("q" ,  "exit"):
            print("Goodbye")
            break
        joke=get_random_joke()
        print(joke)



