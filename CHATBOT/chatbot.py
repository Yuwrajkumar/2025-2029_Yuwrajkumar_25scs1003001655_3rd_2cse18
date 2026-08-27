                                               # Rule-Based Chatbot
                                               # Project - Task 1

import datetime

print("======================================")
print("       🤖 RULE-BASED CHATBOT")
print("======================================")
print("Bot: Hello! I am your chatbot.")
print("Bot: You can ask me simple questions.")
print("Bot: Type 'bye' to exit.\n")

while True:
    user_input = input("You: ").lower().strip()

                                             # Greeting
    if user_input == "hello" or user_input == "hi" or user_input == "hey":
        print("Bot: Hello! Nice to meet you.")

                                        # Asking chatbot's name
    elif "your name" in user_input or "who are you" in user_input:
        print("Bot: I am a simple rule-based chatbot.")

                                       # Asking user's name
    elif "my name" in user_input:
        name = input("Bot: What is your name? ")
        print("Bot: Nice to meet you, " + name + "!")

                                         # How are you
    elif "how are you" in user_input:
        print("Bot: I am doing great! Thanks for asking.")

                                         # Help
    elif "help" in user_input:
        print("Bot: You can ask me:")
        print("- Hello")
        print("- What is your name?")
        print("- How are you?")
        print("- What is the time?")
        print("- What is the date?")
        print("- Bye")

                                       # Time
    elif "time" in user_input:
        current_time = datetime.datetime.now().strftime("%I:%M:%S %p")
        print("Bot: The current time is", current_time)

                                       # Date
    elif "date" in user_input or "today" in user_input:
        current_date = datetime.datetime.now().strftime("%d-%m-%Y")
        print("Bot: Today's date is", current_date)

                                     # Thank you
    elif "thank" in user_input or "thanks" in user_input:
        print("Bot: You're welcome!")

                                     # Goodbye
    elif user_input == "bye" or user_input == "exit" or user_input == "quit":
        print("Bot: Goodbye! Have a great day.")
        break

                                # Unknown input
    else:
        print("Bot: Sorry, I don't understand that.")
        print("Bot: Type 'help' to see what I can understand.")