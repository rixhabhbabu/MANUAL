def avg(listt):
    return sum(listt)/len(listt)

length = int(input("Enter the Length: "))
l1 = []
for i in range(1,length+1):
    l1.append(int(input("Enter the Number: ")))
    
print(f"The Average of the list is: {avg(l1)}")    
    
