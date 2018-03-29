

x = 25
def my_func():
    x=50
    return x

print(x)
print(my_func())


###############################
### Quick examples of LEGB ####
###############################

#LOCAL
f = lambda x:x**2

#Enclosing func locals
name = 'This is a global name'

def greet():
    # Enclosing function
    name = 'Sammy'

    def hello():
        print('Hello '+name)

    hello()

greet()


print name


# Built-in
# These are the built-in function names in Python (don't overwrite these!)
# You will know if you've typed one based on its color!

len



# Example:

x = 50

def func(x):
    print('x is', x)
    x = 2
    print('Changed local x to', x)

func(x)
print('x is still', x)


# The first time that we print the value of the name x with the first line in
# the function’s body, Python uses the value of the parameter declared in the
# main block, above the function definition.
#
# Next, we assign the value 2 to x. The name x is local to our function. So,
# when we change the value of x in the function, the x defined in the main block
# remains unaffected.
#
# With the last print statement, we display the value of x as defined in the main
# block, thereby confirming that it is actually unaffected by the local
# assignment within the previously called function.

################################
# The Global Statement
################################

# If you want to assign a value to a name defined at the top level of the program
# (i.e. not inside any kind of scope such as functions or classes), then you have
# to tell Python that the name is not local, but it is global. We do this using
# the global statement. It is impossible to assign a value to a variable defined
# outside a function without the global statement.
#
# You can use the values of such variables defined outside the function
# (assuming there is no variable with the same name within the function).
# However, this is not encouraged and should be avoided since it becomes unclear
# to the reader of the program as to where that variable’s definition is. Using
# the global statement makes it amply clear that the variable is defined
# in an outermost block.
#
# Example:

x = 50

def func():
    global x
    print('This function is now using the global x!')
    print('Because of global x is: ', x)
    x = 2
    print('Ran func(), changed global x to', x)

print('Before calling func(), x is: ', x)
func()
print('Value of x (outside of func()) is: ', x)


# The global statement is used to declare that x is a global variable - hence,
# when we assign a value to x inside the function, that change is reflected
# when we use the value of x in the main block.
#
# You can specify more than one global variable using the same global statement
# e.g. global x, y, z.

###############################
# Conclusion
###############################

# You should now have a good understanding of Scope (you may have already
# intuitively felt right about Scope which is great!) One last mention is that
# you can use the globals() and locals() functions to check what are your current
# local and global variables.
#
# Another thing to keep in mind is that everything in Python is an object! I can
# assign variables to functions just like I can with numbers! We will go over
# this again in the decorator section of the course!
