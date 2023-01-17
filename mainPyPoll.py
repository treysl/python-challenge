#modules
import os
import csv

#set resource paths
election_csv = os.path.join('C:/Users/Wellmoney/OneDrive/Desktop/Data Visualization Bootcamp/Module 3-7 - Python/Module 3 - Python/Challenge/python-challenge/Starter_Code/Instructions/PyPoll/Resources/election_data.csv')

#empty dictionary for candidate vote counts to be stored
vote_count = {}

#empty dictionary for candidates to be stored
votes_candidates = {}

#total count of all votes
total_votes = 0

with open(election_csv, encoding="utf-8") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader) #skip header row
    
    #loop through the rows of data
    for row in csvreader:
       
        #count the total votes
        total_votes += 1
        
        #count the amount of votes per candidate
        if row[2] in vote_count:
            vote_count[row[2]] += 1
        
        #if a candidate isn't in the dictionary, add them and count a value of 1    
        else:
            vote_count[row[2]] = 1

#winner total votes variable            
winner_count = 0

#loop through the vote count dictionary to calculate vote % and determine a winner
for candidate in vote_count:
    
    #calculate and store the vote percentage
    votes_candidates[candidate] = (vote_count[candidate] / total_votes) * 100
    
    if vote_count[candidate] > winner_count:
        winner_count = vote_count[candidate]
        winner = candidate
        
#export and print the results to a txt file       
results_path = os.path.join('C:/Users/Wellmoney/OneDrive/Desktop/Data Visualization Bootcamp/Module 3-7 - Python/Module 3 - Python/Challenge/python-challenge/PyPoll/Analysis/Election Data Output')

#prints the first set of our results
with open(results_path, 'w', encoding="utf-8") as datafile:
    datafile.write("Election Results\n")
    datafile.write("---------------------------------\n")
    datafile.write(f"Total Votes: {total_votes}\n")
    datafile.write("---------------------------------\n")
    for candidate, votes in vote_count.items():
        datafile.write(f"{candidate}: {votes_candidates[candidate]:.3f}% ({votes})")
    
    datafile.write("--------------------------------\n")
    datafile.write(f"Winner: {winner}\n")
    datafile.write("--------------------------------\n")
