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
print()
print()
print("The total number of months included in the dataset: " + months)


#  The net total amount of "Profit/Losses" over the entire period


netamount = str(sum(int(row[1]) for row in datalist))  
print("The net total amount of 'Profit/Losses' over the entire period: " + netamount )


#  The average of the changes in "Profit/Losses" over the entire period
#  The greatest increase in profits (date and amount) over the entire period
#  The greatest decrease in losses (date and amount) over the entire period

total_diff = 0
change = []
for i in range(1, len(datalist)):
    diff = int(datalist[i][1]) - int(datalist[i-1][1])
    total_diff += int(diff)
    change.append(diff)
maxn = (max(change))
minn = (min(change))
total_average = (sum(change) /len(change))
total_average = str(round(total_average))
indexmax = change.index(maxn)
indexmin = change.index(minn)
print("The average of the changes in 'Profit/Losses' over the entire period: " + total_average)
print("The greatest increase in profits (date and amount) over the entire period: "  + datalist[indexmax+1][0] + " / " + str(maxn))
print("The greatest decrease in profits (date and amount) over the entire period: " + datalist[indexmin+1][0] + " / " + str(minn))

summary = "The total number of months included in the dataset: " + str(months) + "\n"\
+ "The net total amount of 'Profit/Losses' over the entire period: " + str(netamount)  + "\n"\
+ "The average of the changes in 'Profit/Losses' over the entire period: " + str(total_average) + "\n"\
+ "The greatest increase in profits (date and amount) over the entire period: "  + datalist[indexmax+1][0] + " / " + str(maxn)+ "\n"\
+ "The greatest decrease in profits (date and amount) over the entire period: " + datalist[indexmin+1][0] + " / " + str(minn)+ "\n"\


#  In addition, your final script should both print the analysis to the terminal and export a text file with the results.

f = open('summary.txt','w')
f.write(summary)
f.close()

  
