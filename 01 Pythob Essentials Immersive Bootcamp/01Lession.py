#Create a variable
name="Andrey"
Anothername='Andrey2'
MultiStr="""This is a multi-line string. This is the first line."""

x=10
y=1.5
z=True

#Make the variablae name understandable
name_of_the_user="Andrey"

#Variable name rules
#1. Variable names must start with a letter or an underscore
#2. The rest of the name can contain letters, numbers, and underscores
#3. Variable names are case-sensitive
#4. Variable names cannot be a reserved word

#Case sensitive
name="Andrey"
Name="Andrey2"

#A variable can contained variable
x=10
y=x+1

#Operations for variables
x=10
y=5
z=x+y
z=x-y
z=x*y
z=x/y
z=x%y
z=x**y
z=x//y

#Adding to variables
x=10
x=x+1
x+=1

#assigning multiple variables
x,y,z=10,5
print(x)
print(y)
print(z)

player1=player2=player3="Andrey", "Andrey2", "Andrey3"
print(player1)
print(player2)
print(player3)

#Assign one value to multiple variables
x=y=z=10
print(x)
print(y)
print(z)

print(z, y, x)

#printing variables
x=10
print("I am ",x ,"years old")
print(x)
print("x")

#get the type of the variable
x=10
print(type(x))

x=1.5
print(type(x))

x=True
print(type(x))

x="Andrey"
print(type(x))