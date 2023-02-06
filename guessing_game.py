import random

answer = random.randint(1, 100)
guess_num = 1

print(guess_num)

def guess_the_number():

    global guess_num
    guess = int(input("Guess a number between 1 and 100: "))


    if guess == answer:
        print("Got it! The right number was %g and you got the answer in %g attempt(s)" % (answer, guess_num))
    elif guess < answer:
        print("Guess higher!")
        guess_num += 1
        guess_the_number()
    elif guess > answer:
        print("Guess lower!")
        guess_num += 1
        guess_the_number()


guess_the_number()