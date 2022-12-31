fname=str(input("Enter FileName: "))
a="E:\\desktop new stuff\\Ali Things\\tudy material\\Assignments\\ICs\\Lab8\\{}".format(fname)
f=open(a,"r")
filecontents=f.readlines()
for i in filecontents:
    line1=i.replace("\n","")
    b=""
    for j in range(len(line1)-1,-1,-1):
        b=b+line1[j:j+1]
    print(b)
f.close
