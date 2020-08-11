import os 
import csv

#Set file path
csvpath = os.path.join("..", "PyBank","Resources", "budget_data.csv")

# Set variables
total_months = 0 
net_amount = 0 
monthly_change = []
month_count = []
greatest_increase = 0 
greatest_increase_month = 0 
greatest_decrease = 0 
greatest_decrease_month = 0 

#open csv file 
with open(csvpath, newline='') as csvfile: 

    #set file reader 
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read header row
    # Set header row to skip to next row 
    csv_header = next(csvreader)
    row = next(csvreader)

    # Next row command 

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

        #Calculate the greatest decrease 
        if int(row[1]) < greatest_decrease:
            greatest_decrease = int(row[1])
            greatest_decrease_month = row[0]  

        # Calculate The Average & The Date
        average_change = sum(monthly_change)/ len(monthly_change)

        highest = max(monthly_change)
        lowest = min(monthly_change)

        print(f"Financial Analysis")
        print(f"---------------------------")
        print(f"Total Months: {total_months}")
        print(f"Total: ${net_amount}")
        print(f"Average Change: ${average_change:.2f}")
        print(f"Greatest Increase in Profits:, {greatest_increase_month}, (${highest})")
        print(f"Greatest Decrease in Profits:, {greatest_decrease_month}, (${lowest})")

# Write the file 
output_file = os.path.join('.', 'PyBank', 'Resources', 'budget_data_revised.text')

with open(output_file, 'w',) as txtfile:

    txtfile.write(f"Financial Analysis\n")
    txtfile.write(f"---------------------------\n")
    txtfile.write(f"Total Months: {total_months}\n")
    txtfile.write(f"Total: ${net_amount}\n")
    txtfile.write(f"Average Change: ${average_change}\n")
    txtfile.write(f"Greatest Increase in Profits:, {greatest_increase_month}, (${highest})\n")
    txtfile.write(f"Greatest Decrease in Profits:, {greatest_decrease_month}, (${lowest})\n")