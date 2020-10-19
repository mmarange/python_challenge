# initiate variables
ans = 'y'
start = 0

while ans == 'y':
        numbers = input("How many numbers? ")
 # count numbers as requested by user       
        for i in range(start, int(numbers) + 1 + start):
            print(i)
            start += 1 
# 
        ans = input("Would you like to continue (y/n)? ")
       
    

        
