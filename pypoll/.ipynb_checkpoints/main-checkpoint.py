import os
import csv

# Use the relative path to the CSV file
csv_path = os.path.join("pypoll", "resources", "election_data.csv")

# Initialize variables
total_votes = 0
candidate_votes = {}

# Read the CSV file
with open(csv_path, 'r') as file:
    csv_reader = csv.reader(file, delimiter=',')
    next(csv_reader)  # Skip the header row

    for row in csv_reader:
        total_votes += 1
        candidate_name = row[2]

        if candidate_name in candidate_votes:
            candidate_votes[candidate_name] += 1
        else:
            candidate_votes[candidate_name] = 1

# Calculate percentages and determine the winner
percentages = {candidate: (votes / total_votes) * 100 for candidate, votes in candidate_votes.items()}
winner = max(candidate_votes, key=candidate_votes.get)

# Print the results
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for candidate, votes in candidate_votes.items():
    print(f"{candidate}: {percentages[candidate]:.3f}% ({votes})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

# Ensure the output folder exists
output_folder = os.path.join("pypoll", "analysis")
os.makedirs(output_folder, exist_ok=True)
output_path = os.path.join(output_folder, "election_results.txt")

# Write the results to a text file
with open(output_path, 'w') as file:
    file.write("Election Results\n")
    file.write("-------------------------\n")
    file.write(f"Total Votes: {total_votes}\n")
    file.write("-------------------------\n")
    for candidate, votes in candidate_votes.items():
        file.write(f"{candidate}: {percentages[candidate]:.3f}% ({votes})\n")
    file.write("-------------------------\n")
    file.write(f"Winner: {winner}\n")
    file.write("-------------------------\n")
