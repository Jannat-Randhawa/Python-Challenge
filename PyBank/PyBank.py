# Dependencies 
import os 
import csv

# Variables
total_months = 0
net_amount = 0
monthly_change = []
month_count = []
greatest_increase = 0
greatest_increase_month = 0
greatest_decrease = 0
greatest_decrease_month = 0

# Set Path For File
csvpath = os.path.join('.', 'PyBank', 'Resources', 'budget_data.csv')

# Open & Read CSV File
with open(csvpath, newline='') as csvfile:
    
    # CSV Reader Specifies Delimiter & Variable That Holds Contents
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Read header row
    # Set header row to skip to next row 
    csv_header = next(csvreader)
    row = next(csvreader)

    #Set variables + Calculate total months + Net amount  
    previous_row = int(row[1])
    total_months += 1 
    net_amount += int(row[1])
    greatest_increase = int(row[1])
    greatest_increase_month = row[0]

    #loop calculation 
    for row in csvreader: 

        #Calculate total months 
        total_months += 1 
        #Total Net amount 
        net_amount += int(row[1])

        #Calculate monthly change 
        revenue_change = int(row[1]) - previous_row 
        monthly_change.append(revenue_change)
        previous_profit = int(row[1])
        month_count.append(row[0])

        #Calulate greatest increase 
        if int(row[1]) > greatest_increase:
            greatest_increase = int(row[1])
            greatest_increase_month = row[0]
        
        # Calculate The Greatest Decrease
        if int(row[1]) < greatest_decrease:
            greatest_decrease = int(row[1])
            greatest_decrease_month = row[0]  



