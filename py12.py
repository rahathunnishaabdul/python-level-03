print("Government of taminadu")
print("Electricity board")
print("-----------------")
print("bill receipt")
print("------------------")
no=int(input("Enter the EB-no:"))
name=input("Enter the customber name:")
prev=int(input("Enter the previous unit:"))
curr=int(input("Enter the current unit:"))
unit=curr-prev
print("unit consumed:",unit)
if(unit>=1000):
   amount=unit*10
   print("Amount to be paid:",amount)
elif(unit>=500):
   amount=unit*5
   print("Amount to be paid:",amount)
elif(unit>=100):
    amount=unit*2
    print("Amount to be paid:",amount)
else:
    print("Amount to be paid:",Nill)
    
                                     
