def nearlyequal(s1,s2):
    m=len(s1)
    n=len(s2)
    if (m-n>=0):
        a=m-n
    else:
        a=n-m
    if (a>1):
        return False
    else:
        j=0
        count=0
        i=0
        while (i<m)&(j<n):
            if (s1[i]==s2[j]):
                i+=1
                j+=1
            else:
                if (count==1):
                    return False
                else:
                    if(m>n):
                        i+=1
                    else:
                        if(m<n):
                            j+=1
                        else:
                            i+=1
                            j+=1
                    count+=1
        if (i<m)|(j<n):
            count+=1
        else:
            if (count==1):
                return True
            else:
                return False
s1=str(input("Enter string 1: "))
s2=str(input("Enter string 2: "))
a=nearlyequal(s1,s2)
if (a):
    print("string are Nearly Equal")
else:
    print("string are not Nearly Equal")
