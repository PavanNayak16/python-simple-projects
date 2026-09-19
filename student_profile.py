name=input("Enter a name:")
Age=int(input("Enter a age:"))
college_name=input("Enter a college name:")
first_subject_marks=int(input("Enter a first subject marks:"))
second_subject_marks=int(input("Enter a second subject marks:"))
third_subject_marks=int(input("Enter a third subject marks:"))
total_marks=first_subject_marks+second_subject_marks+third_subject_marks
average=total_marks/3
college_name=college_name.upper()

print(f" STUDENT PROFILE \n Name : {name} \n Age : {Age} \n College Name : {college_name} \n Chemistry marks : {first_subject_marks} \n Mathematics marks : {second_subject_marks} \n Physics marks : {third_subject_marks} \n Average marks : {average}")