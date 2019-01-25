"""
    Strings are amongst the most popular types in Python.
    We can create them simply by enclosing characters in quotes.
    Python treats single quotes the same as double quotes.
"""

sample_string = "Bangalore is IT capital of India and it's a nice city! "
another_sample_string = "Bangalore is part of Karnataka state."

# Common String Operations

print("Print String Variable Value =", sample_string)
print("Length =", len(sample_string))
print("Display Characters @ Index 13 - 16 =", sample_string[13:16])
print("Adding 2 Strings =", sample_string + another_sample_string)

# String Search Pattern

new_city = "Mysore"
if new_city in sample_string:
    print("Mysore text is present in a sample string declared in this script")
else:
    print("No, word 'Mysore' is not present in the sample string declared in this script")
print("Good Bye!")
print("--------------------------")


# String Operations (Count Method)

one_more_string = "Bangalore is a having a nice climate, but traffic within the city is becoming a challenge."
print("Count of letter 'i' present in String declared within this script =", one_more_string.count('i'))
print("Count of letter 'e' present in String declared within this script =", one_more_string.count('e'))

# String Operations (Formatting)

new_sample_string = "MS Dhoni"
another_star_cricketer = "virat kohli"

print("Upper Case Conversion =", new_sample_string.upper())
print("Lower Case Conversion =", new_sample_string.lower())
print("Capitalize Formatting =", another_star_cricketer.capitalize())
print("String Length's =", len(new_sample_string))
print("String Size Calculation =", new_sample_string.__sizeof__())
