# Databricks notebook source
def set_global_variable(global_variable):
    global_variable = 2
    return global_variable

global_variable = 1
global_variable = set_global_variable(global_variable)
print ("the global variable is:", global_variable)
