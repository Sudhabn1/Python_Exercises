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

# Write Operations
print("--------------------------")
write_some_data = open("c:/python_write_operation.txt", 'w')  # New File
write_some_data.write("Contents available in this file is been pushed via Python script!\n"
                      "However, you can read contents without any fees\n"
                      "By the way, are you from Bangalore city?")
write_some_data.close()
write_some_data = open("c:/python_write_operation.txt", 'r')
print(write_some_data.read())
write_some_data.close()
print("--------------------------")

# Reading Specific Lines
write_some_data = open("c:/python_write_operation.txt", 'r')
print(write_some_data.read(65))  # Specifically displaying few characters
write_some_data.close()
