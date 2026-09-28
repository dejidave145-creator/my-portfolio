print("STUDENT GRADING SYSTEM")

name = input("Enter student name: ")
score = float(input("Enter student score: "))

if score < 0 or score > 100:
    print("Invalid score. Enter a score between 0 and 100.")

elif score >= 70:
    print(f"{name} scored {score} - Grade A")

elif score >= 60:
    print(f"{name} scored {score} - Grade B")

elif score >= 50:
    print(f"{name} scored {score} - Grade C")

elif score >= 45:
    print(f"{name} scored {score} - Grade D")

elif score >= 40:
    print(f"{name} scored {score} - Grade E")

else:
    print(f"{name} scored {score} - Grade F")