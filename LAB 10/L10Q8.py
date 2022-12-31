def gcd(a,b):
    if(b==0):
        return a
    else:
        return gcd(b,a%b)
def lcm(a,b):
    return (a*b)/gcd(a,b)
a=int(input("Enter the value of a: "))
b=int(input("Enter the value of b: "))
lccm=lcm(a,b)
gccd=gcd(a,b)
print("LCM of two numbers is: {}".format(lccm))
print("GCD of two numbers is: {}".format(gccd))
