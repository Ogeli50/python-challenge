import csv
import os
file_to_load = os.path.join("Resources","election_data.csv")
file_to_load = os.path.join("analysis","election_analysis.txt")

file_to_load

#Initialize an empty list to store the data
voter_data = 0






Read the csv File
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader (csvfile, delimeter=',')