length = int(input("Enter the Length: "))
l1 = []
for i in range(1,length+1):
    l1.append(int(input("Enter the Number: ")))

print("The List before Sorting: " ,l1)
l1.sort(reverse=True)
print("The List after Sorting: " ,l1)    