import random #import the random built in function
jokes = [
    "Why did the programmer quit his job?, Because he didn't get arrays.",
    "Why do Python developers wear glasses?, Because they can't C.",
    "Why was the math book sad?, Because it had too many problems.",
    "Why did the computer go to the doctor?, Because it had a virus.",
    "Why did the scarecrow win an award?, Because he was outstanding in his field."
]  #list of jokes

random_joke = random.choice(jokes) #get random joke
print(random_joke) #print the random joke

