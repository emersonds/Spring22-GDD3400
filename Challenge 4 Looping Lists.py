# Question 1:

numbers = [ "one", 2, 3.5, "four", 5 ]  # Initialize list
print(numbers)                          # Print "numbers"

# Print each item in numbers individually on a new line
for number in numbers:
    print(number)

# Print each item in numbers backwards using slice notation
for number in numbers[::-1]:
    print(number)

# Question 2:

cubes = [ number**3 for number in range(1, 11) ]    # List Comphrension. Fills a list of ten cubes starting at 1 to 10. 1**3, 2**3, etc.
print(cubes)                                        # Print "cubes"
numbers = [ number for number in range(1, 76) ]     # List Comprehension. List contains values from 1 to 75.
print (sum(numbers))                                # Print sum of "numbers" from 1 to 75