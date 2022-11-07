# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆

#156 178 165 171 187
#Write your code below this row 👇
print("Hello World!")
total_height = 0
for height in student_heights:
    total_height = total_height + height

number_of_students = 0
for number in student_heights:
    number_of_students += 1

total_height /= number_of_students
print(round(total_height))


