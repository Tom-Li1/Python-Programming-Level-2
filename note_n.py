# Semicolon
print("Semicolon at the end of a line is legal in python but unnecessary.");

# integers
a, b = 1, -1
w, x, y, z, = 0b00001111, 0o0020, 17, 0x0012
# 0b binary, 0o octonary, 0x hexadecimal
print("In python, integers are not limited in size") 
print(a, b, w, x, y, z)

# Float
print("\nHowever, float can only exist in the interval [-10^308, 10^308]")
a = 3.1415926 # Pi expressed by decimalism
b = 2.99792458e8 # Speed of light shown in scitific notation.
print("Pi = ", a, "; c = ", b)

# Complex
print("\nComplex is expressed in the form (a + bj), where a and b are real and imaginary part.")
cplx = (3 + 7j) # 1j = √-1
print("The real part and imaginary part of", cplx, "is", cplx.real, "and", cplx.imag)

# Conversion
a = 1
print("\nConverting 1 into integer, float and complex")
# complex(real part, imaginary part (0 if the second argument is not provided) )
print(int(a), float(a), complex(a, 0))



# Escape characters: \t \v \r \f \0 \a \b
print("Horizontal and vertical tab are \\t and \\v") # tab \t, vertical tab \v
print("Name\tAge\tGender\t\vBroody\t18\tM\t\vChad\t19\tM\t\vTemara\t17\tF")

print("This text will disappear when \r returns the carriage to the beginning \
Carriage return \\r indicated that the printer carriage \
should return to the beginning of the current line.") # Carriage return \r

print("\\f can clear the previous characters in cmd of some operating systems \
and show the following characters") # line feed \f

print("\\0 is identical to a space in appearance \
but it is a null value in a string") # Null value \0

print("\\a can generate a beep sound in order to notice the user. \a") # warning tone \a

print("\\b is backspace which can delete one character followed by it.\b") # backspace \b


# set
# sets are disordered, and do not contain any multiple and identical elements
# s = {1,1,2,2,3,3,} → {1,2,3}
s = {1,2,3,4,5}
t = {3,4,5,6,7}
print("Union: ", s | t, s.union(t)) # {1,2,3,4,5,6,7}, S∪T
print("Intersection: ", s & t, s.intersection(t)) # {3,4,5}, S∩T
print("Difference: ", s - t, s.difference(t)) # {1,2}, return a set contains elements in S but not in T
print("Symmetrical difference: ", s ^ t, s.symmetric_difference(t))  # {1,2,6,7}, union - intersection
print("A copy of s: ", s.copy()) # return a new set consists with elements of s but has different memory address

s = {0,1,2,3,4,5,6,7} # S includes T, hence S is a superset of T 
t = {3,4,5} # T is included by S, hence T is a subset of S
print("T is a subset of S: ", t.issubset(s)) # True
print("S is a superset of T: ", s.issuperset(t)) # True


# for-else
isbreak = eval(input("Break the for loop? (True / False): "))
for i in range(10):
    print(i, end = " ")
    if isbreak and i == 5:
        print("for loop is broken")
        break
else:
    # if for is not finished due to keyword "break", codes in the "else" part won't run
    print("for loop is finished without break")



# while-else
isbreak = eval(input("Break the while loop? (True / False): "))
a = 0
while a <= 10:
    print(a)
    a += 1
    if isbreak and a == 5:
        print("while loop is broken")
        break
else:
    # Similar to for loop, else part works only when while loop is finished rather than break
    print("while loop is finished without break")



# one-line expression of if-else
num = 0
print("num is 0" if num == 0 else "num is not 0")

lst = [1 if i > 5 else 2 for i in range(10)]
print(lst)

a = 1
num = "0" if a == 0 else "1" if a == 1 else 2
print(num)



# try -> except Error_1 -> except Error_2 -> except -> else -> finally
try:
    a, b = eval(input("Privide two integers in the form (a, b): "))
    c = a / b
except ZeroDivisionError:
    print("[ERRO] An integer cannot be devided by 0")
except:
    print("[ERRO] Unexpected error occurs, pls try again")
else:
    print("[INFO] No error occured, c =", c, sep = " ")
finally:
    print("[INFO] Program finished")



# Passing positional, keyword and variable arguments to a function
def test(a, b, c, d):
    return a + b + c + d
print(test(1, 2, 3, 4), test(1, 2, d = 3, c = 4))

def test(a, b, *c, **d):
    print("Positional argument a and b: ", a, b)
    print("Variable argument *c: ", c)
    print("Variable argumetn **d: ", d)
test(1, 2, 3, 4, 5, name = "Yapeng Giao", gender = "Male", age = "41")



# local and global variables
# A variable defined outside a function is a "global variable" 
a = 1 # a is an example
def calc():
    # variable defined in a function is a "local variable"
    # all local variables will be released in memory once the function is finished 
    b = a + 3 # b is a local variable of the function calc()
    print(b)
calc()
try:
    print(b)
except NameError:
    print('[ERRO] b is a "local variable" hence it is unable to call b outside function calc()')

