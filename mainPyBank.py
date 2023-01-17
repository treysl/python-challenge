import os
import csv

#set local pc path to data csv file
budget_csv = os.path.join("C:/Users/Wellmoney/OneDrive/Desktop/Data Visualization Bootcamp/Module 3-7 - Python/Module 3 - Python/Challenge/python-challenge/Starter_Code/Instructions/PyBank/Resources/budget_data.csv")

#set variables to use for math calculations
months = []
amounts = []
change = []
change_month = []
count = 0

#open and read csv
with open(budget_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    #skip the header row
    csv_header = next(csvfile)

    #read through each row of data after the header
    for row in csv.reader(csvfile):

        #on the first time through, we are going to run a conditional to find the data we need, and then set the new_amount for calculation
        if count == 0:
            #add 1 for first pass only - count the number of items
            count = count + 1
            #set amount for future calculations
            new_amount = int(row[1])
            #add the amount of items to "amounts" list
            amounts.append(int(row[1]))
            #add month to months list
            months.append(str(row[0]))
        else:
            #add amount to amounts list
            amounts.append(int(row[1]))
            #add month to months list
            months.append(str(row[0]))
            #calculate change
            change.append(int(int(row[1]) - new_amount))
            #append change month
            change_month.append(str(row[0]))
            #set new amount for next row
            new_amount = int(row[1])

    #calculate results based on for loop entries
    total_months = len(months)
    total_amount = sum(amounts)
    average_change = round(sum(change) / len(change_month), 2)
    max_change = max(change)
    index_increase = change.index(max_change)
    min_change = min(change)
    index_decrease = change.index(min_change)

#print the results using a long f-string
print(f'''Financial Analysis
----------------------------
Total Months: {total_months}
Total: ${total_amount}
Average Change: ${average_change}
Greatest Increase in Profits: {change_month[int(index_increase)]} (${max_change})
Greatest Decrease in Profits: {change_month[int(index_decrease)]} (${min_change})''')

#output a txt file with the results
output_path = os.path.join('C:/Users/Wellmoney/OneDrive/Desktop/Data Visualization Bootcamp/Module 3-7 - Python/Module 3 - Python/Challenge/python-challenge/PyBank/Analysis/Financial Analysis.txt')
with open(output_path, "w", newline='', encoding="utf-8") as datafile:
    print(f'''Financial Analysis
----------------------------
Total Months: {total_months}
Total: ${total_amount}
Average Change: ${average_change}
Greatest Increase in Profits: {change_month[int(index_increase)]} (${max_change})
Greatest Decrease in Profits: {change_month[int(index_decrease)]} (${min_change})''', file=datafile)
