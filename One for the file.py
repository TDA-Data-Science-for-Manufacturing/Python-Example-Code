# Databricks notebook source
# DBTITLE 1,One for the file
# MAGIC %md
# MAGIC file handling in Python

# COMMAND ----------

# DBTITLE 1,Reading data from a file
#Run this code and then annotate each line

with open('test.txt','r') as file:
  for line in file:
    print(line) 

# COMMAND ----------

# DBTITLE 1,Splitting Lines
#Run this code and then annotate each line

with open('student_data.txt','r') as file:
  for line in file:
    line = line.split(",")
    print(line[1].rstrip(), line[0]) 

# COMMAND ----------

# DBTITLE 1,Write to file
def save_to_file(name, age, form):
  with open('new_data.txt','a') as file:
    line = ','.join([name,age,form])
    file.write(line + '\n')
    file.close

firstname = input('Enter your first name: ')
surname = input('Enter your surname:' )
age = input('Enter your age')
save_to_file(surname, firstname, age)

# COMMAND ----------

# DBTITLE 1,Read from CSV
import csv

with open("csvdata.csv", "r") as csvfile:
    reader = csv.reader(csvfile)
    for line in reader:
        print(line[1], line[0])

# COMMAND ----------

# DBTITLE 1,CSV Read to array
datalist = []

with open("csvdata.csv", "r") as csvfile:
    reader = csv.reader(csvfile)
    for line in reader:
        datalist.append(line)
        
print(datalist)

# COMMAND ----------

# DBTITLE 1,Write to CSV
with open('csvdata.csv', mode='a') as csv_file:
    character_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    character_writer.writerow(['Margo', 'Gru'])
    character_writer.writerow(['Edith', 'Gru'])
    character_writer.writerow(['Agnes', 'Gru'])

# COMMAND ----------

# DBTITLE 1,Attendance
#imprt the csv library
import csv

#function to open the file and return name list
def openfile():
    names = []
    
    #open the csv file in read mode
    with open("csvdata.csv", "r") as csvfile:
        reader = csv.reader(csvfile)
       #for each line in the file add the data to the name list 
        for line in reader:
            #add the data from the line to the end of end of the names list
            names.append(line)
            
    #return the list of names        
    return names

#function to take attendance
def takeattendance(name_list):
    attendance_list = []

    #loop through the name_list  
    for name in name_list:
        # check if attended
        promptstring = name[0] + " " + name[1] + " present? y/n:"
        attendance = input(promptstring)
        # add the first name second name and attendance to attendance_list
        attendance_list.append([name[0]] + [name[1]] + [attendance])

    #return attendance_list
    return attendance_list

#function to wirte data to csv file
def writefile(attendacelist):
    #open the csv file in append mode
    with open('attendance.csv', mode='a') as csv_file:
        attendance_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        # loop through the attendance list and write the data to a row in csv file
        for student in attendancelist:
            attendance_writer.writerow([student[0], student[1], student[2]])
            
    #print success message        
    print("Attendance logged successfully") 



#call open list - returns a 2d list of names [[firstname,surname],...]
namelist = openfile()

#call take attendancefunction passing the name list generated above
attendancelist = takeattendance(namelist)

#write the results to file  by caling the  write file function
writefile(attendancelist)
