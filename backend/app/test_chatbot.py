from chatbot import get_chatbot_response

# Testing block: Run chatbot with user input
if __name__ == "__main__":
    print("Welcome to the Chatbot! Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "bye":
            print("Goodbye! See you next time.")
            break
        response = get_chatbot_response(user_input)
        print("Bot: ", response)
