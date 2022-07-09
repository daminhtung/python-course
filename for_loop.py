print("-----------String-----------")
for letter in "Hello my friends":
    print(letter)

print("-----------Array-----------")
friends = ["Micheal", "Tung", "Nguyen"]
for friend in friends:
    print(friend)

# Range range(0, 3)
print("-----------Range-----------")
for index in range(len(friends)):
    print(friends[index])

for index in range(3):
    if index == 0:
        print("First element")
    else:
        print("Not first element")