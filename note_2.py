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

# String
text_1 = "Hello" # string can be stated by ""
text_2 = 'World' # '' does the same work
text = text_1 + text_2 # + can connect two strings together
text = text * 3 # * followed by an integer can multiply a string
print("\n", text)

# Escape characters
print("\nUsing a linefeed '\\n' to start a new line \n\
Text followed by it will appare on the next line") # \n new line
print("Horizontal and vertical tab are \\t and \\v") # tab \t, vertical tab \v
print("Name\tAge\tGender\t\vBroody\t18\tM\t\vChad\t19\tM\t\vTemara\t17\tF")
print("This text will disappear when \r returns the carriage to the beginning \
Carriage return \\r indicated that the printer carriage \
should return to the beginning of the current line.") # Carriage return \r
print("\\f can clear the previous characters in cmd of some operating systems \
and show the following characters") # line feed \f
print("\\ can also tell the interpreter to treat \', \" and \\ as a common character \
rather than an escape character.") # \\ \" \'
print("\\0 is identical to a space in appearance \
but it is a null value in a string") # Null value /0
print("\\a can generate a beep sound in order to notice the user. \a") # warning tone \a
print("\\b is backspace which can delete one character followed by it.\b") # backspace \b