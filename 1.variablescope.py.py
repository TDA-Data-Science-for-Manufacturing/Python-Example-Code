# Databricks notebook source
def output_global_variable():
    print ("the global variable is:", global_variable)

global_variable = 1
output_global_variable()
print ("the global variable is:", global_variable)
