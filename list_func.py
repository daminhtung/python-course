lucky_numbers = [4, 8, 1, 15, 23, 25, 50]
friends = ["Kevin", "Karen", "Jim", "Kevin1", "Karen1", "Jim1", "Micheal"]

# //Append array
friends.extend(lucky_numbers)
print(friends)

# Append 1
friends.append('Micheal')
print(friends)

friends.insert(1, "This is inserted")
print(friends)

friends.remove("Kevin1")
print(friends)

print(friends.index('Micheal'))

print(friends.count("Micheal")) # => 2

lucky_numbers.sort()
print(lucky_numbers)

lucky_numbers.reverse()
print(lucky_numbers)

friends2 = friends.copy()
print(friends2)

friends.clear()
print(friends)



