a=int(input("Enter coefficient of x^2 : ")) 
b=int(input("Enter coefficient of x : "))   
c=int(input("Enter constant : "))  
x1=0
x2=0

d=((b**2)-(4*a*c))

if d<0: 
    print("Imaginary Equation")
elif d==0:  
    x1=(-b)/(2*a)
    x1=x2
else:   
    x1=(-b+(d**(0.5)))/(2*a)
    x1=(-b-(d**(0.5)))/(2*a)
print("Roots of the equation are",x1,x2)