units=int(input("Please enter the number of the units you consumed: "))

if units<50:
    amount=units*2.60
    surcharge=25
    
elif units<=100:
    amount=units*3.25
    surcharge=35    
    
elif units<=200:
    amount=units*5.25
    surcharge=45  
    
    
else:
    amount=units*8.25
    surcharge=75             
    
total=amount+surcharge

print(f"Bill: {amount}") 

print(f"Tax: {surcharge}")

print(f"Total Bill: {total}")
   