# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 00:05:58 2020

@author: dell
"""
import os
import csv

# set path for csv file
csvpath =os.path.join("Resources", "budget_data.csv")

# open csv file
with open(csvpath) as csvfile:
     csv_reader = csv.reader(csvfile, delimiter=',')
     
     # Remove header from the dataset
     title = next(csv_reader, None)
     # print(title)
     months = []
     total_profit = []
     total_change = []
     
     for row in csv_reader:
         
         months.append(str(row[0]))
         total_profit.append(float(row[1]))
        
 
    
for i in range(len(total_profit)-1):
    profit_change =(total_profit[i+1] - total_profit[i])
    total_change.append(profit_change)
    #print(total_change)

increase = max(total_change)
decrease = min(total_change)
# =============================================================================
increase_index = total_change.index(increase)
decrease_index = total_change.index(decrease)
# =============================================================================



# =============================================================================
average_profit = sum(total_profit)/ len(months)
average_change = sum(total_change)/len(total_change)
# print(len(months))
# print(sum(total_profit))
# print(int(average_profit))
#print(sum(total_change)/len(total_change))


# =============================================================================
print(f"{months[increase_index + 1]} {increase}")
print(f"{months[decrease_index + 1]} {decrease}")
# =============================================================================
# ============================================================================