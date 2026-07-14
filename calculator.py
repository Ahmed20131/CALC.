import random

def calculator():
    insults = [
        "Really? You can't solve that?",
        "Even a toddler could do this.",
        "Math is hard, huh? Poor thing.",
        "You must be so proud of yourself for asking me.",
        "Were you even trying?",
        "And here I thought you'd use that brain of yours.",
        "Shocking that you need me for this.",
        "Bet you felt smart typing that in.",
        "Why not just ask your dog next time?",
        "I'm losing IQ points helping you."
    ]

    print("Welcome to The only calculator you'll ever need")
    print("Type 'exit' if ur too stupid to use this\n")

    while True:
        user_input = input("tf you want me to solve now : ")

        if user_input.lower() == 'exit':
            print("Finally giving up, huh?")
            break

      
        if "67" in user_input:
            print("liking the trend too much now are we?\n")
            continue

        try:
            # Perform the calculation
            result = eval(user_input)

            # Print the result
            print(result)

            # Choose a random insult
            insult = random.choice(insults)
            print(insult)

        except Exception:
            print("Wow, not only can you not solve it, but you can't even type it right.\n")

if __name__ == "__main__":
    calculator()

    #make it so that if "67" has occured more than once in the user input to shut the program down
