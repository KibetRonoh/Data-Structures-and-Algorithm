# List comprehension
odd_square = [x ** 2 for x in range(1, 11) if x % 2 == 1]
print(odd_square)


# Alternatively
# for understanding, above generation is same as,
odd_square1 = []
 
for x in range(1, 11):
    if x % 2 == 1:
        odd_square1.append(x**2)
 
print(odd_square1)
