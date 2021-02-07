## Python Script for Homework Assignment number three, the PyBank portion. ##

# Interfacing with another os
import os
# What os to interface with
import csv

# Identify where the csv file path is located
pybank_csv = os.path.join("", "Resources","budget_data.csv")
## The total number of months included in the dataset

num_rows = 0


for row in open("budget_data.csv"):
    num_rows += 1

print(num_rows)

## The net total amount of "Profit/Losses" over the entire period


## Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes


## The greatest increase in profits (date and amount) over the entire period


## The greatest decrease in losses (date and amount) over the entire period

##Financial Analysis
##----------------------------
##Total Months: 86
##Total: $38382578
##Average  Change: $-2315.12
##Greatest Increase in Profits: Feb-2012 ($1926159)
##Greatest Decrease in Profits: Sep-2013 ($-2196167)
