# Databricks notebook source
# DBTITLE 1,Selection
# MAGIC %md
# MAGIC Selection can be used to make choices in code

# COMMAND ----------

# DBTITLE 1,Selection Example
age = int(input("enter your age"))

if age > 18:
    print ("Welcome")
    

# COMMAND ----------

# DBTITLE 1,Number Comparison
number1 = int(input("Please enter a number"))
number2 = int(input("Please enter another number"))

if number1 > number2:
    print("The first number is greater than the second")

# COMMAND ----------

# DBTITLE 1,if-then-else
age = int(input("enter your age"))

if age > 18:
    print ("Welcome")
else:
    print("You are too young")

# COMMAND ----------

# DBTITLE 1,Compare Numbers - else
number1 = int(input("Please enter a number"))
number2 = int(input("Please enter another number"))

if number1 > number2:
    print("The first number is greater than the second")
else:
    print("The second number is greater than the first")

# COMMAND ----------

# DBTITLE 1,if-then-else
age = int(input("enter your age"))

if age > 18:
    print ("Welcome") 
elif age > 13:
    print("Ride with an adult")
else:
    print("You are too young")



# COMMAND ----------

# DBTITLE 1,Compare Numbers - elif
number1 = int(input("Please enter a number"))
number2 = int(input("Please enter another number"))

if number1 > number2:
    print("The first number is greater than the second")
elif number1 == number2:
    print("The numbers are equal")
else:
    print("The second number is greater than the first")

# COMMAND ----------

# DBTITLE 1,Born in a leap year?
year = int(input("what year were you born"))

if year%4 == 0:
    print("You were born in a leap year")
else:
    print("You were not born in a leap year")

# COMMAND ----------

# DBTITLE 1,Nesting
x = 1
y = 0


if x == 1:
    if y == 1:
        print("x is 1")
        print("y is 1")
    else:
        print("x is 1")
        print("y is something else")
else:
    print("x is something else") 

# COMMAND ----------

# DBTITLE 1,Boolean instead
if x == 1 and y == 1:
    print("x is 1")
    print("y is 1")
elif x == 1:
    print("x is 1")
    print("y is something else")
else:
    print("x is something else") 

# COMMAND ----------

# DBTITLE 1,Swimming Price Calculator
#set initial price as 0
price = 0

#get age of person
year = int(input("please enter age"))

#check if they have a discount card
card = input("do you have a discount card?")

if age < 65:
  if age > 18:
    if card == "y":
      price = 2.5
    else:
      price = 5
  else:
    price = 0
else:
  price = 0
  
print("The price for your swim is: £", price) 

# COMMAND ----------

# DBTITLE 1,Swimming Calculator Alternate
#set initial price as 0
price = 0

#get age of person
year = int(input("please enter age"))

#check if they have a discount card
card = input("do you have a discount card?")

#if child (under 18) or pensioner (over 65) - free
if age < 18 or age > 65:
  price = Free
#if they are not if they have a card - £2.50
elif card == "y":
  price = 2.50
#if not and don't have card - £5.00 
else:
  price = 5.00
  
print("The price for your swim is: £", price)
