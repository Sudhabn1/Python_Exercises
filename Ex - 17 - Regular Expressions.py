"""
    A regular expression is a special sequence of characters that helps you match or find other strings
    or sets of strings, using a specialized syntax held in a pattern. Regular expressions are widely used in UNIX world.

    The module re provides full support for Perl-like regular expressions in Python.
    The re module raises the exception re.error if an error occurs while compiling or using a regular expression.
"""

# Syntax
# re.match(pattern, string, flags=0)

import re

# 1st Example - Generic Code

sentence = "Bengaluru is IT Capital of India and it's also Capital city for Karnataka state!"
matchObj = re.match( r'(.*) also (.*?) .*', sentence, re.M | re.I)
if matchObj:
    print("matchObj.group() : ", matchObj.group())
    print("matchObj.group(1) : ", matchObj.group(1))
    print("matchObj.group(2) : ", matchObj.group(2))
else:
    print("Nothing found!!")

print("--------------------------")

# 2nd Example Match vs Search

line = "Cats are smarter than dogs"

matchObj = re.match(r'dogs', line, re.M | re.I)
if matchObj:
    print("match --> matchObj.group() : ", matchObj.group())
else:
    print("No match!!")

searchObj = re.search(r'dogs', line, re.M | re.I)
if searchObj:
    print("search --> searchObj.group() : ", searchObj.group())
else:
    print("Nothing found!!")

print("--------------------------")

# 3rd Example Search & Replace
# Syntax - re.sub(pattern, repl, string, max=0)

phone = "2004-959-559 # This is Phone Number"

# Delete Python-style comments
num = re.sub(r'#.*$', "", phone)
print("Phone Num : ", num)

# Remove anything other than digits
num = re.sub(r'\D', "", phone)
print("Phone Num : ", num)

print("--------------------------")


# Regular Expression Modifiers: Option Flags
# re.I
#   Performs case-insensitive matching.

# re.L
#   Interprets words according to the current locale.
#   This interpretation affects the alphabetic group (\w and \W), as well as word boundary behavior(\b and \B).

# re.M
#   Makes $ match the end of a line (not just the end of the string)
#   and makes ^ match the start of any line (not just the start of the string).

# re.S
#   Makes a period (dot) match any character, including a newline.

# re.U
#   Interprets letters according to the Unicode character set.
#   This flag affects the behavior of \w, \W, \b, \B.

# re.X
#   Permits "cuter" regular expression syntax.
#   It ignores whitespace (except inside a set [] or when escaped by a backslash)
#   and treats unescaped # as a comment marker.
