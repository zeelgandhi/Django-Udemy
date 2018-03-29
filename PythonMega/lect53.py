# myfile = open("employees.txt", "w")
# myfile.write("Mike \nJoe\nJack")
# myfile.close()
#
# myfile = open("employees.txt", "a")
# myfile.write("\nZeel")
# myfile.close()

myfile = open("employees.txt", "a+")
myfile.read()

myfile.write("\nJohn")
myfile.close()
