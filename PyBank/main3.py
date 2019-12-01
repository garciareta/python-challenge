import os, csv
 
with open(os.path.join("budget_data.csv"), "r") as csvfile:

	# creating a csv reader object 
    csvreader = csv.reader(csvfile) 
    header=next(csvreader)
    datalist = list(csvreader)
    
    print(datalist)
# variables def
months = 0
netamount = 0
average = 0   
    
#  The total number of months included in the dataset
months = len(datalist)
print(months)

#  The net total amount of "Profit/Losses" over the entire period # List comprehension vs "normal" ASK HELP

netamount = sum(int(row[1]) for row in datalist)  

print(netamount)

#  The average of the changes in "Profit/Losses" over the entire period

#  The greatest increase in profits (date and amount) over the entire period

#  The greatest decrease in losses (date and amount) over the entire period

#  In addition, your final script should both print the analysis to the terminal and export a text file with the results.



  
