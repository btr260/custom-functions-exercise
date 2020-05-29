# custom-functions/my_functions.py

# TODO: define temperature conversion function here
def celsius_to_fahrenheit(c):
    return 32 + (c * 9 / 5)


# TODO: define gradebook function here
def numeric_to_letter_grade(score):
    if score >= 97.0:
        grade = "A+"
    elif score >= 93.0:
        grade = "A"
    elif score >= 90.0:
        grade="A-"
    elif score >= 87.0:
        grade = "B+"
    elif score >= 83.0:
        grade = "B"
    elif score >= 80.0:
        grade = "B-"
    elif score >= 77.0:
        grade = "C+"
    elif score >= 73.0:
        grade = "C"
    elif score >= 70.0:
        grade = "C-"
    elif score >= 67.0:
        grade = "D+"
    elif score >= 63.0:
        grade = "D"
    elif score >= 60.0:
        grade = "D-"
    else:
        grade = "F"

    return grade



if __name__ == "__main__":

    print("--------------------")
    print("CUSTOM FUNCTIONS EXERCISE...")

    print("--------------------")
    c = 14
    print("THE CELSIUS TEMP IS:", c, "DEGREES")
    f = celsius_to_fahrenheit(c)
    print("THE FAHRENHEIT EQUIVALENT IS:", f, "DEGREES")

    print("--------------------")
    score = 87.5
    print("THE NUMERIC SCORE IS:", score)
    letter_grade = numeric_to_letter_grade(score)
    print("THE LETTER-GRADE EQUIVALENT IS:", letter_grade)



# BAD PRACTICE to include variables in
# your function definition that aren't
# specifically passed in as a parameter
# for example:
# def bad_function(x):
#   x + y
