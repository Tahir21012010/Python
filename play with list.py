L = [2,4,6,7,8,3,6]
print("original list:", L)
count = 0
for i in L:
    count += 1
avg = count / len(L)
print("sum = ", count)
print("average = ", avg)
L.sort()
print("Smaallest element is:", L[0])
print("Largest element is:", L[-1])
