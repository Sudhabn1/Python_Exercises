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
