#Dependencies
import os 
import csv

#Variable for the data set 
total_votes = 0
khan_votes = 0
correy_votes = 0
li_votes = 0
otooley_votes = 0  

# Set path for the file 
csvpath = os.path.join(',','PyPoll','Resources','eletion_data.csv')

# Open and Read csv file 
with open(csvpath, newline='') as csvfile:
    # Set delimiter and variables 
    csvreader = csv.reader(csvfile, delimiter=',') 
    
    # Read the header of the row 
    csv_header = next(csvfile)
    