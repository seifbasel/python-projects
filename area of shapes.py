print("1 square")
print("2 tringle\n")
enter = int(input("enter the number of the your choice:"))
if enter == 1:
    Sidesq = int(input("enter the side lenght:"))
    areasq = Sidesq*Sidesq
    print("the area of the squareis:", areasq)
elif enter == 2:
    basetr = int(input("enter the base lenght:"))
    height = int(input("enter the height lenght:"))
    areatr = (.5*basetr*height)
    print("the area of the tringle is:", areatr)
else:
    print("input error")
