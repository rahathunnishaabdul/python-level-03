print("Nisha computer mart")
print("Nehru street,puducherry")
print("-----------------------")
print("Bill receipt")
print("--------------")
n=int(input("Enter the item no:"))
name=input("Enter your particular:")
rate=int(input("Enter the rate:"))
quantity=int(input("Enter the qunatity:"))
total=rate*quantity
print("toatl amount in rupees:",total)
if(total>=100000):
    gst=total*10/100
elif(total>=50000):
    gst=total*5/100
elif(total>=20000):
    gst=total*3/100
elif(total>=2/1000):
    gst=total*2/100
else:
    gst=total*1/100
print("gst(goods and service tax):",gst)
amount=total+gst
print("amoount to be paid:",amount)
