x = "awesome"


def myfunc():
    print("Python is " + x)


myfunc()




def my_function():
    x = "fantastic"
    print("python is " + x)


my_function()

print("Python is " + x)


def global_myfunc():
    global y
    y = "fantastic"


global_myfunc()
print("python is " + y)


def my_f():
    global x
    x = "fantastic"

my_f()
print("______________")
print("Python is " + x)