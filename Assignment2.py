# Assignment_2

# Task_1:- Check if a number is even or odd
number = int(input("Enter the number: "))
if number % 2 == 0:
    print(number, "is an even number.")
else:
    print(number, "is an odd number.")


# Task_2:- Sum of integer from 1 to 50 using a loop
sum = 0
for i in range(1, 51):
    sum = sum + i
print("The sum of numbers from 1 to 50 is:", sum)
