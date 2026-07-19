# string indexing (grabbing specific letters from left to right)
"g a l a x y"
"0 1 2 3 4 5"
space_term = "galaxy"
print(space_term[0])  # grabs the first letter 'g'
print(space_term[3])  # grabs the fourth letter 'a'
print(space_term[5])  # grabs the last letter 'y'

# negative indexing (counting from right to left)
# -1 is always the very last character
print(space_term[-1])  # 'y'
print(space_term[-2])  # 'x'
print(space_term[-6])  # 'g' (first letter again)

# slicing: cutting out chunks of text [start:stop:step]
motto = "stay frosty"

print(motto[0:4])    # gets 'stay' (stops right before index 4)
print(motto[5:11])   # gets 'frosty'
print(motto[:4])     # shortcut for starting at the beginning
print(motto[5:])     # shortcut for going all the way to the end

print(motto[:])      # just makes a full copy of the string

# messing with the 'step' part of slicing
print(motto[::2])    # skips every other letter (outputs 'sa rsy')
print(motto[::-1])   # cool trick: reverses the whole string ('ytsorf yats')

# immutability (strings are locked, you can't edit parts of them)
status = "ready"

# status[0] = "R"    # uncommenting this will throw a TypeError! 

# you can't change the original, so you have to build a new string instead
status = "R" + status[1:]  # glues "R" with "eady"
print(status)              # prints 'Ready'

# why are they locked like this?
# - safer code (functions can't accidentally mess up your text)
# - saves memory under the hood
# - we need them to be immutable to use them as dictionary keys later
