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
 
print("-------------------------")
print("Election Results")   
print("-------------------------")
print("Total Votes :" + str(count))    
print("-------------------------")
for i in range(len(unique_candidate)):
            print(unique_candidate[i] + ": " + str(vote_percent[i]) +"% (" + str(vote_count[i])+ ")")
print("-------------------------")
print("The winner is: " + winner)
print("-------------------------")

# Print to a text file: election_results.txt
# Output perhaps needs to be rounded to 3 decimal points. Leaving that formatting out for now) 

with open('election_results.txt', 'w') as text:
    text.write("Election Results\n")
    text.write("---------------------------------------\n")
    text.write("Total Vote: " + str(count) + "\n")
    text.write("---------------------------------------\n")
    for i in range(len(set(unique_candidate))):
        text.write(unique_candidate[i] + ": " + str(vote_percent[i]) +"% (" + str(vote_count[i]) + ")\n")
    text.write("---------------------------------------\n")
    text.write("The winner is: " + winner + "\n")
    text.write("---------------------------------------\n")