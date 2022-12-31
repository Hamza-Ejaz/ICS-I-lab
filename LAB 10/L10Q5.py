def unique(elements):
    dictunique={}
    listunique=[]
    for i in elements:
        a=True
        for j in dictunique:
            if (i==j):
                dictunique[j]+=1
                a=False
        if(a):
            dictunique.update({i:1})
    for j in dictunique:
        if (dictunique[j]==1):
            listunique.append(j)
    return listunique
b=int(input("Enter the size of the list: "))
elements=[]
for i in range(b):
    elements.append(int(input("Enter an element: ")))
c=unique(elements)
print("The unique elements in the list are: ")
for j in c:
    print(j)
