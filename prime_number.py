range_value = int(input("Enter the value of n : "))  
  
for i in range(1, range_value + 2): #to include the n value also if it is prime number
    if i > 1: 
       for n in range(2, i): 
           if (i % n) == 0: 
               break
       else: 
           print(i)