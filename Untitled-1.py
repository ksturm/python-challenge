totalmonth = 0
revenue = []
previous_monthly_rev = int(Budget_data[0][1])
avg_list = []

for item in budget_data
    

    totalmonth = totalmonth + 1
    revenue.append(int(item[1]))
    change = int(item[1] - previous_monthly_rev)
    previous_monthly_rev = int(item[1])
    avg_list.append(change)

    previous_monthly_rev = int(item[1])
Total_revenue = sum(revenue)
Avg = sum(avg_list)/len(avg_list)