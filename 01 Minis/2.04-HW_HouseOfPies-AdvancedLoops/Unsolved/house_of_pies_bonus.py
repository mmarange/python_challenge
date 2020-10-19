pies = ["Pecan",
      "Apple Crisp", 
      "Bean",
      "(4) Banoffee",  
      "(5) Black Bun",
      "(6) Blueberry",
      "(7) Buko", 
      "(8) Burek",  
      "(9) Tamale", 
      "(10) Steak"]

#print(pies)

print(f"Welcome to the House of Pies! Here are our pies:\n"
      f"---------------------------------------------------\n"
      f"(1) Pecann\n"
      f"(2) Apple Crisp\n"  
      f"(3) Bean\n"
      f"(4) Banoffee\n"
      f"(5) Black Bun\n" 
      f"(6) Blueberry\n" 
      f"(7) Buko\n"
      f"(8) Burek\n"  
      f"(9) Tamale\n" 
      f"(10) Steak\n"
        )

select = input("Please select which pie you would like to order via number: ")

print(f"Great! We'll have that {pies[int(select) - 1]} right out for you.")
