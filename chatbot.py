import numpy as np
import nltk
from nltk.stem import PorterStemmer
import random

stemmer = PorterStemmer()

# Training dataset
intents = {
    "greeting": {
        "patterns": ["hi", "hello", "hey", "good morning", "good evening"],
        "responses": [
            "Hello!",
            "Hi there!",
            "Hey! How can I help you?",
            "Greetings!"
        ]
    },

    "goodbye": {
        "patterns": ["bye", "goodbye", "see you", "exit", "quit"],
        "responses": [
            "Bye!",
            "See you later!",
            "Take care!",
            "Goodbye!"
        ]
    },

    "thanks": {
        "patterns": ["thanks", "thank you", "thanks a lot", "appreciate it"],
        "responses": [
            "You're welcome!",
            "No problem!",
            "Glad to help!",
            "Anytime!"
        ]
    },

    "name": {
        "patterns": ["what is your name", "who are you", "your name"],
        "responses": [
            "I am a simple Python chatbot.",
            "You can call me ChatBot.",
            "I am your assistant chatbot."
        ]
    },

    "help": {
        "patterns": ["help", "can you help me", "support", "assist me"],
        "responses": [
            "Sure! How can I help you?",
            "I am here to help.",
            "Tell me your problem."
        ]
    },

    "about": {
        "patterns": ["what can you do", "about you", "your purpose"],
        "responses": [
            "I can chat with you and answer simple questions.",
            "I am designed using Python and NLP.",
            "I am a rule-based chatbot."
        ]
    }
}

def preprocess(sentence):
    tokens = sentence.lower().split()
    return [stemmer.stem(word) for word in tokens]

def chatbot_response(user_input):
    user_words = preprocess(user_input)

    for intent in intents:
        for pattern in intents[intent]["patterns"]:
            pattern_words = preprocess(pattern)
            if any(word in user_words for word in pattern_words):
                return random.choice(intents[intent]["responses"])

    return "Sorry, I didn't understand that."

print("Chatbot is running (type 'exit' to quit)")

while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        print("Bot: Goodbye!")
        break
    print("Bot:", chatbot_response(user_input))
