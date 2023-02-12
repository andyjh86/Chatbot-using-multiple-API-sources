import threading
import requests
import sys
import time
import random

#some general instructions when the code is started
print("type help for a list of commands \n \n \n WELCOME TO ANDYS BOT :-D \n \n type help for a list of commands \n \n")

#this is where the API keys are kept
ninjaapi = '*********PUT_API_KEY_HERE*********'
weatherapi = '*****PUT_WEATHER_API_HERE*******'

#this is where ive defined a check to ensure sys exit only works on bye input
def check_exit_input(input_string:str):
    if input_string.lower() == "bye":
        print("Goodbye!")
        sys.exit()
 #      
 #this is where the function get_fact is defined
 #
def get_fact():
    limit = 1
    api_url = 'https://api.api-ninjas.com/v1/facts?limit={}'.format(limit)
    response = requests.get(api_url, headers={'X-Api-Key': ninjaapi})
    if response.status_code == 200:        
        print(response.text, end='\n \n anything else?:')       
    else:
        print("Error:", response.status_code, response.text)
        time.sleep(1)
        print("\n")
#
#this is where the function get_joke is defined
#
def get_joke():
    limit = 1
    api_url = 'https://api.api-ninjas.com/v1/jokes?limit={}'.format(limit)
    response = requests.get(api_url, headers={'X-Api-Key': ninjaapi})
    if response.status_code == 200: 
        print(response.text, end='\n \n anything else?:')                
    else:
        print("Error", response.status_code, response.text)
        time.sleep(2)
#
#weather command with api key from open weather
#
def get_weather():
    # API Key
    weather_api = weatherapi
    # Location
    city = "Woolloongabba,AU"
    state = "Queensland"
    postcode = "4102"
    # API endpoint
    url = f"https://api.weatherapi.com/v1/current.json?key={weather_api}&q={city},{state},{postcode}"
    # Send the request and get the response
    response = requests.get(url)
    # Convert the response to json
    data = response.json()
    # Get the relevant information from the json
    weather = data["current"]["condition"]["text"]
    temperature = data["current"]["temp_c"]
    chance_of_rain = data["current"]["precip_mm"]    
    if chance_of_rain > 0:
        print(f"The current weather in Woolloongabba, {state}, {postcode} is {weather} with a temperature of {temperature} degree celsius and chance of rain today.")
    else:
        print(f"The current weather in Woolloongabba, {state}, {postcode} is {weather} with a temperature of {temperature} degree celsius and no chance of rain today.")
 
#       
#dad joke
#
def get_dadjoke():
    limit = 1
    api_url = 'https://api.api-ninjas.com/v1/dadjokes?limit={}'.format(limit)
    response = requests.get(api_url, headers={'X-Api-Key': ninjaapi})
    if response.status_code == requests.codes.ok:
        print(response.text, end='\n \n anything else?:')
    else:
        print("Error:", response.status_code, response.text)


#
#guess number game 
#
def guess_number():
    print("Welcome to the number guessing game! Guess a number between 1 and 10.")
    secret_number = random.randint(1, 10)
    while True:
        guess = input("Your guess: ")
        if guess.lower() == "back":
            return
        try:
            guess = int(guess)
            if guess == secret_number:
                print("Congratulations, you guessed the number!")
                return
            elif guess < secret_number:
                print("Too low, try again!")
            else:
                print("Too high, try again!")
        except ValueError:
            print("Invalid input, please enter a number or 'back' to return to the main loop.")

"""
EXTRA IMPORTANT 
#
#this is where the users input is defined so they can call either a joke or a fact
#
EXTRA IMPORTANT
"""
def user_input():
    while True:
        user_input = input("entry: ")
        if user_input.lower() == "help":
            print("Welcome to Andys Bot :-D \n type fact for a random fact \n joke for a random joke \n number to play the number guessing game \n and bye to exit the program \n NEW weather to get the current weather forcast for Woolloongabba \n NEW dad to get random dad joke")
            time.sleep(1)
        elif user_input.lower() == "fact":
            t1 = threading.Thread(target=get_fact)
            t1.start()
        elif user_input.lower() == "joke":
            t2 = threading.Thread(target=get_joke)
            t2.start()
        elif user_input.lower() == "weather":
         t3 = threading.Thread(target=get_weather)
         t3.start()
        elif user_input.lower() == "dad":
         t4 = threading.Thread(target=get_dadjoke)
         t4.start()    
        elif user_input.lower() in ["bye", "close", "exit", "see ya"]:
            input("bye")
            sys.exit()
        elif user_input.lower() == "number":
            guess_number()
        else:
            print("Sorry, I don't know that. \n")

#this is the, code that allows the user to input words

user_input()
