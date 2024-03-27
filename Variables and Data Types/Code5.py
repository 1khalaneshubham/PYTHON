# Expression Execution

A,B = 2,3   # 2*3=6
Text = "@"  # 6*str = six time string yete
print(A*Text*B)  # keuu hila dala na

A,B = "4",5
Txt = "@"
print((A+Txt)*B)

A,B = 2,10
C = 4
print(A+B*C)

A,B = 10,7.0
C= A*B
print(C) # result in float

A,B = 1,2
C = A/B
print(C)

A,B = 1.5,3
C = A//B    # result of (A//B) is same as floor (A/B)
print(C,A/B) # float // int = float

A,B = 12,5
C = A//B
print(C)  # 2

A,B = -12,5
C = A//B
print(C)  # -3

A,B = 12,-5
C = A//B
print(C)  # -3

# Remainder is Negative when denominator is negative
A,B = -5,2
C = A%B
print(C)  # 1

A,B = 5,2
C = A%B
print(C)  # 1

A,B = 5,-2
C = A%B
print(C)  # -1