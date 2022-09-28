import random

# random() returns a random number within (0.0, 1.0]
print("random():", random.random())

# seed(a) initialize the seed which is used to generate random numbers
# same seed generates same random numbers
random.seed(114514.1919810)
print("random() with fixed seed:", random.random())
random.seed() # default seed is the current time read from the OS

# randint(a, b) returns a random integer within [a, b]
print("Randint(1, 10) generates 10 random integers:", [random.randint(1, 10) for _ in range(10)])

# uniform(a, b) returns a random float within [a, b)
print("uniform(1, 10) generates 10 random floats:", [random.uniform(1, 10) for _ in range(10)])

# randrange(start, stop, step) randomly returns a integer with in range(start, stop, step)
# randrange(1, 10, 3) = choice([1,4,7])
print("randrange(1, 10, 3) generates 5 random integers:",\
    [random.randrange(1, 10, 3) for _ in range(5)])

# getrandbits(k) returns an integer with length k in binary representation
# getrandbits(1) = [0b1, 0b0].choice()
print("getrandbits(1) generates 10 random integers:", \
    [random.getrandbits(1) for _ in range(10)])

# choice(seq) randomly returns a term in seq
print("choice(list('python')):", random.choice(list("python")))

# shuffle(seq) randomly rearranges terms in seq and returns None
lst = [i for i in "Hello World!"]
shuffled_lst = lst.copy()
random.shuffle(shuffled_lst)
print(lst, "-> shuffle(seq) ->", shuffled_lst)

# sample(seq, k) randomly choices k elements from seq (iterable object) and returns result in a list
print("sample('Hello, world!', 8):", random.sample("Hello, world!", 8))
