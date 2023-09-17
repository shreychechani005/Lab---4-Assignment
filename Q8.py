n= int(input("Enter a number: "))
i = 2
while i<=n:
    if n%i==0:
        if n==i:
            print("This number is a prime number")
            break
        else:
            print("This number is not a prime number")
            break
    else:
        i= i+1