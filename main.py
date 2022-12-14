# Review:
# Create a function called greet().
# Write 3 print statements inside the function.
# Call the greet() function and run your code.

# def greet():
#   print("line 1")
#   print("line 2")
#   print("line 3")

# greet()
#Function with input
# def greet_with_name(name):
#   print(f"Hello {name}")
#   print(f"How do you do {name}?")

# greet_with_name("Van")


# Function with multiple inputs
def greet_with(name, location):
    print(f"Hello there, I'm {name}")
    print(f"I'm from {location}")


greet_with("Van", "Ottawa")


# Keyword arguments
def my_function(a=1, b=2, c=3):
    print(a)
    print(b)
    print(c)
def greet_with(name="Van", location="Ottawa"):
    print(f"Hello there, I'm {name}")
    print(f"I'm from {location}")


greet_with()