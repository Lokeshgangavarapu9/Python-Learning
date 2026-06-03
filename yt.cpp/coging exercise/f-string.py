# F-String Example
name = "Lokesh"
age = 25
height=6
# Using f-string to format the string
print(f"My name is {name} and I am {age} years old. My height is {height} inches.")
print("my name is" + name + "i am " + str(age) + "years old" +"heighis is" + str(height) +"inches")

# F-String with expressions
a = 5
b = 10
print(f"The sum of {a} and {b} is {a + b}.")

# F-String with formatting
pi = 3.14159
print(f"The value of pi is approximately {pi:.2f}.")

# F-String with variables and expressions
x = 10
y = 20
print(f"The product of {x} and {y} is {x * y}.")

# F-String with a function call
def greet(name):
    return f"Hello, {name}!"
print(f"{greet(name)} Welcome to Python programming.")

# F-String with a list
fruits = ["apple", "banana", "cherry"]
print(f"My favorite fruits are: {', '.join(fruits)}.")

# F-String with a dictionary
person = {"name": "Alice", "age": 30}
print(f"{person['name']} is {person['age']} years old.")

# F-String with a tuple
coordinates = (10, 20)
print(f"The coordinates are: {coordinates[0]}, {coordinates[1]}.")

# F-String with a set
unique_numbers = {1, 2, 3, 4, 5}
print(f"The unique numbers are: {', '.join(str(num) for num in unique_numbers)}.")

# F-String with a boolean
is_raining = True
print(f"Is it raining? {is_raining}.")

# F-String with a None value
favorite_color = None
print(f"My favorite color is: {favorite_color}.")

# F-String with a multi-line string
multiline_string = f"""This is a multi-line string.
It can span multiple lines without needing escape characters."""
print(multiline_string)
