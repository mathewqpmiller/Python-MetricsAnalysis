## Python Script for Homework Assignment number three, the PyBank portion. ##

# Import Modules
import os
import csv

# Path Directory
py_bank_csv = os.path.join("Resources","budget_data.csv")

# Create Lists 
profit = []
monthly_changes = []
date = []

# Initialize Variable 
count = 0
total_profit = 0
total_change_profits = 0
initial_profit = 0

# Read CSV
with open(py_bank_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    # For Loop
    for row in csvreader:    
      # Count Iteration
      count = count + 1 
      # Append Date
      date.append(row[0])
      # Append Profit
      profit.append(row[1])
      # Calculate Total Profit
      total_profit = total_profit + int(row[1])
      # Calculate Month-to-Month Change in Profits
      final_profit = int(row[1])
      monthly_change_profits = final_profit - initial_profit
      # Append Month-to-Month Change in Profits
      monthly_changes.append(monthly_change_profits)
      # Parse Calculated Profits
      total_change_profits = total_change_profits + monthly_change_profits
      initial_profit = final_profit
      # Calculate Average Change in Profits
      average_change_profits = (total_change_profits/count)
      # Find Max Increase in Profits 
      greatest_increase_profits = max(monthly_changes)
      # Find Min Increase in Profits
      greatest_decrease_profits = min(monthly_changes)

      increase_date = date[monthly_changes.index(greatest_increase_profits)]
      decrease_date = date[monthly_changes.index(greatest_decrease_profits)]
      
    print("----------------------------------------------------------")
    print("Financial Analysis")
    print("----------------------------------------------------------")
    print("Total Months: " + str(count))
    print("Total Profits: " + "$" + str(total_profit))
    print("Average Change: " + "$" + str(int(average_change_profits)))
    print("Greatest Increase in Profits: " + str(increase_date) + " ($" + str(greatest_increase_profits) + ")")
    print("Greatest Decrease in Profits: " + str(decrease_date) + " ($" + str(greatest_decrease_profits)+ ")")
    print("----------------------------------------------------------")

with open('financial_analysis.txt', 'w') as text:
    text.write("----------------------------------------------------------\n")
    text.write("  Financial Analysis"+ "\n")
    text.write("----------------------------------------------------------\n\n")
    text.write("    Total Months: " + str(count) + "\n")
    text.write("    Total Profits: " + "$" + str(total_profit) +"\n")
    text.write("    Average Change: " + '$' + str(int(average_change_profits)) + "\n")
    text.write("    Greatest Increase in Profits: " + str(increase_date) + " ($" + str(greatest_increase_profits) + ")\n")
    text.write("    Greatest Decrease in Profits: " + str(decrease_date) + " ($" + str(greatest_decrease_profits) + ")\n")
    text.write("----------------------------------------------------------\n")
