def dups(elements):
    dictdups={}
    listdups=[]
    for i in elements:
        a=True
        for j in dictdups:
            if (i==j):
                dictdups[j]+=1
                a=False
        if(a):
            dictdups.update({i:1})
    for j in dictdups:
        if (dictdups[j]>1):
            listdups.append(j)
    return listdups
b=int(input("Enter the size of the list: "))
elements=[]
for i in range(b):
    elements.append(int(input("Enter an element: ")))
c=dups(elements)
print("The duplicate elements in the list are: ")
for j in c:
    print(j)
