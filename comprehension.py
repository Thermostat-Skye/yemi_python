numbers = [1, 2, 4, 6, 7, 8, 9]
new_numbers = []

for n in numbers:
    new_numbers.append(n)
print(new_numbers)

even_numbers = []
for e in range(1, 43):
    if e % 2 == 0:
        even_numbers.append(e)
print(even_numbers)

nums = [3, 4,6, 7, 8, 9, 12, 21]
print_numbers = [n for n in nums]
print(print_numbers)

list_even_numbers = [e for e in range(30) if e % 2 == 0]
print(list_even_numbers)