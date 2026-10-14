# Program 147: Sum of Even and Odd Numbers

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_sum = 0
odd_sum = 0

for number in numbers:
    if number % 2 == 0:
        even_sum += number
    else:
        odd_sum += number

print("Sum of even numbers:", even_sum)
print("Sum of odd numbers:", odd_sum)