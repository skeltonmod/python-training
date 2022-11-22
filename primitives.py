####################################################
# 1. Primitive Datatypes and Operators
####################################################
# You have numbers
print(3)  # => 3

# Math is what you would expect
print(1 + 1)  # => 2
print(8 - 1)  # => 7
print(10 * 2)  # => 20
print(35 / 5)  # => 7.0

# The result of division is always a float
print(10.0 / 3)  # => 3.3333333333333335

# Modulo operation
print(7 % 3)  # => 1
# i % j have the same sign as j, unlike C
print(-7 % 3)  # => 2

# Exponentiation (x**y, x to the yth power)
print(2**3)  # => 8

# Enforce precedence with parentheses
print(1 + 3 * 2)  # => 7
print((1 + 3) * 2)  # => 8

# Boolean values are primitives (Note: the capitalization)
print(True)  # => True
print(False)  # => False

# negate with not
print(not True)  # => False
print(not False)  # => True

# Boolean Operators
# Note "and" and "or" are case-sensitive
print(True and False)  # => False
print(False or True)  # => True

# True and False are actually 1 and 0 but with different keywords
print(True + True)  # => 2
print(True * 8)  # => 8
print(False - 5)  # => -5

# Comparison operators look at the numerical value of True and False
print(0 == False)  # => True
print(1 == True)  # => True
print(2 == True)  # => False
print(-5 != False)  # => True

# None, 0, and empty strings/lists/dicts/tuples/sets all evaluate to False.
# All other values are True
print(bool(0))  # => False
print(bool(""))  # => False
print(bool([]))  # => False
print(bool({}))  # => False
print(bool(()))  # => False
print(bool(set()))  # => False
print(bool(4))  # => True
print(bool(-6))  # => True

# Using boolean logical operators on ints casts them to booleans for evaluation,
# but their non-cast value is returned. Don't mix up with bool(ints) and bitwise
# and/or (&,|)
print(bool(0))  # => False
print(bool(2))  # => True
print(0 and 2)  # => 0
print(bool(-5))  # => True
print(bool(2))  # => True
print(-5 or 0)  # => -5

# Equality is ==
print(1 == 1)  # => True
print(2 == 1)  # => False

# Inequality is !=
print(1 != 1)  # => False
print(2 != 1)  # => True

# More comparisons
print(1 < 10)  # => True
print(1 > 10)  # => False
print(2 <= 2)  # => True
print(2 >= 2)  # => True

# Seeing whether a value is in a range
print(1 < 2 and 2 < 3)  # => True
print(2 < 3 and 3 < 2)  # => False
# Chaining makes this look nicer
print(1 < 2 < 3)  # => True
print(2 < 3 < 2)  # => False

# (is vs. ==) is checks if two variables refer to the same object, but == checks
# if the objects pointed to have the same values.
a = [1, 2, 3, 4]  # Point a at a new list, [1, 2, 3, 4]
b = a  # Point b at what a is pointing to
print(b is a)  # => True, a and b refer to the same object
print(b == a)  # => True, a's and b's objects are equal
b = [1, 2, 3, 4, 5]  # Point b at a new list, [1, 2, 3, 4, 5]
print(b)
print(b is a)  # => False, a and b do not refer to the same object
print(b == a)  # => True, a's and b's objects are equal

# Strings are created with " or '
print("This is a string.")
print("This is also a string.")

# Strings can be added too
print("Hello " + "world!")  # => "Hello world!"
# String literals (but not variables) can be concatenated without using '+'
print("Hello " "world!")  # => "Hello world!"

# A string can be treated like a list of characters
print("Hello world!"[0])  # => 'H'

# You can find the length of a string
print(len("This is a string"))  # => 16

# Since Python 3.6, you can use f-strings or formatted string literals.
name = "Reiko"
print(f"She said her name is {name}.")  # => "She said her name is Reiko"
# Any valid Python expression inside these braces is returned to the string.
print(f"{name} is {len(name)} characters long.")  # => "Reiko is 5 characters long."

# None is an object
print(None)  # => None

# Don't use the equality "==" symbol to compare objects to None
# Use "is" instead. This checks for equality of object identity.
# "etc" is None  # => False
print(None is None)  # => True
