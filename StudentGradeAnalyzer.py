name = input("Enter Your Name: ")
marks = []
marks.append(int(input("Enter Marks Of Marathi: ")))
marks.append(int(input("Enter Marks Of Hindi: ")))
marks.append(int(input("Enter Marks Of English: ")))
marks.append(int(input("Enter Marks Of Java: ")))
marks.append(int(input("Enter Marks Of Python: ")))

print(marks)

#total = marks[0] + marks[1] + marks[2] + marks[3] + marks[4]
total = sum(marks) 
average = total / len(marks)

if average >= 90: 
    print("---------------------")
    print("Name: ", name)
    print("Average: ", average)
    print("Grade: A")
elif average < 90 and average >= 70: 
    print("---------------------")
    print("Name: ", name)
    print("Average: ", average)
    print("Grade: B")
elif average < 70 and average >= 50:
    print("---------------------")
    print("Name: ", name)
    print("Average: ", average)
    print("Grade: C")
elif average < 50 and average >= 35:
    print("---------------------")
    print("Name: ", name)
    print("Average: ", average)
    print("Grade: D")
else:
    print("---------------------")
    print("Fail")
    print("Average: ", average)
    print("Hope You're Well!")


