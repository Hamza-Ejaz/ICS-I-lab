dict={"EZZA":"19/11/2003","KINZA":"16/09/2004","NADEEM":"20/03/1965",
       "JALAL":"28/05/1996","KALEEM":"06/10/2000","FASIH":"08/01/1996",
       "GUL":"17/04/1992","HASSAN":"26/12/2001","QIRAT":"09/04/1974",
       "IRTIZA":"11/09/1995"}
date = str(input("Enter date(dd-mm-yyyy): "))
a = date.split("-")
DB = "/".join(a)
b = False
for i in dict:
    if(dict[i] == DB):
        c = i
        b = True
if(b):
    print("Date of Birth {} is found in the birthday dictionary".format(dict[c])
          +" whose name is {}.".format(c))
else:
    print("Date of Birth is not found....")
