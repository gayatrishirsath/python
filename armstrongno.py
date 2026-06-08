n=int(input("Enter Number::"))
sum=0
temp=n
while n>0:
    ld=n%10
    sum=sum+(ld)**3
    n=n//10

if temp==sum:
    print("Number is Armstrong..")
else:
    print("Number is not Armstrong..!")
    
