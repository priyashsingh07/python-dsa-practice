# standard printing
print("System booting up...")
print(404)
print(9.81)

# printing multiple things at once (automatically adds spaces)
player = "Zane"
hp = 150
print("Character:", player, "Health:", hp)

# gluing strings together (concatenation)
first_part = "Cyber"
second_part = "Punk"
game_title = first_part + second_part
print(game_title)

# print("HP left: " + 50)  # this breaks! you can't add an int to a string
print("HP left: " + str(50))  # much better, cast it to a string first

# f-strings (honestly the best way to do this in python)
hero = "Batman"
gadgets = 5
city = "Gotham"

# just put an 'f' in front of the quotes and use curly braces for variables
status = f"Alert: {hero} has {gadgets} gadgets left in {city}."
print(status)

# you can even do math right inside the curly braces
print(f"After using one, he has {gadgets - 1} gadgets remaining.")

# f-strings are also great for formatting numbers
tax_rate = 0.082594
print(f"Tax rate: {tax_rate:.2f}")  # rounds it neatly to 2 decimal places

# messing with escape characters
print("Line one\nLine two")    # \n creates a new line
print("Column A\tColumn B")    # \t pushes text over like a Tab key
print("whoops\b")              # \b is a backspace (deletes the 's')
print("folder\\subfolder")     # \\ prints a single backslash

# dealing with quotes inside quotes
print('It\'s raining outside')   # escaping the single quote so it doesn't break the string
print("She yelled \"Stop!\"")    # escaping double quotes

# raw strings (tells python to literally ignore escape characters)
# standard way (annoying)
file_path_1 = "C:\\Users\\admin\\Downloads"
print(file_path_1)

# raw string way (just put an 'r' in front, much cleaner for file paths)
file_path_2 = r"C:\Users\admin\Downloads"
print(file_path_2)

# raw strings are super common when writing regular expressions (regex)
import re
regex_pattern = r"\d{4}-\d{2}"  # doesn't treat \d as an escape character