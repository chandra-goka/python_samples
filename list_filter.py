numbers = [1, 2, 3, 4, 5, 6, 7]

even_numbers = filter(lambda item: item % 2 == 0, numbers)
print(even_numbers)

even_numbers = list(filter(lambda item: item % 2 == 0, numbers))

print(f"Even numbers: {even_numbers}")


even_numbers = [number for number in numbers if number % 2 == 0]
print(f"even numbers : {even_numbers}")