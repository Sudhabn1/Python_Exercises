"""
    Decision making is anticipation of conditions occurring while execution of the program and specifying actions
    taken according to the conditions. Decision structures evaluate multiple expressions which produce TRUE or FALSE as
    an outcome. You need to determine which action to take and which statements to execute if outcome is TRUE or FALSE!

    Types of Decision Making logic -
        Python IF ELSE Statement
        Python IF...ELIF...ELSE Statements
        Python nested IF statements
"""

# If Else Statements

sample_variable = 100
if sample_variable >= 88:
    print()
    print("Yes, Variable' value is more than 88 & it's declared value =", sample_variable)
else:
    print("Variable's Value is more than our Conditional value")

print("--------------------------")


sample_string = "Hey, you are executing Python scripts!"
another_sample_string = "python"        # p is lower case (Comparison is case-sensitive)
yet_another_sample_string = "Python"    # P is upper case (Comparison works!)
if another_sample_string in sample_string:
    print("Yes, word 'Python' characters are present in SAMPLE_STRING's value")
else:
    print("Hmm! Might be case-sensitive.")

if yet_another_sample_string in sample_string:
    print("Yes, word 'Python' characters are present in SAMPLE_STRING's value")
else:
    print("Hmm! Might be case-sensitive.")

print("--------------------------")


some_float_number = 4778299.882
divide_by_number = 1883.22
if some_float_number // divide_by_number >= 2500:       # Performs floor division
    print("Yes, it's correct! Indeed actual floor division output =", some_float_number // divide_by_number)
else:
    print("No! Output of floor division is less than Comparison/Conditional value")

print("--------------------------")


# If Elif Else Statements

var = 100
if var == 200:
    print("1 - Got a true expression value")
    print(var)
elif var == 150:
    print("2 - Got a true expression value")
    print(var)
elif var == 100:
    print("3 - Got a true expression value")
    print(var)
else:
    print("4 - Got a false expression value")
    print(var)
print("Good bye!")

print("--------------------------")


sample_var_one = "Johnson"
sample_var_two = "Cookson"
sample_var_three = "Thomson"
sample_var_four = "Pearson"
validation_var_value = "Jackson"

if validation_var_value == sample_var_one:
    print("Name is matching with 'sample_var_one' variable's string value")
elif validation_var_value == sample_var_two:
    print("Name is matching with 'sample_var_two' variable's string value")
elif validation_var_value == sample_var_three:
    print("Name is matching with 'sample_var_three' variable's string value")
elif validation_var_value == sample_var_four:
    print("Name is matching with 'sample_var_four' variable's string value")
else:
    print("It's not matching with any of the above declared names! Actual name declared =", validation_var_value)

print("--------------------------")


# Nested If Statements

num = float(85)
if num >= 0:
    if num == 0:
        print("Zero")
    else:
        print("Positive number")
else:
    print("Negative number")

print("--------------------------")


year = 2019
if (year % 4) == 0:
    if (year % 100) == 0:
        if (year % 400) == 0:
            print("{0} is a leap year".format(year))
        else:
            print("{0} is not a leap year".format(year))
    else:
        print("{0} is a leap year".format(year))
else:
    print("Yes! {0} is not a leap year".format(year))

print("--------------------------")
