# type conversion

a = 2
b = 4.25
sum = a + b
print(sum)  # auto conversion

c = "10"
d = 4.30
# sum1 = c + d
# print(sum1) #TypeError: can only concatenate str (not "float") to str

e = int("2")
f = 30
sum3 = e + f
print(sum3)

b = 3.14
b = str(b)
print(type(b))