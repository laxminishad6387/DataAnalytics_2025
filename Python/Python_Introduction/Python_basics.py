# check case sensitivity in python.that python is case sensitive or not
Z="pw"
z="wallah"
print(Z)  #pyhton is case sensitive language
print(z)  # in this file capital Z and small z are different variables



# print multiple variables in single print statement
x=10
y=20
z=30
print(x,y,z)  # it will print all the variables value with space in between them


# we have efficent way to declare multiple variables in single line
a,b,c=100,200,300
print(a,b,c)  # it will print all the variables value with space in between them

a,b,c= "python","great"   #it will give us  value error like that: ValueError: not enough values to unpack (expected 3, got 2)
print(a,b)


# we have  an efficient way to assign same value to multiple variables in single line
a=b=c="10"
print(a,b,c)  # it will print all the variables value with space in between them




# naming variables in python
2x=10  # it will give us syntax error like that: SyntaxError: invalid syntax
@a=10  # it will give us syntax error like that: SyntaxError: invalid syntax
1x=20  # it will give us syntax error like that: SyntaxError: invalid syntax
_name="pw"
print(_name)  # it will print the value of variable _name
x^^2=30  # it will give us syntax error like that: SyntaxError: invalid syntax
for=30  # it will give us syntax error like that: SyntaxError: invalid syntax. because for is a reserved keyword in python
For=30
print(For)  # it will print the value of variable For






# comparision operators in python
x=10
y=20
print(x==y)  # it will print False because 10 is not equal to 20
print(x!=y) # it will print True because 10 is not equal to 20
print(x>y)  # it will print False because 10 is not greater than 20
print(x<y)  # it will print True because 10 is less than 20
print(x>=y)  # it will print False because 10 is not greater than or equal to 20
print(x<=y)  # it will print True because 10 is less than or equal to 20
print(x is y)  # it will print False because 10 is not the same as 20
print(x is not y)  # it will print True because 10 is not the same as 20
print(x=y)  # it will give us syntax error like that: SyntaxError: invalid syntax.beacause we are using assignment operator instead of comparision operator






# Arithmetic operators in python
x=10
y=20
print(x+y)  # it will print 30 because 10+20=30
print(x-y)  # it will print -10 because 10-20=-10
print(x*y)  # it will print 200 because 10*20=200
print(x/y)  # it will print 0.5 because 10/20=0.5
print(x//y)  # it will print 0 because 10//20=0
print(x%y)  # it will print 10 because 10%20=10
print(x**y)  # it will print 100000000000000000000 because 10**20=100000000000000000000
print(+x)  # it will print 10 because +10=10
print(-x)  # it will print -10 because -10=-10




# uniary operators in python
x=10
y=20
print(++x)  # it will print 10 because ++10=10
print(--x)  # it will print 10 because --10=10






# how to check variable data type in python
x=10
print(type(x)) # it will print <class 'int'> because x is an integer variable
y=2.5
print(type(y)) # it will print <class 'float'> because y is a float variable
z=True
print(type(z)) # it will print <class 'bool'> because z is a boolean variable
a="python"
print(type(a)) # it will print <class 'str'> because a is a string variable
b=3+4j
print(type(b)) # it will print <class 'complex'> because b is a complex variable




