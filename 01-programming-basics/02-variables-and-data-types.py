# trying out different naming styles
login_attempts = 3   # snake case (standard for python)
loginAttempts = 3    # camel case
LoginAttempts = 3    # pascal case (mostly for classes)

# testing rules for variable names
_secret_key = "abc123"
valid_name_99 = True

# 1st_place = "gold"  # this throws an error, can't start with a number
# user score = 50     # adding spaces in between , shows ERROR 
# user-score = 50     # adding hyphens in bitween , shows ERROR

# python cares about capital letters
city = "London"
City = "Paris"
print(city)  # prints London
print(City)  # prints Paris

# can't use built-in words like def, class, if, etc.
# class = "Math 101"  # syntax error!

# messing with numbers
score = 100
penalty = -10
win_rate = 75.5
weird_math = 5 + 2j

# checking what type of data these are
print(type(score))     # <class 'int'>
print(type(win_rate))  # <class 'float'>

# strings and quotes
first_word = 'Hello'
second_word = "Universe"

# joining strings together
phrase = first_word + " " + second_word
phrase = f"{first_word} {second_word}" # alternative way to add 2 strings
print(phrase) # Output: Hello Universe 

# string tricks
msg = "coding is hard"
print(msg.upper()) #output: COADING IS HARD
print(msg.lower()) #output: coading is hard
print(msg.replace("hard", "fun")) # output: coading is fun
print(len(msg))  # counts the characters, including spaces

# true or false stuff (booleans)
has_key = True
door_locked = False

print(has_key and door_locked)  # false, because both aren't true
print(has_key or door_locked)   # true, because at least one is true
print(not has_key)              # false, it flips the true to false

# changing data types (casting)
string_num = "404"
real_int = int(string_num)      # string to int: 404
real_float = float(string_num)  # string to float: 404.0
back_to_str = str(99)           # int back to string: "99"

# string Take whatever is inside these parentheses and turn it into text !
