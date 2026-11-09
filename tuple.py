# Empty tuple
empty = ()

# Tuple with items
point = (3, 5)
colors = ("red", "green", "blue")

# Single item tuple needs comma!
single = (42,)  # Note the comma
not_tuple = (42)  # This is just 42 in parentheses

# Without parentheses (implicit)
coordinates = 10, 20

print(empty)        # ()
print(point)        # (3, 5)
print(colors)       # ('red', 'green', 'blue')
print(single)       # (42,)
print(not_tuple)    # 42
print(coordinates)  # (10, 20)
print(type(coordinates))     # <class 'tuple'>


point = (3, 5)
colors = ("red", "green", "blue")

# Get items
print(point[0])      # 3
print(colors[-1])    # "blue"

# Slicing works too
print(colors[0:2])   # ("red", "green")


# Unpack values
point = (3, 5)
x, y = point  # x = 3, y = 5

print(x)  # 3
print(y)  # 5

# Multiple assignment
a, b, c = 1, 2, 3  # Same as (1, 2, 3)
print(a)  # 1   
print(b)  # 2
print(c)  # 3

# Swap variables elegantly
x, y = y, x  # Swaps values!
print(x)  # 5
print(y)  # 3


# Wrong - tuples are immutable
point = (3, 5)
point[0] = 4  # TypeError!

# Right - create a new tuple
point = (4, point[1])
print(point)  # (4, 5)  
# Or convert to list, modify, convert back
temp = list(point)
temp[0] = 4
point = tuple(temp)

print(point)  # (4, 5)
print(type(point))  # <class 'tuple'>
print(type(temp))   # <class 'list'>