import csv

# Initialize variables
total_votes = 0
candidates = {}
winner = ""
winner_votes = 0

# Read the CSV file
with open('election_data.csv', 'r') as file:
    csvreader = csv.reader(file)
    next(csvreader)  # Skip header row

    # Loop through each row in the CSV file
    for row in csvreader:
        total_votes += 1
        candidate = row[2]


# Count the votes for each candidate
        if candidate in candidates:
            candidates[candidate] += 1
        else:
            candidates[candidate] = 1

       # Calculate the percentage of votes each candidate won
for candidate, votes in candidates.items():
    percentage = (votes / total_votes) * 100
    candidates[candidate] = (percentage, votes) 

        # Determine the winner
    if votes > winner_votes:
        winner = candidate
        winner_votes = votes

# Print the analysis results
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for candidate, (percentage, votes) in candidates.items():
    print(f"{candidate}: {percentage:.3f}% ({votes})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")