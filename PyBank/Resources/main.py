import csv
import os

# Define the path to the CSV file
csv_path = 'budget_data.csv'

# Check if the file exists
if not os.path.isfile(csv_path):
    print(f"File not found: {csv_path}")
    exit()

print(f"Reading file: {csv_path}")

# Initialize variables
total_months = 0
total_profit_losses = 0
previous_profit_loss = None
changes = []
greatest_increase = {'date': '', 'amount': float('-inf')}
greatest_decrease = {'date': '', 'amount': float('inf')}

# Open and read the CSV file
try:
    with open(csv_path, newline='') as csvfile:
        # Create a CSV reader object
        csvreader = csv.reader(csvfile, delimiter=',')
        
        # Read the header
        header = next(csvreader)
        
        # Loop through each row in the CSV
        for row in csvreader:
            date = row[0]
            profit_loss = int(row[1])
            
            # Calculate the total number of months
            total_months += 1
            
            # Calculate the net total amount of "Profit/Losses"
            total_profit_losses += profit_loss
            
            # Calculate changes in "Profit/Losses"
            if previous_profit_loss is not None:
                change = profit_loss - previous_profit_loss
                changes.append(change)
                
                # Check for greatest increase and decrease
                if change > greatest_increase['amount']:
                    greatest_increase = {'date': date, 'amount': change}
                if change < greatest_decrease['amount']:
                    greatest_decrease = {'date': date, 'amount': change}
            
            previous_profit_loss = profit_loss

    # Calculate the average change
    average_change = sum(changes) / len(changes)

    # Print the analysis results
    print("Financial Analysis")
    print("----------------------------")
    print(f"Total Months: {total_months}")
    print(f"Total: ${total_profit_losses}")
    print(f"Average Change: ${average_change:.2f}")
    print(f"Greatest Increase in Profits: {greatest_increase['date']} (${greatest_increase['amount']})")
    print(f"Greatest Decrease in Profits: {greatest_decrease['date']} (${greatest_decrease['amount']})")
except Exception as e:
    print(f"An error occurred: {e}")

# Writing analysis to text file
line="\n\n\n\n"


with open ("Analysis/pybank.txt","w") as bank:
    bank.write("Financial Analysis")
    bank.write(line)
    bank.write("----------------------------")
    bank.write(line)
    bank.write(f"Total Months: {total_months}")
    bank.write(line)
    bank.write(f"Total: ${total_profit_losses}")
    bank.write(line)
    bank.write(f"Average Change: ${average_change:.2f}")
    bank.write(line)
    bank.write(f"Greatest Increase in Profits: {greatest_increase['date']} (${greatest_increase['amount']})")
    bank.write(line)
    bank.write(f"Greatest Decrease in Profits: {greatest_decrease['date']} (${greatest_decrease['amount']})")
    
