medical_cause=input("did you have a medical cause Y or N: ")
atten = int(input("Enter The attendence of the student: "))
if medical_cause == "Y":
    print("You are alowed")
else:
    if atten>=75:
        print("You are alowed")
    else:
        print("You are not alowed")
        