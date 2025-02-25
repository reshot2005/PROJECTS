print('Hello! My name is Chachan.')
print('I was created in 2025.')
print('Please, remind me your name.')

name = input()

print('What a great name you have, ' + name + '!')
print('Let me guess your age.')
print('Enter remainders of dividing your age by 3, 5 and 7.')

# reading all remainders
rem3 = int(input())
rem5 = int(input())
rem7 = int(input())

# calculating age
your_age = (rem3 * 70 + rem5 * 21 + rem7 * 15) % 105

print(f"Your age is {your_age}; that's a good time to start programming!")
print('Now I will prove to you that I can count to any number you want.')

# read a number and count to it here
num = int(input())
for i in range(num + 1):  # Counting from 0 to the given number
    print(f"{i} !")

print('Completed, have a nice day!')
print("Let's test your programming knowledge.")
print("Why do we use methods?")
print("1. To repeat a statement multiple times.")
print("2. To decompose a program into several small subroutines.")
print("3. To determine the execution time of a program.")
print("4. To interrupt the execution of a program.")

# Loop until the correct answer (2) is given
while True:
    answer = int(input())
    if answer == 2:
        print("Congratulations, have a nice day!")
        break
    else:
        print("Please, try again.")
