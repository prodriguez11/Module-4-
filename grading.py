# Calculating Grades (ok, let me think about this one)

# Write a program that will average 3 numeric exam grades, return an average test score, a corresponding letter grade, and a message stating whether the student is passing.

# Average	Grade
# 90+	A
# 80-89	B
# 70-79	C
# 60-69	D
# 0-59	F

# Exams: 89, 90, 90
# Average: 90
# Grade: A
# Student is passing.

# Exams: 50, 51, 0
# Average: 33
# Grade: F
# Student iis failing.

exam_one = int(input("Input exam grade one: "))

exam_two = int(input("Input exam grade two: "))                     #added int()

exam_three = int(input("Input exam grade three: "))                 #changed the number 3 to three and replaced str to int

grades = [exam_one,exam_two,exam_three]                             #added missing comas
sum = 0
for grade in grades:                                                #added an s to grade
   sum = sum + grade

avg = sum / len(grades)

if avg >= 90:
    letter_grade = "A"
elif avg >= 80 and avg < 90:                                       #added missing colon
    letter_grade = "B"
elif avg > 69 and avg < 80:
    letter_grade = "C"                                             #changed ' to "
elif avg <= 69 and avg >= 65:
    letter_grade = "D"
else:                                                              #changed elif to else:
    letter_grade = "F"

for grade in grades:
    print("Exam: " + str(grade))

    print("Average: " + str(avg))

    print("Grade: " + letter_grade)

if letter_grade is "F":                                            #changed dash to underscore
    print("Student is failing.")                                   #added missing parantheses
else:
    print("Student is passing.")                                   #added missing parantheses
