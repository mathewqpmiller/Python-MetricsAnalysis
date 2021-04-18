## Python Script for Homework Assignment number three: PyPoll ##

# Import Module
import os
import csv

# Path Directory
py_poll_csv = os.path.join("Resources","election_data.csv")

# Create Lists
candidate_list = []
unique_candidate = []
vote_count = []
vote_percent = []

# Initialize Variable
count = 0

# Define Function
def get_results(data):
    
    # For Loop
    for row in data:
        # Count Iteration
        count += 1
        # If Statement: Append Names
        if row[2] not in unique_candidate:
            unique_candidate.append(row[2])
        # Count Votes
        vote_count.append(row[2])

    # For Loop
    for candidate in unique_candidate:
        # Candidate Vote Counts
        candidate_list.append(vote_count.count(candidate))
        # Candidate Vote Percentage
        vote_percent.append(round(vote_count.count(candidate)/count*100,3))

    # Poll Winner
    winner = unique_candidate[candidate_list.index(max(candidate_list))]
    
    # print results, use a loop for the number of uniqueCandidates
    print('PyPoll Election Results')
    print('--------------------------------')
    print(f'Total Votes: {count}')
    print('--------------------------------')
    for i in range(len(unique_candidate)):
        print(f'{unique_candidate[i]}: {vote_percent[i]}% {candidate_list[i]}')
    print('--------------------------------')
    print(f'Winner: {winner}')
    print('--------------------------------')

    # Export Path
    poll_output = os.path.join("election_results.txt")

    # Export Print
    with open(poll_output, "w") as txtfile:
        txtfile.write('PyPoll Election Results')
        txtfile.write('\n------------------------------------')
        txtfile.write(f'\nTotal Votes: {count}')
        txtfile.write('\n------------------------------------')
        for i in range (len(unique_candidate)):
            txtfile.write(f'\n{unique_candidate[i]}: {vote_percent[i]}% {candidate_list[i]}')
        txtfile.write('\n------------------------------------')
        txtfile.write(f'\nWinner: {winner}')
        txtfile.write('\n------------------------------------')

# Read CSV
with open(py_poll_csv, newline='') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')
    # Account for Header
    csv_header = next(csvfile)
    # Call Function
    get_results(csv_reader)
