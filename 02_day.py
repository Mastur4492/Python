# 📌 Type conversion functions in Python:
# 1. int() - Convert to integer
# 2. float() - Convert to float
# 3. str() - Convert to string
# 4. ord() - Get ASCII value of a character
# 5. chr() - Get character from ASCII value
# 6. bin() - Convert to binary
# 7. hex() - Convert to hexadecimal
# 8. oct() - Convert to octal
# 9. complex() - Create complex numbers

x = ord('a')  # ASCII value of 'a'
print(x)  # Output: 97

x = chr(97)  # Character from ASCII value
print(x)  # Output: 'a'

y = bin(10)  # Convert to binary
print(y)  # Output: '0b1010'

z = hex(55)  # Convert to hexadecimal
print(z)  # Output: '0x37'

"""
==========================================
  📌 Data Types in Python
==========================================
"""

# Python supports different types of data:

# 1. Primitive Data Types:
#    - int, float, string, complex, bool, bytes

x = complex(2, 4)  # Complex number
print(x)  # Output: (2+4j)

a = True  # Boolean type
print(a, type(a))  # Output: True <class 'bool'>

name = "Pawan"  # String
print(name, type(name))  # Output: Pawan <class 'str'>

y = b"Pawan"  # Bytes data type
print(y)  # Output: b'Pawan'

"""
==========================================
  ❌ Immutable and Mutable Data Types
==========================================
"""

# 📌 Strings in Python are immutable (cannot be modified).

name = "abc"
# name[0] = 'x'  # ❌ TypeError: 'str' object does not support item assignment

print(name)  # Output: 'abc'

"""
==========================================
  📚 Collection Data Types
==========================================
"""

# 📌 Python supports four main collection data types:
# 1. List - Ordered, mutable
# 2. Set - Unordered, unique elements
# 3. Tuple - Ordered, immutable
# 4. Frozenset - Immutable version of set

# ✅ List - Mutable (Can be modified)
l = ["Pawan", 1, 3, 56, 78, 90]
print(l)

l[3] = 100  # Modifying an element
print(l)  # Output: ['Pawan', 1, 3, 100, 78, 90]

# ✅ Set - Unordered, unique elements, removes duplicates
s = {12, 34, 678, 90, "pawan", 12}  # Duplicate 12 will be removed
print(s)  # Output: {34, 12, 90, 'pawan', 678} (order may vary)

"""
==========================================
  🎯 Summary:
==========================================

✅ Python is an easy-to-learn, dynamically typed, and case-sensitive language.
✅ print() function is used to display output with optional separators and end characters.
✅ Variables do not need explicit type declaration.
✅ Constants can be simulated using a custom class.
✅ Input is taken as a string and must be type-casted when needed.
✅ Various type conversion functions help in data manipulation.
✅ Strings are immutable, but lists are mutable.
✅ Sets automatically remove duplicates.

"""

# End of lecture 🚀


# A = 10

# print(A)

# print(type(A))

# A = 12.7

# print(A)


# In Python, you can't create truly constant variables, but you can enforce immutability using custom classes. Below are different approaches to prevent reassignment.


# class Constant:
#     def __setattr__(self, name, value):
#         if hasattr(self, name):  # If the attribute is already set, prevent reassignment
#             raise TypeError(f"Cannot modify constant '{name}'")
#         super().__setattr__(name, value)

# const = Constant()
# const.A = 10   # ✅ Allowed: First assignment
# print(const.A) # 10

# const.A = 12.7 # ❌ TypeError: Cannot modify constant 'A'

# python case sensitive 


# B = 10

# b = 20

# print(b)
# print(B)



# How to take input from user?

# x = 10
# print(x)


# x = input()

# print(x)
# print("Enter Number : ")
# x = input()

# print(x)

# x = input("Enter Number : ")

# print("Value : ",x)

# Type Casting Constructor


# x = int(input("Enter Number : "))

# print("Value : ",x)
# print(type(x))

"""
1. int()
2. float()
3. str()
4. ord()
5. chr()
6. bin()
7. hex()
8. oct()
9. complex() """

# x = 12

# print(str(x))
# print(type(str(x)) )

# x = ord('a')

# print(x)


# x = chr(97)

# print(x)


# y = bin(10)
# print(y)

# y = bin(5)
# print(y)


# z = hex(55)

# print(z)



# DataType

# 1. primitive datatype -> integer, float, string, complex, bool, bytes

# x = complex(2,4)

# print(x)

# a = True
# print(a)
# print(type(a))

# name = "Pawan"

# print(name)
# print(type(name))


# y = b"Pawan"

# print(y)  # Output: b'Pawan'

# # Attempt to modify an element of bytes
# y[0] = b'H'  # ❌ TypeError: 'bytes' object does not support item assignment

# string

# name = "abc"

# name[0] = 'x'  # ❌ TypeError: 'str' object does not support item assignment

# print(name)


# 2. collection datatype

# 1.list
# 2. set
# 3. tuple
# 4. frozenset



#list -> mutable

# l = ["Pawan",1,3,56,78,90]
# print(l)
# l[3] = 100

# print(l)

#set -> unique , remove dublicate

# s = {12,34,678,90,"pawan",12}

# print(s) 