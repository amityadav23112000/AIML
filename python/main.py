# python code
# lecture 1

print(10)
print('amit')
print("amit")
print(10.555)
print(True)
print(type(10))
print(type(20.55) == float)
print(type('a') == str)
print('a', 'b', 'c', 100.20, 10 + 2022)
print('a', end=' ')
print('b')
print(10, 30, 20, sep='*')

# data type -int ,string ,float,bool
# check using type() fn.

# --------------------------------------------------------------------------

# lecture -2

# Operators

# print(2+3)
# print(20-10)
# print(10*10)
# print(10/5)   division
# print(11//5) floor division
# print('amit' + 'yadav')  concat happen
# print('amit'+10) not possible

# print(3/2) print(1.5)
# print(3//2) floor division
# print(3%2)
# print(2**5)  power print 32
# print(abs(-3.5))
# print(round(3.55453453, 2))
# print(pow(2,5))

# s="amit"
# a=ord('a')  give ascii value
# print(a)

# comparison operator
#  == != >= <= > <
#  all give result 0 or 1
# True == 1 and false == 0

# logical operator
# and   or   not
# print(True and True)
# print(not True)
#  --------------------------------------------------------------

# lecture -3 typecasting

# print(int('1'))
# print(float('1'))
# print(bool(10))
# print(str('a'))
# print(bool(0.0))

# ----------------------------------------------------------------
# lecture 4 string

# print('amit' + '1' + 'yadav')
print('amit'*2)
# print(len('amit'))
print('-' * 20)
print('amit'[0])
# print a -- indexing
# print('amit'[-1]) print t  -- from last
print('amit'[-4:])
print('amit'[0:4])

print('amit'.upper())
# print('amit'.lower())
# print('  amit         '.strip()) - remove space
# print('amit'.replace('t', 'tt'))
# print('aaaaaa'.count('a'))
# print('aaaAAAA'.lower().count('a'))
# print('1'.isalnum())
# print('amit yadav. yadav'.title())
# print('amit yadav. yadav'.capitalize())
# -------------------------------------------
# lecture 5
# a = 10
# x = y = z = 0
# b, c, d = 1, 2, 3
# print(a)
# print(x, y, z)
# print(b, c, d)

# n = input("enter no: \n")  by default string  -- so typecast them
# print(n)

# Function	Description	Example
# math.sqrt(x)	   Square root	math.sqrt(16) → 4.0
# math.pow(x, y)	x raised to y	math.pow(2, 3) → 8.0
# math.factorial(x)	Factorial	math.factorial(5) → 120
# math.ceil(x)	    Round up	math.ceil(2.3) → 3
# math.floor(x)	    Round down	math.floor(2.7) → 2
# math.sin(x)	    Sine (x in radians)	math.sin(math.pi/2) → 1.0
# math.cos(x)	    Cosine	math.cos(0) → 1.0
# math.tan(x)	    Tangent	math.tan(math.pi/4) → 1.0
# math.log(x)	    Natural log	math.log(2.71828) → ~1.0
# math.log10(x)   	Base-10 log	math.log10(100) → 2.0
# math.exp(x)	    e^x	math.exp(1) → 2.71828...