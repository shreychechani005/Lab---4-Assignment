X = int(input("Enter Number 1 :"))  
Y = int(input("Enter Number 2 :"))  
N = int(input("Enter the number to check divisibility : ")) 

count = X+1 
while count<Y:
    if N%count==0:  
        print(count)
        count=count+1
    else:
        count=count+1 