#Libraries
import os
import csv
#Variables
totalv = 0
candidates = []
candidate_number = 0
candidate_votes = {}
votes = []
percentage = []

csvpath = os.path.join("..", "Resources", "election_data.csv")
with open(csvpath) as csvfile:
    #Read the data doc and separate with comas
    csvreader = csv.reader(csvfile, delimiter = ",")
    #skip the header
    csv_header = next(csvreader)

    #To search for the total amount of votes
    for row in csvreader:
        totalv +=1
        #Name of the candidates in a list
        candidate_name = row[2]
        if candidate_name not in candidates:
            candidates.append(candidate_name)
            candidate_votes[candidate_name] = 0
            candidate_number += 1

        #Sum de candidate votes
        candidate_votes[candidate_name] += 1

#collect the votes 
for i in candidates:
    votes.append(candidate_votes[i])
    
for avrg in range(0,(len(candidates))):
    #of the percentages append we obtain the votes divided by the total of votes times 100 (to obtain the percentage with three decimals)
    percentage.append(round(((votes[avrg]/totalv) * 100),3))
"takes the name of the winner"
winner = max(candidate_votes, key = candidate_votes.get)
"takes the number of higher votes"
winner_votes = candidate_votes.get(max(candidate_votes))

#Print on Terminal
print("Election Results")
print("------------------------------------------")
print("Total Votes: ", totalv)
print("------------------------------------------")
print(candidates[0], percentage[0], "% ","(",votes[0],")")
print(candidates[1], percentage[1], "% ","(", votes[1],")")
print(candidates[2], percentage[2], "% ","(",votes[2],")")
print("------------------------------------------")
print("Winner: ", winner,"with", winner_votes,"votes")
print("------------------------------------------")
# We join the txt file of the results
output_path = os.path.join("results.txt")

#Print to txt
with open(output_path, 'w') as txtfile:
    txtfile.write("Election Results\n")
    txtfile.write("-----------------------------------------\n")
    txtfile.write(f"Total Votes: {totalv}\n")
    txtfile.write("-----------------------------------------\n")
    txtfile.write(f"{candidates[0]}: {percentage[0]}% ({votes[0]}) \n")
    txtfile.write(f"{candidates[1]}: {percentage[1]}% ({votes[1]}) \n")
    txtfile.write(f"{candidates[2]}: {percentage[2]}% ({votes[2]}) \n")
    txtfile.write("-----------------------------------------\n")
    txtfile.write(f"Winner: {winner} with:{winner_votes} votes\n")
    txtfile.write("-----------------------------------------\n")