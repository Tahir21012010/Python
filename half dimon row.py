rowSize = int(input("enter te number of rows: "))
if rowSize%2== 0:
    halfDimRow = int(rowSize/2)
else:
    halfDimRow = int((rowSize/2)+1)
space = halfDimRow
for i in range(1, halfDimRow + 1):
    for j in range(1, space + 1):
        print(end=" ")
        space = space-1
        num = 1
        for j in range(2*i-1):
            print(end=str(num))
            num = num + 1
        print()
    space = 1
    for i in range(1, halfDimRow):
        for j in range(1, space + 1):
            print(end=" ")
            space = space + 1
            num = 1
            for j in range(1, 2*(halfDimRow-i)):
                print(end=str(num))
                num = num + 1
            print()