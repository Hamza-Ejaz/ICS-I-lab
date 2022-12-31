def cumupro(numbers):
    cumprodlist=[]
    prod=1
    for i in numbers:
        prod=prod*i
        cumprodlist.append(prod)
    return cumprodlist
b=int(input("Enter the size of the list: "))
numbers=[]
for i in range(b):
    numbers.append(int(input("Enter an element: ")))
c=cumupro(numbers)
print("The cumulative product of list of elemetns are: ")
for j in c:
    print(j)
