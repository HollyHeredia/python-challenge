# Pull csv file to work with
import os
import csv

bank_csv = os.path.join("Resources","PyBank_Resource.csv")

#Open and read csv
with open(bank_csv, 'r') as csvfile:
    bank_reader = csv.reader(bank_csv, delimiter=',')

# Define/skip the header
csv_header = next(bank_reader)
for row in bank_reader:

# Definition block. Set variables and indexes to 0
total_index = []
difference_index = []
net_total_index = []
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
        # Add profit_losses to Net total
        net_total_index.append(profit_losses)
        # Find the difference for greatest/lamest indications later
        profit_difference = profit_losses - profit_difference
        difference_index.append(profit_difference)

        # Reset profit_difference to remember for next loop
        profit_difference = row[1]

    # If the row in blank
    elif row == 0:
        # Reset profit difference
        profit_difference = row[1]

#calculations for average
# Adding together profit differences
net_profit_difference = sum(difference_index/len(difference_index)) 
# Round integer
net_profit_difference = round(net_profit_difference,2)

# Finding the max and min for the profit/losses
greatest_gain = difference_index.index(max(difference_index))
lamest_lost = difference_index.index(min(difference_index))
greatest_month = (date[int(greatest_gain)], max(difference_index))
lamest_month = (date[int(lamest_lost)], min(difference_index))

# Print statement in terminal
print(f'Financial Analysis:')
print(f'_____________________')
print(f'Total months: {total_month}')
print(f'Total: $ {sum(net_total_index)}')
print(f'Average Change: $ int{net_profit_difference}')
print(f'Greatest Increase in Profits:  {greatest_month}   {greatest_gain}')
print(f'Greatest Decrease in Profits:  {lamest_month}    {lamest_lost}')

# Print statement to txt file
# Text Path
PyBank_Holly = os.path.join(PyBank_Solved.txt)

# Open file to write
with open(PyBank_Holly, 'w') as txtfile:
    txtfile.write(f'Financial Analysis:')
    txtfile.write(f'___________________')
    txtfile.write(f'Total months: {total_month}')
    txtfile.write(f'Total: $ {sum(net_total_index)}')
    txtfile.write(f'Average Change: $(int{net_profit_difference})')
    txtfile.write(f'Greatest Increase in Profits: {greatest_month}  {greatest_gain}')
    txtfile.write(f'Greatest Decrease in Profits: {lamest_month}    {lamest_lost}')