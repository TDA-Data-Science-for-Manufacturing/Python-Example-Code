# Databricks notebook source
# DBTITLE 1,Array for lists
# MAGIC %md
# MAGIC Data structures in Python

# COMMAND ----------

# DBTITLE 1,List tasks
my_list = ["i","d","l","e"]

# COMMAND ----------

print(my_list)

# COMMAND ----------

del my_list[2:4]
print(my_list)

# COMMAND ----------

my_list[1] = "n"
print(my_list)

# COMMAND ----------

new_list = [“s”] + my_list
print(new_list)

# COMMAND ----------

new_list.append("g")
print(new_list)

# COMMAND ----------

new_list.insert(1,"t")

# COMMAND ----------

import random
letter = random.choice(new_list)
print(letter)

# COMMAND ----------

final_list = []
for i in new_list:
    final_list.append(new_list.index(i))

print(final_list)

# COMMAND ----------

print(sum(final_list))

# COMMAND ----------

print(len(final_list))


# COMMAND ----------

# DBTITLE 1,Printing Lists
my_list = ["one", "two", "three", "four"]
print(my_list[0])

# COMMAND ----------

my_list = ["one", "two", "three", "four"]

for i in my_list:
    print(i, end = ',') # Separates each element by a comma 

for i in reversed(my_list):
    print(i, end = '\t')    # Separates each element by a tab

# COMMAND ----------

# DBTITLE 1,List Program
#define the empty list
number_list = []

#loop ten times
for i in range(1,11):
    #get input from the user, cast as an int and assign to variable temp
    temp = int(input("enter a number"))
    #append the value of temp to the list number_list
    number_list.append(temp)
    
#assign the sum of all items in the list to the variable total using sum()
total = sum(number_list)

#calculate the average using the total divided by the length of the list  using len()
average = total/len(number_list)

#output the total and average to the screen 
print("The total of the numbers is:", total)
print("the total of the numbers is:", average)

#loop through each value (number) in number_list
for number in number_list:
    #print the correct statement for each number
    if number > average:
        print(number, "is above average")
    elif number == average:
        print(number, "is equal to the average")
    else:
        print(number, "is below average")

# COMMAND ----------

# DBTITLE 1,Other data structures
list = ["item1", "item2"]

tuple =("item1", "item2")

set = {"item1", "item2"}

dict ={"key1": "value1", "key2": "value2"} 


# COMMAND ----------

# DBTITLE 1,Strings as Lists
my_string = "Hello World"
print(my_string[0])

print(my_string[7:])

my_string[2]= "C"
