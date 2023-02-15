# Databricks notebook source
# DBTITLE 1,Hello World
print("Hello World!")

# COMMAND ----------

# MAGIC %md
# MAGIC This demonstrates the code to output to the screen (and how cells work)

# COMMAND ----------

# DBTITLE 1,Assign variables
number1 = 22
number2 = 33

# COMMAND ----------

# MAGIC %md
# MAGIC variables store data for use later in the program.

# COMMAND ----------

# DBTITLE 1,Calculate total and Display
total = number1 + number2
print(total)

# COMMAND ----------

# MAGIC %md
# MAGIC They can be used in operations

# COMMAND ----------

# DBTITLE 1,User Input
number1 = input("Enter a number")
number2 = input("Enter a second number")

total = number1 + number2
print(total)

# COMMAND ----------

# DBTITLE 1,Casting
number1 = input("Enter a number")
number2 = input("Enter a second number")

total = int(number1) + int(number2)
print(total)

# COMMAND ----------

# MAGIC %md
# MAGIC Alternately if the inputted value will alway be treated as a number then cast at the point of input

# COMMAND ----------

# DBTITLE 1,Casting at point of input
number1 = int(input("Enter a number"))
number2 = int(input("Enter a second number"))

total = number1 + number2
print(total)

# COMMAND ----------

# DBTITLE 1,Mathematical Operators
print(7/5)
print(7//5)
print(7%5)
print(7//5, "r", 7%5)

# COMMAND ----------

# DBTITLE 1,Average
number1 = input("Enter a number")
number2 = input("Enter a second number")
number3 = input("Enter a third number")

average = (int(number1) + int(number2) + int(number3)) / 3
           
print("average:", average)
