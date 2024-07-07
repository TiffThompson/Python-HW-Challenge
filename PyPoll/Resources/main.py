import csv

# Initialize variables
total_votes = 0
candidates_votes = {}
candidates_percentages = {}

#Define Path to the CSV file
csvpath = 'Resources\\election_data.csv'
output_file = 'election_results.txt'  # Name of the output file

# Open and  Read CSV file 
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Skip header
    next(csvreader)
    
    # Process each row
    for row in csvreader:
        total_votes += 1
        candidate_name = row[2]
        
        # Count votes for each candidate
        if candidate_name in candidates_votes:
            candidates_votes[candidate_name] += 1
        else:
            candidates_votes[candidate_name] = 1

# Calculate percentages
for candidate, votes in candidates_votes.items():
    percentage = (votes / total_votes) * 100
    candidates_percentages[candidate] = percentage

# Determine the winner
winner = max(candidates_votes, key=candidates_votes.get)

# Prepare the output string
output = (
    "Election Results\n"
    "-------------------------\n"
    f"Total Votes: {total_votes}\n"
    "-------------------------\n"
)

for candidate, votes in candidates_votes.items():
    output += f"{candidate}: {candidates_percentages[candidate]:.3f}% ({votes})\n"

output += (
    "-------------------------\n"
    f"Winner: {winner}\n"
    "-------------------------\n"
)

# Print results to terminal
print(output)

# Export results to text file
with open(output_file, 'w') as file:
    file.write(output)

print(f"Results have been exported to {output_file}")