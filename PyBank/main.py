# Pull csv file to work with
import os
import csv

bank_csv = os.path.join("Resources","PyBank_Resource.csv")

#Open and read csv
with open(bank_csv, 'r') as csvfile:
    bank_reader = csv.reader(bank_csv, delimiter=',')

# Check that csv is reading properly by printing the header
    csv_header = next(bank_reader)
    #print(f"Header: {csv_header}")

# Find unique values of month/year and count them for final tally
# Set total_months to 0
net_total = 0
total_index = []
greatest_gain = 0
lamest_lost = 0
greatest_month = 0
lamest_month = 0

#Everytime the loop encounters a month/year to add 1 to count

for row in bank_reader:
    date = str(row[0])
    total_index.append(date)
    total_month = len(total_index)

# Net total of profits and loses

# Take the last value and subtract the first value

# Find first_value by taking the value that is in cell(1,1)
#first_value = csv_reader(1,1)

# find the last value of column 2 in the spreadsheet
#last_value = 0 
# Average of total changes of profits and loses
# Take total number of profits and divide by total_months
# Greatest increase in profits and loses over a time period
# Find the biggest number in the profits and loses column
   
for row in bank_reader:
    change_total = int(row[1])
    net_total = change_total + net_total

    if row[1] >= greatest_gain:
        greatest_gain = int(row[1])
        greatest_month = str(row[0])
    elif row[1] <= lamest_lost:
            lamest_lost = int(row[1])
            lamest_month = str(row[0]) 
    else:
        greatest_gain = greatest_gain
        greatest_month = greatest_month
        lamest_lost = lamest_lost
        lamest_month = lamest_month

average_total = int(net_total/total_month)
# Greatest decrease in profits and loses over a time period
        
# Export text file with results in addition to running it in the terminal
print(f'Financial Analysis:')
print(f'_____________________')
print(f'Total months: {total_month}')
print(f'Total: $ {net_total}')
print(f'Average Change: $ int{average_total}')
print(f'Greatest Increase in Profits:  {greatest_month}   {greatest_gain}')
print(f'Greatest Decrease in Profits:  {lamest_month}    {lamest_lost}')