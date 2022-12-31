fname=str(input("Enter FileName: "))
a="E:\\desktop new stuff\\Ali Things\\tudy material\\Assignments\\ICs\\Lab8\\{}".format(fname)
f=open(a,"r")
filecontents=f.read()
noc=0
nol=1
now=1
for i in filecontents:
    noc+=1
    if (i=="\n"):
        nol+=1
    if ((i==" ")|(i=="\n")):
        now+=1
print("Number of lines : {}".format(nol))
print("Number of words : {}".format(now))
print("Number of characters : {}".format(noc))
f.close
