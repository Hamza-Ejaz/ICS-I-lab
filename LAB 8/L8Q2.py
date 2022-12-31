a = str(input("Input a string: "))
dict={}
for i in a:
    b = list(dict.keys())
    c = True
    for j in range(len(b)):
        if(b[j]==i):
            dict[i] += 1
            c = False
    if(c):
        dict.update({i:1})
b = list(dict.items())
for j in range(len(b)):
    print("Count of {} in {} is: {}".format(b[j][0],a,b[j][1]))
