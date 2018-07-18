# Import Libraries
import os
import csv

# Init Variables/Lists
num_votes = 0

candidates = []

vote_counts = []

# Define Path
poll_data = "Resources/election_data.csv"
poll_path = os.path.join(poll_data)


#Open File
with open(poll_path, newline="") as csvfile:
    csvreader = csv.reader(csvfile)
    #Skip Header
    row = next(csvreader,None) 

    #count vote total as well as based on candidate/ add candidate to list of candidates if not already in list
    for row in csvreader:
        num_votes = num_votes + 1
        candidate = row[2]

        if candidate in candidates:
            candidate_index = candidates.index(candidate)
            vote_counts[candidate_index] = vote_counts[candidate_index] + 1
        else:
            candidates.append(candidate)
            vote_counts.append(1)

#Variable Init
vote_percents = []
high_votes = vote_counts[0]
max_index = 0
#Compares each candidates vote_count to the total num_votes, output X100 for percent
for count in range(len(candidates)):
    percent_votes = vote_counts[count]/num_votes*100
    vote_percents.append(percent_votes)
    #if an item in the list is greater than the last greatest item saved it replaces it, sets max index to the index of that candidate
    if vote_counts[count] > high_votes:
        high_votes = vote_counts[count]
        print(high_votes)
        max_index = count
#prints name of Candidate holding max_index as thier count
winner = candidates[max_index]
sumarry = (
    f"\nElection Results\n"
    f"--------------\n"
    f"Total Votes Cast: {num_votes}\n"
    f"Candidates: {candidates}\n"
    f"Winner: {winner}\n"
    f"Candidate Votes: {vote_counts}\n"
    f"Vote Percents: {vote_percents}\n"
)
#print Sumarry
# print(winner)
# print(*candidates)
# print(*vote_counts)
# print(vote_percents)
# print(num_votes)
print(sumarry)
txtOutputPath = os.path.join('Pypoll.txt')
with open(txtOutputPath, "w") as f:
    f.write(sumarry)