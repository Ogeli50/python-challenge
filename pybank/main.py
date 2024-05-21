import os
import csv

# Use the relative path to the CSV file
csv_path = os.path.join("pybank", "resources", "budget_data.csv")

# Print the CSV path for debugging
print("CSV Path:", csv_path)

# Initialize variables
total_months = 0
net_total = 0
changes = []
greatest_increase = ["", 0]
greatest_decrease = ["", 0]

try:
    # Read the CSV file
    with open(csv_path, 'r') as file:
        csvreader = csv.reader(file)
        header = next(csvreader)  # Skip the header row

        prev_profit = None  # Initialize previous profit to None

        for row in csvreader:
            # Calculate total months and net total
            total_months += 1
            current_profit = int(row[1])
            net_total += current_profit

            # Calculate changes in profit/losses
            if prev_profit is not None:  # Check if this is not the first row
                change = current_profit - prev_profit
                changes.append(change)

                # Find greatest increase and decrease
                if change > greatest_increase[1]:
                    greatest_increase = [row[0], change]
                if change < greatest_decrease[1]:
                    greatest_decrease = [row[0], change]

            prev_profit = current_profit  # Update previous profit

    # Calculate average change
    average_change = sum(changes) / len(changes) if changes else 0  # Handle division by zero

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

except FileNotFoundError as e:
    print("Error: File not found. Please check the file path and try again.")
    print(e)
