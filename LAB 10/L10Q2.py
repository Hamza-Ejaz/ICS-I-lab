'''
def mean_median_mode(marks):
    su=0
    length=len(marks)
    for i in range(length):
        su=su+marks[i]
    mean=su/length
    marks1=marks
    marks1.sort()
    if (len(marks1)%2==0):
        mid=int(len(marks1)/2)
        median=(marks1[mid-1]+marks1[mid])/2
    else:
        median=marks1[int(len(marks1)/2)]
    dictmode={}
    mode=[]
    for i in marks:
        b=True
        for j in dictmode:
            if (i==j):
                dictmode[i]+=1
                b=False
        if(b):
            dictmode.update({i:1})
    frli=[0]
    for i in dictmode:
        if (dictmode[i]>frli[0]):
            mode.clear()
            frli.clear()
            mode.append(i)
            frli.append(dictmode[i])
        elif (dictmode[i]==frli[0]):
            mode.append(i)
    tup=(mean, median, mode)
    return tup
a=int(input("Enter number of marks: "))
c=[]
for i in range(a):
    c.append(int(input("Enter Number: ")))
print(mean_median_mode(c))
'''
'''
mode = []
mode.append(None)
for key, value in frequency.items():
    if value > largest:
        largest = value
        mode[0] = float(key)
 
    return average, median, mode
data = []
for i in range(int(input("Enter the size of the list: "))):
    data.append(float(input("Enter an element : ")))
mean, median, mode = mean_median_mode(data)
print(f"Mean = {mean}\nMedian = {median}\nMode = {mode}")
'''

