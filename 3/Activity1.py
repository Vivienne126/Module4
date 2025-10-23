import requests
url="https://uselessfacts.jsph.pl/random.json?language=en"
def get_random():
    response=requests.get(url)
    if response.status_code==200:
        fact_data=response.json()
        print(f"Did You Know {fact_data["text"]}")
    else:
        print("Failed to fetch text")

while True:
    user_input=input("Press enter for another fact or q to quit")
    if user_input.lower()=="q":
        break
    get_random()