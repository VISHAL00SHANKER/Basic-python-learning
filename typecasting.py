#implicit
a = 2.5
b = 2
c = a + b
print(a, ":", type(a), '\n')
print(b, ":", type(b), '\n')
print(c, ":", type(c), '\n') # auto type convertion to float


#explicit
d = (str(c)) + " = a + b"
print(d, ":", type(d), '\n')
