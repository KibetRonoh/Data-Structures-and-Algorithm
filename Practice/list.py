##########
list = [1, 2, 3, 4, 4]
list.append('kibet')
list.insert(3, 'Ronoh')
list.extend([2, 'hillary', '$ 2500'])

print(list)

# adding multiple elements using append method
lost = [8, 9, 78, 6, 45]

for i in range(1, 9):
    lost.append(i)
print(lost)

lost.pop()
print(lost)

lost.pop(3)
print(lost)


