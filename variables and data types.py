#1. variables - a varibles is a container that holds a value
name="anjali"
age=19
height=5.6
is_student=True
print(name)
print(age)
print(is_student)
print(height)
""" variables naming rules 
1.start with letter or underscore 
2, can contain letters numbers, underscores
3.case-sensitive (age!=AGE)
4.use snake_case: my_variable(not myvariable)"""

#2.DATA TYPES - different kinds of values
#A.integer(int) - whole numbers(positive,negative,zero)
x=10
y=-5
z=0
print(x) #output 10

#B. float - decimal numbers
pi=3.14
height=5.9
temperature=-2.5
print(pi) #output:3.14

#C. string(str) - text/chracters (inside quotes)
name="tanvi"
city="ongole"
message="hello world"
print(name)  #output:tanvi

#D. boolean (bool)-true or false (logical values);
is_student=True
is_graduated=False
print(is_student) #output:True


#E.None - represents nothing / no value
x=None
print(x)


#3.type conversion 
#string to integer
age_str="19"
age_int=int(age_str)

# integer to string
num=100
num_str=str(num)
print(num_str)

#string to float 
price_str="9.99"
price_float=float(price_str)
print(price_float)

# check data  type
x=10
print(type(x))  #output: < class 'int'>

#4.comment
name="tanvi"  # this is single line comment
""" this is multi line comment
you can write many lines as much as you want
"""

#5.print & input
print("hello world")
print(20)
print(3.45)
name="tanu"
print(name)
#multi values
print("name:",name,"age:",10) 

#input from user
name=input("enter your name")
print(name)
#input always returns a string
# to convert in to string 
age=int(input("enter your age: "))
print(age)
# now it is an integer



# exercise 1: create variables
name="anjali"
age=19
height=5.6
is_student=True
print(name)
print(age)
print(is_student)
print(height)


# exerxise 2: type conersion 
name=int(input("enter your age:"))
year=int(input("enter your present year:"))
birth_year=year-age
print(birth_year)

# exercise 3: simple calculator
num1=int(input("enter the number"))
num2=int(input("enter the number"))
sum=num1+num2
print(sum)







