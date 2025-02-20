import random

# Predefined chatbot responses
responses = {
    "hello": ["Hi there!", "Hello!", "Hey!", "Hi! How can I help?"],
    "how are you": ["I'm just a bot, but I'm doing great!", "I'm fine, thanks for asking!", "I'm here to assist you!"],
    "your name": ["I'm ChatBot!", "You can call me ChatBot.", "I'm just a friendly chatbot!"],
    "bye": ["Goodbye!", "See you later!", "Bye! Have a great day!"],
    "default": ["I'm not sure how to respond to that.", "Can you rephrase that?", "I don't understand."]
}

def get_response(user_input):
    """Get a response from the chatbot based on user input."""
    user_input = user_input.lower()
    for key in responses.keys():
        if key in user_input:
            return random.choice(responses[key])
    return random.choice(responses["default"])

def chat():
    """Start the chatbot conversation."""
    print("ChatBot: Hello! Type 'exit' to end the chat.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("ChatBot: Goodbye!")
            break
        response = get_response(user_input)
        print(f"ChatBot: {response}")

if __name__ == "__main__":
    chat()
