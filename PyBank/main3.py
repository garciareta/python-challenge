import os, csv
 
with open(os.path.join("budget_data.csv"), "r") as csvfile:

	# creating a csv reader object 
    csvreader = csv.reader(csvfile) 
    header=next(csvreader)
    datalist = list(csvreader)
    
    #print(datalist)
   
    
months = 0
netamount = 0 
    
#  The total number of months included in the dataset
months = str(len(datalist))
print("The total number of months included in the dataset: " + months)

#  The net total amount of "Profit/Losses" over the entire period 

netamount = str(sum(int(row[1]) for row in datalist))  

print("The net total amount of 'Profit/Losses' over the entire period: " + netamount )

#  The average of the changes in "Profit/Losses" over the entire period
total_diff = 0

for i in range(1, len(datalist)):
    diff = int(datalist[i][1]) - int(datalist[i-1][1])
    total_diff += int(diff)
    print(total_diff)



#  The greatest increase in profits (date and amount) over the entire period

#  The greatest decrease in losses (date and amount) over the entire period

#  In addition, your final script should both print the analysis to the terminal and export a text file with the results.



  
