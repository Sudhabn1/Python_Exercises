"""
    In this article, you'll learn about Python file operations.
    More specifically, opening a file, reading from it, writing into it, closing it and various file methods.
"""

# Opening File

file_open = open("c:/python_file.txt")
print(file_open)  # We can see the path of file, mode of operation and additional details!
print("Class =", type(file_open))


# Reading Contents
print("--------------------------")
print(file_open.read())
print("--------------------------")