import os
import csv

# Initialize variables
total_months = 0
net_total = 0
changes = []
greatest_increase = ["", 0]
greatest_decrease = ["", 0]

# Read the CSV file
with open('budget_data.csv' as file:
    csvreader = csv.reader(file)
    header = next(csvreader)  # Skip the header row

    for row in csvreader:
        # Calculate total months and net total
        total_months += 1
        net_total += int(row[1])

        # Calculate changes in profit/losses
        if total_months > 1:
            change = int(row[1]) - prev_profit
            changes.append(change)

            # Find greatest increase and decrease
            if change > greatest_increase[1]:
                greatest_increase = [row[0], change]
            if change < greatest_decrease[1]:
                greatest_decrease = [row[0], change]

prev_profit = int(row[1])

# Calculate average change
average_change = sum(changes) / len(changes)

# Print the results
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_total}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})")
print(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})")

# Write results to a text file
with open('financial_analysis.txt', 'w') as output_file:
    output_file.write("Financial Analysis\n")
    output_file.write("----------------------------\n")
    output_file.write(f"Total Months: {total_months}\n")
    output_file.write(f"Total: ${net_total}\n")
    output_file.write(f"Average Change: ${average_change:.2f}\n")
    output_file.write(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n")
    output_file.write(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n")

