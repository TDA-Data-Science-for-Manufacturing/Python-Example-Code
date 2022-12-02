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

# COMMAND ----------

# DBTITLE 1,While
count = 1
while count <10:
	print (count)
	count += 1


# COMMAND ----------

# DBTITLE 1,Password Check
password = "letmein"
entry = False

while entry != password:
	entry = input("please enter your password")
    
print("Welcome in!")

# COMMAND ----------

# DBTITLE 1,Infine Loop
#while True:
		#print("This goes on forever")


# COMMAND ----------

# DBTITLE 1,break - continue 
guess = ""

while guess != "Rumplstiltskin":
    guess = input('Guess my name')
print("Correct")

# COMMAND ----------

guess = ""

while True:
    guess = input('Guess my name')
    if guess == "Rumplstiltskin":
        print("Correct")
        break
    print("Wrong!")

# COMMAND ----------

guess = ""

while True:
    guess = input('Guess my name')
    if guess != "Rumplstiltskin":
        print("Wrong!")
        continue
    print("Correct")
    break
        

# COMMAND ----------

# DBTITLE 1,Number Add
number = 1
total = 0

while number != 0:
    number = int(input("enter a number"))
    total += number
print(total)
