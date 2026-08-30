"""
CodeAlpha Python Programming Internship
Task 4: Basic Chatbot

A simple rule-based chatbot that responds to predefined user inputs
like greetings, small talk, and farewells.

Key Concepts Used: if-elif, functions, loops, input/output.
"""

import random

# Predefined responses grouped by intent.
# Each intent maps to a list of trigger phrases and a list of possible replies.
RESPONSES = {
    "greeting": {
        "triggers": ["hello", "hi", "hey", "hiya", "good morning", "good evening"],
        "replies": ["Hi there!", "Hello!", "Hey! Good to see you."],
    },
    "how_are_you": {
        "triggers": ["how are you", "how's it going", "how are you doing"],
        "replies": ["I'm fine, thanks! How about you?", "Doing great, thanks for asking!"],
    },
    "name": {
        "triggers": ["what is your name", "what's your name", "who are you"],
        "replies": ["I'm a simple rule-based chatbot built for a CodeAlpha task.", "You can call me ChatBot!"],
    },
    "thanks": {
        "triggers": ["thank you", "thanks", "thx"],
        "replies": ["You're welcome!", "No problem at all!", "Anytime!"],
    },
    "help": {
        "triggers": ["help", "what can you do"],
        "replies": [
            "I can chat about simple things like greetings and how you're doing. "
            "Try saying 'hello', 'how are you', or 'bye'."
        ],
    },
    "bye": {
        "triggers": ["bye", "goodbye", "see you", "exit", "quit"],
        "replies": ["Goodbye!", "See you later!", "Bye! Take care."],
    },
}

DEFAULT_REPLIES = [
    "Sorry, I didn't understand that. Could you rephrase?",
    "I'm not sure how to respond to that yet.",
    "Hmm, I don't have an answer for that. Try 'help' to see what I can do.",
]


def get_response(user_input):
    """
    Determine which predefined intent (if any) matches the user's input,
    and return an appropriate reply. Returns None if the input matches
    the 'bye' intent, signaling the chat should end.
    """
    text = user_input.lower().strip()

    for intent, data in RESPONSES.items():
        for trigger in data["triggers"]:
            if trigger in text:
                reply = random.choice(data["replies"])
                is_farewell = intent == "bye"
                return reply, is_farewell

    return random.choice(DEFAULT_REPLIES), False


def main():
    print("=" * 40)
    print("SIMPLE RULE-BASED CHATBOT")
    print("=" * 40)
    print("Type 'bye' to end the conversation.\n")

    while True:
        user_input = input("You: ").strip()

        if not user_input:
            print("Bot: Please type something!")
            continue

        reply, is_farewell = get_response(user_input)
        print(f"Bot: {reply}")

        if is_farewell:
            break


if __name__ == "__main__":
    main()
