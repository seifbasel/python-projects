print("tip calculator")
bill=int(input("enter your bill value:  "))
num_of_persons=int(input("how many people are there to split the bill?  "))
tip_percent=int(input("what percent do you want to pay as tip?  "))
one_should_pay=(bill/num_of_persons)
tip=((tip_percent/100)*bill)/num_of_persons
one_will_pay=(tip+one_should_pay)
print(f"each one will pay {one_will_pay}")