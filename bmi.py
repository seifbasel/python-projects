height=float(input("enter your height in meters: "))
weight=float(input("enter your weight in kilos: "))
bmi=weight/(height**2)
print("your bmi is" ,bmi)
      
if bmi < 18.5 :
    print("under weight")
elif 18.5<bmi<25:
    print ("normal weight")
elif 25.5 < bmi < 30:
    print("over weight")
elif 30 < bmi < 50:
    print("very fat")
else:
    print("unknowen")