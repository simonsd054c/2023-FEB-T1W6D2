# List - Array - collection of data - mutable(change) - indexed

# numbers = [ 13, 2, 5, 98, 56 ]
#     #       0   1  2  3   4

# print(numbers)
# print(numbers[2])
# numbers[2] = 15
# print(numbers)
# numbers.append(42)
# print(numbers)
# numbers.insert(3, 28)
# print(numbers)
# numbers.pop()
# print(numbers)
# numbers.remove(98)
# print(numbers)
# # sort(), reverse(), count(), index()
# print(len(numbers))


# Tuple - similar to list - indexed - immutable (not change)
# names = ( "John", "Jane", "Mike", "John" )
# print(names)
# print(type(names))
# print(names[1])
# print(names.count("John"))
# print(len(names))
# # append, remove, pop, insert - cannot do any of these
# # cannot do - names[1] = "Smith"

# months = ("Jan", "Feb")
# coordinates = (-67.45, 72.57)


# Primitive - copied by value
# a = 2
# b = a
# print(b)
# a = 3
# print(b)

# Complex - copied by reference (address)
a = [ 1, 2, 3, 4 ]
b = a.copy()
print(b)
a.append(5)
print(b)
# a = 5
# print(b)