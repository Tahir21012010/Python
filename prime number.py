num=int(input("enter the number"))
if num>2:
    for i in range(2,num):
        if num%i==0:
            print(num,"is not prime")
            break
    else:
        print(num,"is prime")
else:
    print("enter a valid number")