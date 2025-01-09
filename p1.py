# Grade Caluculator

# This function is used to calculate your grade.
def grade_calculator(marks):
    if marks >= 90:
        return "A+"
    elif marks >= 80:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 50:
        return "D"
    else:
        return "F"

# This function is used to print your grade in terminal.
def print_your_grade(marks):
    if grade_calculator(marks) == "F":
        print("You have been failed.")
        print("Please meet your faculty advisor.")

    else:
        # prints the grade
        print(f"Your grade is {grade_calculator(marks)}")

# User input
marks = int(input("Enter your marks: "))
# Run the function
print_your_grade(marks)
