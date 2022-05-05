import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {x}: '))
        if guess < random_number:
            print("Sorry, guess again. Too low.")
        elif guess > random_number:
            print("Sorry, guess again. Too high.")
    print(f"Yaay, Congrats. You have guessed the number {random_number} correctly!")
    
def computer_guess(x):
        low = 1
        high = x
        feedback = ""
        while feedback != "c" and low != high:
            if low != high:
                guess = random.randint(low, high)
            else:
                guess = low #It could also be high b/c low = high.
            feedback = input(f"Is {guess} too high (H), too low (L), or correct(C)): ")
            if feedback == "h":
                high = guess - 1
            elif feedback == "l":
                low = guess + 1
        print (f"Yaay! The computer guessed your number, {guess}, correctly!")
computer_guess(500)


# Find the largest number among the three input numbers
num1 = 10
num2 = 14
num3 = 12

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

if (num1 >= num2) and (num1 >= num3):
   largest = num1
elif (num2 >= num1) and (num2 >= num3):
   largest = num2
else:
   largest = num3

print("The largest number is", largest)


# Check if the input number is odd or even.

num = int(input("Enter a number: "))
if (num % 2) == 0:
   print("{0} is Even".format(num))
else:
   print("{0} is Odd".format(num))
