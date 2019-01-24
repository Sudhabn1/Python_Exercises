"""
    Operators are the constructs which can manipulate the value of operands.
    Consider the expression 4 + 5 = 9. Here, 4 and 5 are called operands and + is called operator.
    Types of Operator:
        Python language supports the following types of operators.

            Arithmetic Operators
            Comparison (Relational) Operators
            Assignment Operators
            Bitwise Operators
            Membership Operators
            Identity Operators
            Operators Precedence
"""

# Example - Python Arithmetic Operators
# Assume variable A holds 21 and variable B holds 10, then −
A = 21
B = 10

C = A + B
print()
print("Addition, Value of C =", C)

C = A - B
print("Subtraction, Value of C =", C)

C = A * B
print("Multiplication, Value of C =", C)

C = A / B
print("Division, Value of C =", C)

C = A % B
print("Modulus, Value of C =", C)

C = A ** B
print("Exponent, Value of C", C)

print("--------------------------")


# Example - Python Comparison Operators
# Assume variable A holds 10 and variable B holds 20, then −
A = 10
B = 20

if A == B:
    print("A is equal to B")
else:
    print("A is not equal to B")

if A != B:
    print("A is not equal to B")
else:
    print("A is equal to B")

if A > B:
    print("A is greater than B")
else:
    print("A is less than B")

if A < B:
    print("A is less than B")
else:
    print("A is greater than B")

if A <= B:
    print("A is less than or equal to B")
else:
    print("A is more than or equal to B")

if A >= B:
    print("A is greater than or equal to B")
else:
    print("A is less than or equal to B")

print("--------------------------")


# Example - Python Assignment Operators
# Assume variable A holds value 34, then −
A = 34

C = A + B
print("C value of A + B ::", C)

C = 2   # Let's assume C's value is 2
C += A
print("C value of C += A ::", C)

C = 4   # Let's assume C's value is 4
C *= A
print("C value of C *= A ::", C)

C /= A
print("C value of C /= A ::", C)

C = 7   # Let's assume C's value is 7
C %= A
print("C value of C %= A ::", C)

C = 2   # Let's assume C's value is 7
C **= A
print("C value of C **= A ::", C)

C //= A
print("C value of C //= A ::", C)

print("--------------------------")


# Example - Python Bitwise Operators
# Assume variable A holds value 47 and B holds 33, then −

A = 47
B = 33

C = A & B
print("& Binary (AND) value =", C)

C = A | B
print("| Binary (OR) value =", C)

C = A ^ B
print("^ Binary (XOR) value =", C)

C = ~A
print("~ Binary (Ones Complement) value =", C)

C = A << 2
print("<< Binary (Left Shift) value =", C)

C = A >> 2
print(">> Binary (Right Shift) value =", C)

print("--------------------------")


# Example - Python Membership Operators
# Assume variable A holds value 39 and B holds 26, then −

A = 39
B = 26

new_list = [22, 29, 38, 30, 56, 64]

if A in new_list:
    print("A is present in new_list")
else:
    print("A is not present in new_list")

if B not in new_list:
    print("B is not present in new_list")
else:
    print("B is present in new_list")

print("--------------------------")


# Example - Python Identity Operators
# Assume variable A holds value 20 and B holds 20, then −

A = 20
B = 20

if A is B:
    print("A is equal to B, points to same memory locations!")
else:
    print("A is not equal to B")

if id(A) == id(B):
    print("A is equal to B by id() values, points to same memory locations!")
else:
    print("A is not equal to B")

A = 25  # Let's assume A's value is 25
if A is B:
    print("A is equal to B, points to same memory locations!")
else:
    print("A is not equal to B")

if id(A) == id(B):
    print("A is equal to B by id() values, points to same memory locations!")
else:
    print("A is not equal to B")

print("--------------------------")


# Example - Python Operators Precedence
# Assume variable A holds value 2, B holds 6, C holds 3 and D holds 8 then −

A = 2
B = 6
C = 3
D = 8

E = (A + B) * C / D     # (8 * 3) / 8
print("(A + B) * C / D results ::", E)

E = ((A + B) * C) / D   # (8 * 3) / 8
print("((A + B) * C) / D results ::", E)

E = (A + B) * (C / D)   # (8) * (3 / 8)
print("(A + B) * (C / D) results ::", E)

E = A + (B * C) / D     # 2 + (18 / 8)
print("A + (B * C) / D results ::", E)

print("--------------------------")

