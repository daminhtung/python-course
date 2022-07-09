countries_file = open("files/countries.txt", "r")

# print(countries_file.readline())
# print(countries_file.readline())
# print(countries_file.readline())

# all line
# print(countries_file.readlines()[1])

for country in countries_file.readlines():
    print(country)

countries_file.close()