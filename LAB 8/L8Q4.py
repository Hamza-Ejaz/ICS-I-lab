name = []
salaries = []
personinfo = {}
j = 0
n = int(input("Enter the number of data: "))
for i in range(n):
    name.append(str(input("Enter name {}: ".format(i+1))))
    salaries.append(int(input("Enter salary {}: ".format(i+1))))
print("\nNames: {}".format(name))
print("Salaries: {}\n".format(salaries))
for j in range(len(name)):
    personinfo.update({name[j]:salaries[j]})
print(personinfo)
