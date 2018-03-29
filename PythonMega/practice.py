# Udemy course: Python mega course practice exercise solutions:

#1

# def c_to_f(C):
#
#     if C <= -273.15:
#         return "Please enter valid temp"
#     else:
#         F= C * 9/5 + 32
#         return F
#
# print(c_to_f(-270))


#2

# def string_length(mystring):
#     if type(mystring) == int:
#         return "Sorry, integers dont have length"
#     elif type(mystring)== float:
#         return "Sorry, floats dont have length"
#     else:
#         return len(mystring)
#
# print(string_length(10.0))


#3

# mylist = [1,2,3,4,5]
# for i in mylist:
#     print(i)


# mylist = [1,2,3,4,5]
# for i in mylist:
#     if i > 2:
#         print(i)

#4

# file = open("fruits.txt")
# content = file.read()
# file.close()
# content = content.split()
# for i in content:
#     print(len(i))

#5
temp = [10, -20, -289, 100]
def c_to_f(C):

    if C < -273.15:
        return "Please enter valid temp"
    else:
        F= C * 9/5 + 32
        return F
for t in temp:
    print(c_to_f(t))
