students_marks={'Alice':85,'John':92,'Henry':79,'len':98}
try:
    a=input("Enter the student's name: ")
    print(a+"'s","marks is: ",students_marks[a])
except:
    print("Sorry,student not found.")