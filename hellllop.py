m = int(input("Enter number of elements in arr 1: "))
n = int(input("Enter number of elements in arr 2: "))
k = int(input("Enter k for minimum element: "))

arr1 = []
arr2 = []
arr3 = []

for i in range(m):
    element = int(input("Enter sorted elements in arr 1: "))
    arr1.append(element)

for j in range(n):
    element = int(input("Enter sorted elements in arr 2: "))
    arr2.append(element)

x = 0
y = 0

while x < m and y < n:
    if arr1[x] < arr2[y]:
        arr3.append(arr1[x])
        x += 1
    else:
        arr3.append(arr2[y])
        y += 1

while x < m:
    arr3.append(arr1[x])
    x += 1

while y < n:
    arr3.append(arr2[y])
    y += 1

minimum = arr3[k - 1]

print("kth minimum element is", minimum)