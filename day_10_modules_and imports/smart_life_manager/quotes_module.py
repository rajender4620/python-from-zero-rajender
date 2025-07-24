import random

quotes = [
    "Discipline is the bridge between goals and accomplishment.",
    "What you do today can improve all your tomorrows.",
    "Success doesn’t come from what you do occasionally, it comes from what you do consistently.",
    "Small habits lead to big changes.",
    "You don’t need more motivation, you need more discipline."
]


def show_quote():
    print("💡 Daily Quote:")
    print(random.choice(quotes))
