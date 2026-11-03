# Student marks calculate 

s1 = int(input('Enter hindi marks: '))
s2 = int(input('Enter maths marks: '))
s3 = int(input('Enter english marks: '))
s4 = int(input('Enter chemistry marks: '))
s5 = int(input('Enter physics marks: '))

total = s1 + s2 + s3 + s4 + s5
print("Total marks(500): ", total)

parsentage = (total / 500)*100
print("Parsentage: ", parsentage)

if parsentage >= 90:
    print("Grade A") 
elif  parsentage >= 80:
    print("Grade B")
elif   parsentage >= 60:
    print("Grade C")
elif  parsentage >= 40:
    print("Grade D")
else:
    print("Student is fail")    
