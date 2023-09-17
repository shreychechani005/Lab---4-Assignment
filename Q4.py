N = int(input())   
count1 = 0
count2 = 0
while True:      
    X = int(input())  
    if X == -999 :      
        break
    elif X%N == 0 :  
        count1 += 1
    elif X % N != 0:    
        count2 += 1
print("Total numbers which are divisible by",N,":",count1)      
print("Total numbers which are not divisible by",N,":",count2)     