# Databricks notebook source
def set_global_variable():
    global global_variable
    global_variable = 2
    print ("the global variable is:", global_variable)

global_variable = 1
set_global_variable()
print ("the global variable is:", global_variable)
