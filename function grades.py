def grades(a,b,c):
        print ("your first subject degree is: ",a)
        print("your second subject degree is: ",b)
        print("your third subject degree is: ",c)
    
        sum1 = ((a+b+c)/3)
        if 100 >= sum1 >= 90:
            print("student grade is A")
        elif 90 > sum1 >= 80:
            print("student grade is B+")
        elif 80 > sum1 >= 65:
            print("student grade is B")
        elif 65 > sum1 >= 50:
            print("student grade is c")
        elif sum1 < 50:
            print("student failed")
        else:
            print("error")
    
for i in range(0, 5):
    a=int(input("inter your first degree: "))
    b=int(input("inter your second degree: "))
    c=int(input("inter your third degree: "))
    grades(a,b,c)
print("finshed")  
