print("name: {}; age: {}".format("Jack", "18")) # position
print("name: {1}; age: {0}".format("19", "James")) # index
print("name: {0[0]}, age: {0[1]}".format(("Bill", "17"))) # index followed by index
print("This guy is {name} who is {age} years old.".format(age = 18, name = "Jack")) # keyword
print("server: {server}; ip: {0}; port: {1}".format("192.168.0.1", 8848, server = "iCloud"))

# "{:Filler Align Length}".format(obj)
# Filler: the character used to fill the spaces, default value is " "
# Aligh: < align left, > align right, ^ align middle
# Length: length of the formated string
# e.g "{:*^10}".format("Python") -> "**Python**"
print("{:$^50}".format(" Pay for these guys today "))

# use filler and float rounder together
# "{:Filler Align Length Decimal f}".format(float)
# e.g "{:!<10.5f}".format(3.14159265356) -> "3.14159!!!"
print("{:*^50}".format(" {0} worths ${1:.2f} ".format("Jack", 199.234141)))
print("{0:} worths {1:$^7.2f}".format("James", 12.3123123))

# providing arguments to format() with a **dictionary
# e.g "{key_1} example {key_2}".format(**{"key_1":1, "key_2":2}) -> "1 example 2"
print("{name} has a big {pet} which has a same name \
as its owner {name}".format(**{"name":"Jack Zou", "pet":"dog"}))

# convert integers to hexadecimal, decimalism, octonary, binary form with string.format()
print("{0:d} = 0x{0:x}".format(123))
print("{0:d} = 0o{0:o}".format(456))
print("{0:d} = 0b{0:b}".format(789))
print("{0:x}, {0:o}, {0:b}, {0:d} -> {0:d}".format(114514))
