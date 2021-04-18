## Python Script for Homework Assignment number three: PyBank ##

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
      mean_profit_change = (total_change_profits/count)
      # Find Max Increase in Profits 
      maximum_profit_increase = max(monthly_changes)
      # Find Min Increase in Profits
      maximum_profit_decrease = min(monthly_changes)

      increase_date = date[monthly_changes.index(maximum_profit_increase)]
      decrease_date = date[monthly_changes.index(maximum_profit_decrease)]

    # Print to Terminal 
    print("----------------------------------------------------------")
    print("PyBank Financial Analysis")
    print("----------------------------------------------------------")
    print("Total Months: " + str(count))
    print("Total Profits: " + "$" + str(total_profit))
    print("Average Change: " + "$" + str(int(mean_profit_change)))
    print("Greatest Increase in Profits: " + str(increase_date) + " ($" + str(maximum_profit_increase) + ")")
    print("Greatest Decrease in Profits: " + str(decrease_date) + " ($" + str(maximum_profit_decrease)+ ")")
    print("----------------------------------------------------------")

# Export Path
py_bank_output = os.path.join("Analysis","financial_analysis.txt")

# Export to File
with open(py_bank_output, 'w') as text:
    text.write("----------------------------------------------------------\n")
    text.write("  PyBank Financial Analysis"+ "\n")
    text.write("----------------------------------------------------------\n\n")
    text.write("    Total Months: " + str(count) + "\n")
    text.write("    Total Profits: " + "$" + str(total_profit) +"\n")
    text.write("    Average Change: " + '$' + str(int(mean_profit_change)) + "\n")
    text.write("    Greatest Increase in Profits: " + str(increase_date) + " ($" + str(maximum_profit_increase) + ")\n")
    text.write("    Greatest Decrease in Profits: " + str(decrease_date) + " ($" + str(maximum_profit_decrease) + ")\n")
    text.write("----------------------------------------------------------\n")
