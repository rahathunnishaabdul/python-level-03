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
if m1>=40 and m2>=40 and m3>=40:
   print("Result:pass")
if total>=250:
   print("Grade:o G rade")
elif total>=200:
   print("Result:A+ Grade")
else:
   print("Grade:B Grade")
   print("Result:Fail")
   print("Grade:no Grade(failed)")
