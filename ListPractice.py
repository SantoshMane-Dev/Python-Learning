numbers = [10, 25, 7, 42, 18, 31]

# list practice only not methods
print("--------------------- Output -------------------------")
print("Element At Index 0: ", numbers[0])
print("Element At Last: ", numbers[-1])
print("Elements between index index of 0 to 2: ", numbers[0:2])
print("Reverse the String: ", numbers[::-1])
numbers[2] = 100;
print( "After Removing 7 to 100: " ,numbers)
numbers.append(50)
print("After Adding 50 At End: ", numbers)
numbers.remove(25)
print("After Removing 25 In List: ",numbers)
print("Printing The Final List: ")
print(numbers)

# string methods learning 

print("---------------------- Methods -----------------------")

number = [25, 10, 40, 10, 35, 20]

print("Count Use: ", number.count(10))
print("Index Of Use: ", number.index(35))
number.remove(10)
newString = number.pop(1)
print("Pop Method is Use: ", newString)
number.sort()
print("Sorting List: ", number)
number.reverse()
print("reverse List: ", number)
backup = number.copy()
print("Copied List: ", backup)
backup.append(100)
print("Appended Value 100: ", backup)
backup.clear()
print("Original List: ", number, "\n", "Backup List: ", backup)

print("------------------------------------------------------")
