num_of_students = int(input("Enter the number of students: "))

sum = 0
count = num_of_students

while count > 0:
    mark = float(input(f"Enter Mark: ({count- 1 }) Remaining: "))
    sum += mark
    count -= 1 

average = sum/num_of_students

print(f"Your class average is {average}")