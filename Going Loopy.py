# Databricks notebook source
# DBTITLE 1,Iteration
# MAGIC %md
# MAGIC repeating code

# COMMAND ----------

# DBTITLE 1,Definite Iteration
for counter in range (10):
    print(counter)

# COMMAND ----------

# DBTITLE 1,Twenty Numbers
for i in range(20):
    print(i)

# COMMAND ----------

# DBTITLE 1,Range()
for i in range(10):
    print(i)

for i in range(1, 11):
    print(i)

for i in range(0, 21, 2):
    print(i)


# COMMAND ----------

# DBTITLE 1,Repeating Message
msg = input("Please enter a message")
repeat = int(input("How many times do you want it to repeat?"))

for i in range(repeat):
    print(msg)

# COMMAND ----------

# DBTITLE 1,Repeating Message with count
msg = input("Please enter a message")
repeat = int(input("How many times do you want it to repeat?"))

for i in range(repeat):
    print(i, msg)

# COMMAND ----------

# DBTITLE 1,RepeatIng Message from one
msg = input("Please enter a message")
repeat = int(input("How many times do you want it to repeat?"))

for i in range(1, repeat +1):
    print(i, msg)

# COMMAND ----------

# DBTITLE 1,Times Table
timestable = int(input("What times table?"))

for i in range(1,13):
    print(i, "x", timestable, "=", i * timestable) 

# COMMAND ----------

# DBTITLE 1,Times Tables
timestable = int(input("What times table?"))

#loop for each timestable from 1 to required timestable
for i in range(1, timestable+1):
    # generate the timestable for each iteration
    for j in range(1,13):
        print(j, "x", i, "=", j * i) 
