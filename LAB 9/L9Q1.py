fname=str(input("Enter FileName: "))
a="C:Users\\Hamza Ejaz\\Desktop\\LAB 9\\{}".format(fname)
f=open(a,"r")
filecontents=f.read()
Dict={}
for i in filecontents:
    b=list(Dict.keys())
    c=True
    for j in range(len(b)):
        if(b[j]==i):
            Dict[i]+=1
            c=False
    if(c):
        Dict.update({i:1})
b=list(Dict.items())
for j in range(len(b)):
    print("{} : {}".format(b[j][0],b[j][1]))
d=fname.split(".")
if (d[1]=="py"):
    print("Input file is Python program file")
elif (d[1]=="c"):
    print("Input file is C program file")
elif (d[1]=="txt"):
    print("Input file is Text program file")
f.close
