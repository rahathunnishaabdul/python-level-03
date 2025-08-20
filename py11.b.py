print("Takshashila university")
print("ongur,tindivanam")
print("------------------")
print("student mark list")
m1=int(input("Enter the python mark:"))
m2=int(input("Enter the DBMS mark:"))
m3=int(input("Enter the industry mark:"))
total=m1+m2+m3
print("total mark:",total)
avg=total/3
print("Average mark:",avg)
if m1>=30 and m2>=30 and m3>=30:
   print("Result:fail")
if total>=250:
   print("Grade:A Grade")
elif total>=200:
   print("Result:F Grade")
else:
   print("Grade:F Grade")
   print("Result:Fail")
   print("Grade:F Grade(failed)")
