name = input('What is your name?')
age = input('What is your age?')
location = input('Where do you live?')

print(f'Hello {name}. You are {age} years old and live in {location}')


import random


jokes = [
    "Why do programmers prefer dark mode? Because the light attracts bugs!",
    "Why do Java developers wear glasses? Because they don't see sharp.",
    "How many programmers does it take to change a light bulb? None, that's a hardware problem!",
    "Why do Python developers wear glasses? Because they can't C.",
    "I would tell you a UDP joke, but you might not get it.",
    "Why did the programmer quit his job? Because he didn't get arrays!",
    "There are 10 kinds of people in the world: those who understand binary and those who don’t.",
    "A SQL query walks into a bar, walks up to two tables, and asks: 'Can I join you?'",
    "How do functions break up? They stop calling each other!",
    "What's a programmer's favorite place to hang out? The Foo Bar."
]


joke = random.choice(jokes)

print("Here's a programming joke for you:")
print(joke)


