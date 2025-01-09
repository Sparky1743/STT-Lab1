"""
Grade Caluculator
"""

def grade_calculator(marks):
    """
    This function is used to calculate your grade.
    """
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
    return "F"

def print_your_grade(marks):
    """
    This function is used to print your grade in terminal.
    """
    if grade_calculator(marks) == "F":
        print("You have been failed.")
        print("Please meet your faculty advisor.")

    else:
        # prints the grade
        print(f"Your grade is {grade_calculator(marks)}")

# User input
m = int(input("Enter your marks: "))
# Run the function
print_your_grade(m)
