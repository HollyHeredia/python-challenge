#Pull csv file to work with
import os
import csv

poll_csv=os.path.join('CodeResources','PyPoll_Resource_file.csv')

with open(poll_csv) as csvfile:
    csvreader = csv.reader(poll_csv, delimiter=',')
# Skip header
header = next(csvreader)
print(f'{header}')
# Definitions

votes = 0
votes_index = []
candidate_list = []
unique_candidate_index = []
percent_index = []

# Loop row
for row in csvreader:
# Total number of votes cast
votes = row[2]
    votes_index.append(votes)
    total_votes = len(votes_index)

# Complete list of candidates who received votes
# Made unique candidate index and when someone is not in the index, to add to it
    if row[2] not in unique_candidate_index:
        unique_candidate_index.append(row[2])

# Loop through unique candidate list and add votes
for candidate_list in unique_candidate_index:
# The total number of votes each candidate won
    candidate_list.append(votes_index.count(candidate_list))
# The percentage of each vote each candidate received
    percent_index.append(round(votes_index.count(candidate_list)/total_votes*100,3))

# Winner of the election based off the popular vote
winner = unique_candidate_index[unique_candidate_index.index(max(candidate_list))]

# Print block
print(f'Total votes = {total_votes}')
print(f'____________________________')
for p in range(len(unique_candidate_index)):
    print(f'{unique_candidate_index[p]}: {percent_index[p]}% {candidate_list[p]}')
print(f'___________________________________')
print(f'Winner: {winner}')
print(f'___________________________________')

# Text Path
PyPoll_Holly = os.path.join(PyPoll_Holly.txt)

# Open file to write
with open(PyPoll_Holly, 'w') as txtfile:
    txtfile.write(f'Total votes = {total_votes}')
    txtfile.write(f'____________________________')
for p in range(len(unique_candidate_index)):
    txtfile.write(f'{unique_candidate_index[p]}: {percent_index[p]}% {candidate_list[p]}')
    txtfile.write(f'___________________________________')
    txtfile.write(f'Winner: {winner}')
    txtfile.write(f'___________________________________')