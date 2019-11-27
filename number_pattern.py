value =int(input("Enter the n value : "))
y=3
for j in range(1, value+ 1):
    for k in range(1,j+1):
    
       x=3
       m=(x*k)
       n=str(j*'_')
        
    if (k == 1):
         print(y,end="")          
    else:
       print(n,m, end="")         
            
    print()

            
        