# import dependencies
import os
import csv

# variables
total_months = 0
total_rev = 0
greatest_inc = 0
greatest_dec = 0
greatest_inc_date = ""
greatest_dec_date = ""
file = os.path.join('budget_data.csv')

# Module for reading CSV files through my desktop from which I execute my python
with open(file, 'r') as csvfile:
    csvread = csv.reader(csvfile)

    # skip header row
    next(csvread, None)

    # count months
    for row in csvread:
        
        # splitting the string to an array
        row = row[0].split(',')
        
        # iterating thorugh the string
        total_months = total_months + 1
        total_rev = total_rev + int(row[1])
        
        if int(row[1]) >= greatest_inc:
            greatest_inc = int(row[1])
            greatest_inc_date = row[0]
        
        if int(row[1]) <= greatest_dec:
            greatest_dec = int(row[1])
            greatest_dec_date = row[0]

# calculating average revenue change
average_revenue_change = round(total_rev/total_months, 2)

# Printing the report
print("Financial Analysis")
print("--------------------------------------------")
print("Total Months: " + str(total_months))
print(f"Total: " + str(total_rev))
print("Average Revenue Change: $" + str(average_revenue_change))
print("Greatest Increase in Revenue: " + greatest_inc_date + " ($" + str(greatest_inc) + ")")
print("Greatest Decrease in Revenue: " + greatest_dec_date + " ($" + str(greatest_dec) + ")")

# creating the new txt file
new_file = open("analysis_1.txt", "w")

# writing the text file
new_file.write("Financial Analysis \n")
new_file.write("-------------------------------------------- \n")
new_file.write("Total Months: " + str(total_months) + "\n")
new_file.write("Total Revenue: $" + str(total_rev) + "\n")
new_file.write("Average Revenue Change: $" + str(average_revenue_change) + "\n")
new_file.write("Greatest Increase in Revenue: " + greatest_inc_date + " ($" + str(greatest_inc) + ")" + "\n")
new_file.write("Greatest Decrease in Revenue: " + greatest_dec_date + " ($" + str(greatest_dec) + ")" + "\n")