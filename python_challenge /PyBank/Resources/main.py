

#Libraries
import os
import csv

#Variables
total = 0
pl = 0
changes_month = []
months_list = []
pl_list = []

#Read .cvs and skip header
csvpath = os.path.join("budget_data.csv")
with open(csvpath) as csvfile:
    #Read the data doc and separate with comas
    csvread = csv.reader(csvfile, delimiter = ",")
    #skip the row of the header
    csv_header = next(csvread)
    #for each row we add the values
    for i in csvread:
        total = total + 1
        pl = pl + int(i[1])

    #I make lists that contain both all months on the file and all profits and losses.
        months_list.append(i[0])
        pl_list.append(float(i[1]))
    
    #While looping in the list, we go row by row making a sustraction to obtain the difference
    for i in range(1,(len(months_list))):
        changes_month.append(pl_list[i] - pl_list[i-1])
        #Round the value to two decimals round(value,decimals)       #The number of decimals
    avrg_change = round((sum(changes_month) / len(changes_month)),2)

    #Increases and Decreases
    inc= max(changes_month)
    dec= min(changes_month)
    increase = months_list[changes_month.index(inc) + 1]
    decrease = months_list[changes_month.index(dec) + 1]

#Printing on terminal
print("Financial  Analysis")
print("-----------------------------------------")
print("Total Months: ", total)
print("Total: $", pl)
print("Average Change in PL: $", avrg_change)
print("Greatest Increase in Profits: ", increase,"(", " $", inc,")")
print("Greatest Decrease in Profits: ", decrease, "("," $", dec,")")

#Write on txt file (\n skips a line)
output_path = os.path.join("analysis.txt")
with open(output_path, "w") as txtfile:
    txtfile.write("Financial Analysis\n")
    txtfile.write("------------------\n")
    txtfile.write(f"Total Months: {total}\n")
    txtfile.write(f"Total PL: ${pl}\n")
    txtfile.write(f"Average Change: ${avrg_change}\n")
    txtfile.write(f"Greatest Increase in Profits: {increase}( ${inc})\n")
    txtfile.write(f"Greatest Decrease in Profits: {decrease} (${dec})\n")
