
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
     
     # Create empty lists
     months = []
     total_profit = []
     total_change = []
     
     # Read through file and fill empty lists
     for row in csv_reader:
         
         months.append(str(row[0]))
         total_profit.append(float(row[1]))
        
 
#Analyse the data    
for i in range(len(total_profit)-1):
    profit_change =((total_profit[i+1] - total_profit[i]))
    total_change.append(profit_change)
    
increase = max(total_change)
decrease = min(total_change)

# =============================================================================
increase_index = total_change.index(increase)
decrease_index = total_change.index(decrease)
# =============================================================================

average_profit = int(sum(total_profit))/ int(len(months))
average_change = int(sum(total_change))/int(len(total_change))

# =============================================================================
output = (f'Financial Analysis\n====================\n'
          f'Total Months in Period: {len(months)}\n'
          f'Total Profit: {"${:,.2f}".format(sum(total_profit))}\n'
         f'Average Profit: {"${:,.2f}".format(int(average_profit))}\n'
         f'Average Profit Change: {"${:,.2f}".format(sum(total_change)/len(total_change))}\n' 
         f'Greatest Increase in Profits:{months[increase_index + 1]}  {"${:,.2f}".format(increase)}\n'
         f'Greatest decrease in Profits:{months[decrease_index + 1]}  {"${:,.2f}".format(decrease)}'
          )

print(output)
# =============================================================================
# Create text file
with open("Analysis/Analysis.txt", "w") as txt_file:
     txt_file.write(output)
