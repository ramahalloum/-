number = int(input("Enter a non-negative number to calculate the factorial: "))

fact = 1

if number < 0:
    print("Sorry, factorial does not exist for negative numbers.")
else:
    for i in range(1, number + 1):
        fact *= i

print("The factorial of", number, "is", fact)
