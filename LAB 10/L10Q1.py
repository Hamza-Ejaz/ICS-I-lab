import math
def ball_collide(x1,y1,r1,x2,y2,r2):
    distance= math.sqrt((x2-x2)**2+(y2-y1)**2)
    sumradi=r1+r2
    if (distance<=sumradi):
        return True
    else:
        return False
print("Enter the First Ball Co-Ordinates")
x1=int(input("Enter the value of x1: "))
y1=int(input("Enter the value of y1: "))
r1=int(input("Enter the value of r1: "))
print("Enter the Second Ball Co-Ordinates")
x2=int(input("Enter the value of x2: "))
y2=int(input("Enter the value of y2: "))
r2=int(input("Enter the value of r2: "))
func=ball_collide(x1,y1,r1,x2,x2,r2)
print("Whether the given two balls colliding? {}".format(func))
