# Databricks notebook source
# DBTITLE 1,Functional Skills
# MAGIC %md

# COMMAND ----------

# DBTITLE 1,Builtin Functions
num = 3.1472

print(round(num, 2))

# COMMAND ----------

print(eval("num + 1"))

# COMMAND ----------

import random

print(random.randint(1,5))
print(random.randint(1,num))


# COMMAND ----------

# DBTITLE 1,User Defined Functions
def square(number):
   squaredNumber = number**2
   return squaredNumber

answer = square(4)
print (answer)

# COMMAND ----------

# DBTITLE 1,Variable Scope
# Global Variable
#global variable
variableName = "value"

def mySubroutine():	
    #local Variable
    variableName = "Value"

