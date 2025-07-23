score = int(input("Enter your score: "))

if score < 0 or score > 100:
    print("Invalid score. Please enter a score between 0 and 100.")
    exit()

if score >= 90:
    grade = "A"

elif score >= 80:
    grade = "B"

elif score >= 70:
    grade = "C"

elif score >= 60:
    grade = "D"

else:
    grade = "F"

print(f"Your grade is: {grade}")