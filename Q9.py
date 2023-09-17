n= input("Enter the sentence: ")
index= 0 
capital= 0
small= 0
digit= 0
special= 0
while index< len(n):
    i= n[index]
    if 'A'<=i and i <= 'Z':
        capital = capital+ 1
    elif 'a'<=i and i <= 'z': 
        small= small+1
    elif '0'<=i and i <= '9':
        digit= digit+1
    else:
        special= special+1
    index= index+1
print("Capital: ", capital)
print("Small: ", small)
print("Digit: ", digit)
print("Special:",special)