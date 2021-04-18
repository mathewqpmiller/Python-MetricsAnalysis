## Python Script for Homework Assignment number three: PyPoll ##

# Import Module
import os
import csv

# Path Directory
PyPollcsv = os.path.join("Resources","election_data.csv")

# Create Lists
candidate_list = []
unique_candidate = []
vote_count = []
vote_percent = []

# Initialize Variable
count = 0

# Read CSV
with open(PyPollcsv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    
    # For Loop
    for row in csvreader:
        # Count Iteration
        count = count + 1
        # Append Candidates
        candidate_list.append(row[2])
    # For Loop
    for x in set(candidate_list):
        # Append Names
        unique_candidate.append(x)
        # Count Votes
        y = candidate_list.count(x)
        # Append Count
        vote_count.append(y)
        # Calculate Vote Percentage
        z = (y/count)*100
        # Append Vote Percentage
        vote_percent.append(z)
        
    winning_vote_count = max(vote_count)
    winner = unique_candidate[vote_count.index(winning_vote_count)]
    
# Note to TA: I have tried several ways to get the max of the votecount list and retrieve the name as Winner. But unsucessful. 
# Hence I am leaving that part out of this code. But Khan is the winner, I know!!!!
# Jake suggested: votecount = votecount["percentage"].sort_values()
# Print to terminal
# Output perhaps needs to be rounded to 3 decimal points. Leaving that formatting out for now) 
 
   # print results, use a loop for the number of uniqueCandidates
    print('PyPoll Election Results')
    print('--------------------------------')
    print(f'Total Votes: {count}')
    print('--------------------------------')
    for i in range(len(unique_candidate)):
        print(f'{unique_candidate[i]}: {vote_percent[i]}% {vote_count[i]}')
    print('--------------------------------')
    print(f'Winner: {winner}')
    print('--------------------------------')

    # set exit path
    poll_output = os.path.join("PyPollResults.txt")

    # write out results to text file
    with open(poll_output, "w") as txtfile:
        txtfile.write('PyPoll Election Results')
        txtfile.write('\n------------------------------------')
        txtfile.write(f'\nTotal Votes: {count}')
        txtfile.write('\n------------------------------------')
        for i in range (len(unique_candidate)):
            txtfile.write(f'\n{unique_candidate[i]}: {vote_percent[i]}% {vote_count[i]}')
        txtfile.write('\n------------------------------------')
        txtfile.write(f'\nWinner: {winner}')
        txtfile.write('\n------------------------------------')