# Pull csv file to work with
import os
import csv

bank_csv = os.path.join("Resources","PyBank_Resource.csv")

#Open and read csv
with open(bank_csv, 'r') as csvfile:
    bank_reader = csv.reader(bank_csv, delimiter=',')

# Define/skip the header
csv_header = next(bank_reader)

# Definition block. Set variables and indexes to 0
net_total = 0
total_index = []
difference_index = []
profit_difference = 0
greatest_gain = 0
lamest_lost = 0
greatest_month = 0
lamest_month = 0

# Start loop

for row in bank_reader:
    #If row has a value
    if row != 0:
        # Look for date in 1st column, add to index, count index
        date = str(row[0])
        total_index.append(date)
        total_month = len(total_index)

        # Look at profit/losses column
        profit_losses = int(row[1])
        # Add profit/losses to a total
        net_total = profit_losses + net_total
        # Find the difference for greatest/lamest indications later
        profit_difference = profit_losses - profit_difference
        difference_index.append(profit_difference)

        # Reset profit_difference to remember for next loop
        profit_difference = row[1]

    # If the row in blank
    elif row == 0:
        # Reset profit difference
        profit_difference = row[1]

#calculations
average_total = int(net_total/total_month)

# Finding the max and min for the profit/losses
greatest_gain = difference_index.index(max(difference_index))
lamest_lost = difference_index.index(min(difference_index))
greatest_month = (date[int(greatest_gain)], max(difference_index))
lamest_month = (date[int(lamest_lost)], min(difference_index))

# Print statement in terminal
print(f'Financial Analysis:')
print(f'_____________________')
print(f'Total months: {total_month}')
print(f'Total: $ {net_total}')
print(f'Average Change: $ int{average_total}')
print(f'Greatest Increase in Profits:  {greatest_month}   {greatest_gain}')
print(f'Greatest Decrease in Profits:  {lamest_month}    {lamest_lost}')

# Print statement to txt file
# Text Path
PyBank_Holly = os.path.join(PyBank_Solved.txt)

# Open file to write
with open(PyBank_Holly, 'w') as txtfile:
    textfile.write(f'Financial Analysis:')
    textfile.write(f'___________________')
    textfile.write(f'Total months: {total_month}')
    textfile.write(f'Total: $ {net_total}')
    textfile.write(f'Average Change: $(int{average_total})')
    textfile.write(f'Greatest Increase in Profits: {greatest_month}  {greatest_gain}')
    textfile.write(f'Greatest Decrease in Profits: {lamest_month}    {lamest_lost}')