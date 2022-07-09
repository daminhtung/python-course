# a = append
# w = override all content of file by text

countries_file = open("files/countries.txt", "a")

countries_file.write("\nPoland")

countries_file.close()



html_page = open("files/index.html", "w")

html_page.write("<p>This is Index page</p>")

html_page.close()