import random

responses = {
    "hello": ["Hello!", "Hi there!", "Hey budy!", "Hey Hi"],
    "how are you": ["I'm good, thanks!", "I'm doing well, how about you?", "Pretty good, thanks for asking!"],
    "goodbye": ["Goodbye!", "See you later!", "Bye budy!"],
    "thanks": ["You're welcome!", "No Worries!", "Anytime!"]

}

def get_responses(user):
       message = user.lower()
       if message in responses:
              return random.choice(responses[message])
       else:
              return "I didn't understand come again"

def main():
    print("Welcome to Simple Chatbot! ")
    print("You can start chatting with the bot")
    print("Enter exit to leave..!")
    while True:
        user = input("You: ")
        if user.lower() == "exit":
           print("Bot: Good Bye! Have a great day..:)")
           break
        response = get_responses(user)
        print("Bot:",response)


if __name__ == "__main__":
    main()