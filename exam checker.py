medical=input("Did you have a medical cause Y or N: ")
attendance=int(input("Enter the attendance of the student: "))

if medical=="Y":
    print("You are allowed")
    
else:
    if attendance >= 75:
        print("Allowed")
        
    else:
        print("Not allowed")        
    