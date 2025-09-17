# The basics
print("Hello world!")

""" VARIABLES """

# Variables can really be anything
var = "something" # words
var = 388 # numbers

# They can even be functions
def func():
    print("This is a function")

var = func() # ?

var = lambda : func()
var # !

# They can also be custom types (classes)
class Something:

    def __init__(self):
        print("I made a class.")

    def huh(self):
        print("How?")
    
var = Something()
var.huh()

""" FUNCTIONS """

# Regular function, contents indented
def func(param):

    print(param)

# Parameters not bound to any type
func("Not bound to anything")
func(7)
func(func) 

# Pack params (more on this later)
def func2(*param):

    print(param)

func2("Multiple", "params")

""" CONDITIONALS """

# Assume both variables are true to begin with
raining = True
umbrella = True

print(f"Don't go outside: {raining and not umbrella}")
print(f"Go outside: {not raining or umbrella}")

print(f"Optimal: {raining == umbrella}")

# if-else block
if raining:
    print("Don't go out")
else:
    print("You can go out")

# if-else if-else block
if raining and umbrella:
    print("Go")
elif raining:
    print("Don't go")
else:
    print("Go")

go_out = raining == umbrella
print(go_out)