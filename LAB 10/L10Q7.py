def reverse(elements):
    reverselist=elements[::-1]
    return reverselist
b=int(input("Enter the size of the list: "))
numbers=[]
for i in range(b):
    numbers.append(int(input("Enter an element: ")))
c=reverse(numbers)
print("The Original list is: ")
print(numbers)
print("After reversing, all the elements the list becomes: ")
print(c)
