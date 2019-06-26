#Marksheet program
k = 0
marks = [0, 0, 0, 0, 0]
while k < 5:
    marks[k] = int(input("Enter subject " + str(k+1) + " marks "))
    k += 1

total = marks[0] +  marks[1] +  marks[2] + marks[3] +  marks[4]
grade = total/5

print("\nYour toal marks are", total)
print("Your grade is", grade, "\n")

k = 0
while k < 5:
    print("Marks in subject ", str(k+1) , " are ", marks[k])
    k += 1

if grade > 90:
    print("Your grade is A+")
elif grade > 80:
    print("Your grade is A")
elif grade >= 70:
    print("Your grade is B")
else:
    print("You are fail")
    
    
