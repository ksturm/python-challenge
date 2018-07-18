
import pandas as pd

csv_path = "Resources/budget_data.csv"

Budget_df = pd.read_csv(csv_path)
chrono_df = Budget_df.set_index("Revenue")

total_months = len(Budget_df)


chrono_df.head()


total_rev = Budget_df[["Revenue"]].sum()
##print("Total Revenue: $" + Total_rev)

max_rev = Budget_df[["Revenue"]].max()
month_max = chrono_df.loc[max_rev, "Date"]


min_rev = Budget_df[["Revenue"]].min()
month_min = chrono_df.loc[min_rev, "Date"]


#may need to import as csv for this loop, does it work????

import os
import csv

budget_data = os.path.join("Resources", "budget_data.csv")

#initialize varibles and sets
date = []
dateDiff = []
revenue = []
DistinctMonths = []
revenueDiffList = []
totalRevenue = 0
previousRevenue = 0
biggestIncrease = ["", 0]
biggestDecrease = ["", 9999999999]

with open(budget_data, 'r') as csvfile:
    csvreader = csv.DictReader(csvfile, delimiter=',')
    next(csvreader, None)

    for row in csvreader:
        print(row['Date'])
        date.append(row['Date'])
        revenue.append(int(row['Revenue']))
        totalRevenue += int(row['Revenue'])
        # change = int(row[1] - previous_monthly_rev)
        # previous_monthly_rev = int(row[1])
        # avg_list.append(change)
        # previous_monthly_rev = int(row[1])
        revenueDiff = int(row['Revenue']) - previousRevenue
        previousRevenue = int(row['Revenue'])
        revenueDiffList = revenueDiffList + [revenueDiff]
        dateDiff = dateDiff + [row['Date']]
        
        if (revenueDiff > biggestIncrease[1]):
            biggestIncrease[0] = row['Date']
            biggestIncrease[1] = revenueDiff
        if (revenueDiff < biggestDecrease[1]):
            biggestDecrease[0] = row['Date']
            biggestDecrease[1] = revenueDiff

avgRevenue = round(sum(revenueDiffList) / len(revenueDiffList),2)
#Avg = sum(avg_list)/(len(avg_list)-1)

#could make this a function
sumarry = (
    f"\nFinancial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total Revenue: ${total_rev}\n"
    f"Average Revenue Change: ${avgRevenue}\n"
    f"Greatest Increase in Revenue: {biggestIncrease[0]} (${biggestIncrease[1]})\n"
    f"Greatest Decrease in Revenue: {biggestDecrease[0]} (${biggestDecrease[1]})\n")
print(sumarry)
# print("Financial Analysis"
# "----------------------------"
# "Total Months: " + total_months)
# print("Total Revenue: $" + total_rev)
# print("Average Change in Revenue: $" + Avg)
# print("Greatest Increase in Profits: " + month_max)
# print("Greatest Decrease in Profits: " + month_min)
txtOutputPath = os.path.join('PyBank.txt')
with open(txtOutputPath, "w") as f:
    f.write(sumarry)

#poiece together csv export from below, variables need changing


#cleaned_csv = zip(#title, price, subscribers, reviews, review_percent, length#)

# Set variable for output file
# output_file = os.path.join("pybank_output.csv")

# #  Open the output file, w for write mode  

# with open(output_file, "w", newline="") as datafile:
#     writer = csv.writer(datafile)

#     writer.writerow([#"Title", "Course Price", "Subscribers", "Reviews Left",
#                     #"Percent of Reviews", "Length of Course"#])
#     writer.writerows(#cleaned_csv)