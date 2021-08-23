# Max Zinski
# Problem 1

# What is the time complexity of the following code snippets?

# n is the number of items in the numbers object

# Snippet 1: O(n)
map(lambda x: x ** 2, numbers)

# Snippet 2: O(n)
filter(lambda x: x % 2, numbers)

# Snippet 3: O(n)
reduce(lambda x,y: x + y, numbers)