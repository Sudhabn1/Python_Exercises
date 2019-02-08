"""
    A regular expression is a special sequence of characters that helps you match or find other strings
    or sets of strings, using a specialized syntax held in a pattern. Regular expressions are widely used in UNIX world.

    The module re provides full support for Perl-like regular expressions in Python.
    The re module raises the exception re.error if an error occurs while compiling or using a regular expression.
"""

# Syntax
# re.match(pattern, string, flags=0)

import re

sentence = "Bengaluru is IT Capital of India and it's also Capital city for Karnataka state!"
matchObj = re.match( r'(.*) also (.*?) .*', sentence, re.M|re.I)
if matchObj:
    print("matchObj.group() : ", matchObj.group())
    print("matchObj.group(1) : ", matchObj.group(1))
    print("matchObj.group(2) : ", matchObj.group(2))
else:
    print("Nothing found!!")
