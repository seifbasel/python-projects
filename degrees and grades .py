students_num = 5
subjects_num = 3
std1_list = []

for x in range(0, students_num):

    for i in range(0, subjects_num):
        std1_list.append(int(input("enter the student degrees:")))
    print("the student degrees is: ", std1_list)
    sum1 = ((sum(std1_list))/3)
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

    std1_list.pop()
    std1_list.pop()
    std1_list.pop()
