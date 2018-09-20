# import dependencies
import os
import csv

# variables
votes_number = []
candidates = []
file = os.path.join('election_data.csv')

# Module for reading CSV files through my desktop from which I execute my code
with open(file, 'r') as csvfile:
    csvread = csv.reader(csvfile)

    # skip header row
    next(csvread, None)

    # Iterating through the data
    for row in csvread:
        
        # spliting our row to strings represented as array
        row = row[0].split(',')
        candidate = row[2]
        
        # Looking if there is such candidate and increment its votes number
        if candidate in candidates:
            candidate_index = candidates.index(candidate)
            
            # if so --->> ++1 to candidate votes
            votes_number[candidate_index] += 1
        
        else:
            # if no ---> adding candidate
            candidates.append(candidate)
            votes_number.append(1)

# Printing results
print('Election result')
print('------------------------------')
print('Total votes ' + str(sum(votes_number)))
print('------------------------------')

# All our candidates are stored in candidates in the same order as their number of votes stored in votes_number
# Iterating over candidates, calculating percentages and printing votes number for each candidate
for candidate in candidates:
    print(candidate + ': ' + str(round(votes_number[candidates.index(candidate)] / sum(votes_number) * 100)) + '% '
          + '(' + str(votes_number[candidates.index(candidate)]) + ')')

#Printing the winner
print('------------------------------')
print('Winner' + ' ' + candidates[votes_number.index(max(votes_number))])
print('------------------------------')

# creating the new txt file
new_file = open("ElectionResults.txt", "w")

# writing results to the text file
new_file.write('Election result\n')
new_file.write('------------------------------\n')
new_file.write('Total votes ' + str(sum(votes_number)) + '\n')
new_file.write('------------------------------\n')

for candidate in candidates:
    new_file.write(candidate + ': ' + str(round(votes_number[candidates.index(candidate)] / sum(votes_number) * 100)) +
                   '% ' + '(' + str(votes_number[candidates.index(candidate)]) + ')\n')

new_file.write('------------------------------\n')
new_file.write('Winner' + ' ' + candidates[votes_number.index(max(votes_number))] + '\n')
new_file.write('------------------------------\n')
