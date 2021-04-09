# Pull csv file to work with
import os
import csv

bank_csv = os.path.join("Resources","PyBank_Resource.csv")

#Open and read csv
with open(bank_csv) as csv_file:
    bank_reader = csv.reader(bank_csv, delimiter=',')

# Check that csv is reading properly by printing the header
    csv_header = next(csv_file)
    #print(f"Header: {csv_header}")

# Skip header row

# Find unique values of month/year and count them for final tally
# Set total_months to 0
total_month = 0
greatest_gain = 0
lamest_lost = 0

#Everytime the loop encounters a month/year to add 1 to count
for row[0] in bank_reader:
    if total_month != 0:
        total_month = total_month + 1
    else:
        total_month = total_month

# Net total of profits and loses

# Take the last value and subtract the first value

# Find first_value by taking the value that is in cell(1,1)
#first_value = csv_reader(1,1)

# find the last value of column 2 in the spreadsheet
#last_value = 0 

# Average of total changes of profits and loses
# Take total number of profits and divide by total_months
    average_total = int(net_total/total_month)

# Greatest increase in profits and loses over a time period
# Find the biggest number in the profits and loses column
   
for row[1] in csv_reader:
    net_total = sum(row[1])
    average_total = int(net_total/total_month)
    if row[1] >= greatest_gain:
        greatest_gain = row[1]
        greatest_month = row[0]
    elif row[1] < lamest_lost:
            lamest_lost = row[1]
            lamest_month = row[0] 
    else:
        greatest_gain = greatest_gain
        greatest_month = greatest_month
        lamest_lost = lamest_lost
        lamest_month = lamest_month


# Greatest decrease in profits and loses over a time period
        
# Export text file with results in addition to running it in the terminal
print(f'"Financial Analysis:')
print(f'_____________________')
print(f'"Total months: " + total_month')
print(f'"Total: $'+ net_total)
print(f'"Average Change: $" + int(average_total)')
print(f'"Greatest Increase in Profits: " + greatest_month + "  " + greatest_gain')
print(f'"Greatest Decrease in Profits: " + lamest_month + "   " + lamest_lost')