n = 1 # n at here is a global variable
def calc_local(a, b):
    n = b
    # this n is a local variable existing in the memory space of calc()
    # hence assign the value of b to n does NOT affect the global one
    print(n) # locally, n = b
    return a + b

s = calc_local(2,2)
print(s, n) # but globally n = 1

def calc_global(a, b):
    global n 
    # keyword "global" tells the function that operate n in the global memory space
    n = b # this time, n at here is the global one rather than only existing in the function
    return a + b

s = calc_global(2, 3)
print(s, n) # n is assigned to a new value in calc_global()



# keyword "lambda" and anonymous function
# <function name> = lambda <arguments>: <expression>
f = lambda x, m, c: m * x + c
y = f(5,1,1)
print(y)
s = lambda *x: sum(x) # variable arguments built-in functions also works
print(s(1,2,3))



# modes of opening a file
try:
    f = open("test_file.txt", mode = "x")
except FileExistsError:
    # Texts are able to write into a file opend with mode "x" and "w"
    # but "x" causes FileExistError when file exists
    # while "w" covers the previous contents
    print("[ERRO] FileExistError")
else:
    f.write("abc")
    f.close()



# file.seek(offset, whence = 0)
# offset must be 0 when mode is not "b"
f = open("test_file.txt", "w")
f.write(" middle ")
f.seek(0, 1)
f.write("-middle-")
f.seek(0, 2)
f.write(" end ")
f.seek(0, 0)
f.write(" beginning wowowowowo") # existing texts will be covered
f.close()

with open("test_file.txt", "w") as f:
    for i in range(10):
        f.write("A line of text " + str(i) + "\n")
f = open("test_file.txt", "r")
print(f.read()) # return a string consists with all text
f.seek(0, 0)
# After reading through read() readline() readlines()
# the position of cursor will be altered
# method seek(0, 0) can place the cursor at the beginning of a text file for next reading 
print(f.readlines())
f.seek(0, 0)
for i in range(15):
    print(f.readline())
    input()



# one-dimentional data
data = ["Jack", "Broody", "Chad", "Mickey", "Temara"]
with open("one-dimentional data.csv", "w") as f:
    f.write(",".join(data) + "\n")

f = open("one-dimentional data.csv", "r")
data = f.read()[:-1].split(",")
print(data)



# Two-dimensional data
data = [
    ["Aame", "Age", "Gender", "Hobby"],
    ["Chad", "19", "M", "Assisting those who bullies"],
    ["Broody", "18", "M", "Bullying others"],
    ["Mickey", "16", "M", "Being bullied"],
    ["Temera", "17", "F", "Doing"]
]

# writing data into a .csv file
with open("two-dimensional data.csv", "w") as f:
    for line in data:
        f.write(",".join(line) + "\n")

# reading a .csv file and construct a [[], [], [], ...]
data = []
with open("two-dimensional data.csv", "r") as f:
    for line in f:
        data.append(line.rstrip("\n").split(","))
print(data)



# Some of built-in function of python3

# abs(x)
# return the absolute value of x
a = abs(-10) 
print(a) # a = 10

# all(iterable_object)
# return True if every element is True
print(all([1 == 1, 2 == 2, 3 == 1 + 2])) # True
print(all([1, 1, 0, ""])) # False

# any(iterable_object)
# return False if every element is False
print(any([0,0,0,1,0,0,0])) # True
print(any([0, "", 1 + 1 != 2, "1".isalpha()])) # False

# ascii(object)
# return a printable string of the provided object
print(ascii(True)) # 'True'
print(ascii("简体中文")) # non-ascii -> "'\\u7b80\\u4f53\\u4e2d\\u6587'"

# bin(int)
# Return the binary representation of an integer
print(bin(123)) # "0b01111011"

# bool(x)
# Returns True when the argument x is true, False otherwise.
print(bool(123), bool(0), bool(1+1==2))

# bytearray(x)
# Return a mutable array of bytes of x
print(
    bytearray("简体中文", "utf-8"),
    bytearray(10), # return an empty array with length 10
    bytearray([0,1,2,3,4,5,6,7,8,9])
)

# bytes(x)
# return a byte string of x
print(
    bytes("撒地方对方的", "gbk"), #b'\xc8\xf6\xb5\xd8\xb7\xbd\xb6\xd4\xb7\xbd\xb5\xc4'
    bytes(5), # b'\x00\x00\x00\x00\x00'
    bytes([12,13,14]) # b'\x0c\r\x0e'
)

# divmod(a, b)
# return (a // b, a % b)
print(divmod(20, 5), divmod(10, 3))



# import

# import <module>
# import all functions and classes to global scope
# Call statement: module.function() # call functions in the imported module

# import <module> as <new_name>
# import a module and assign a new name (usually shorter)
# Call statement: new_name.function()

# from <module> import <function 1>, <function 2>, <class 1>, ...
# import some of functions and classes from the module
# from <module> import *
# import all functions and classes of the module
# Call statement: function()