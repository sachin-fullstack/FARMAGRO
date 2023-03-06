import random

# Define a dictionary of possible chatbot responses
responses = {
    "hello": ["Hello!", "Hi there!", "Greetings!"],
    "how are you": ["I'm doing well, thank you.", "I'm great, thanks for asking!"],
    "what's your name": ["My name is Chatbot.", "I go by the name of Chatbot."],
    "goodbye": ["Goodbye!", "See you later!", "Until next time!"]
}

# Define a function to respond to user input
def respond(message):
    # Convert user input to lowercase
    message = message.lower()
    
    # Check if the user input matches any of the keys in the dictionary
    for key in responses.keys():
        if message in key:
            # If a match is found, randomly select a response from the list of possible responses
            return random.choice(responses[key])
    
    # If no match is found, return a default response
    return "I'm sorry, I don't understand. Please try again."

# Define a loop to continually prompt the user for input and respond
while True:
    user_input = input("You: ")
    bot_response = respond(user_input)
    print("Chatbot:", bot_response)
