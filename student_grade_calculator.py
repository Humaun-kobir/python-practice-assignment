# Example Output
# Student Name: Rahim
# Total Marks: 245
# Average: 81.67
# Grade: A+

name = input("Enter student's name: ")

sub1 = int(input("Enter marks for subject 1: "))
sub2 = int(input("Enter marks for subject 2: "))
sub3 = int(input("Enter marks for subject 3: "))


total_marks = sub1 + sub2 + sub3
average = total_marks / 3


if average >= 80:
  grade = "A+"
elif average >= 70:
  grade = "A"
elif average >= 60:
  grade = "B"
elif average >= 50:
  grade = "C"
else:
  grade = "F"

print()
print("Student Name:", name)
print("Total Marks:", total_marks)
print("Average:", average)
print("Grade:", grade)