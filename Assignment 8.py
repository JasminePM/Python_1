#Grade Input for Each Subject

grade_inputcalc = float(input("Please input grade for Calculus: "))
grade_inputpsych = float(input("Please input grade for Psychology: "))
grade_inputstats = float(input ("Please input grade for Statistics: "))

#Calculating Grade Average
aver_grade = (grade_inputstats + grade_inputcalc + grade_inputpsych) / 3

#Processing Grade Average Range
if aver_grade >= 90:
    print("Grade Average is A")
elif 80 <= aver_grade <= 89:
    print("Grade Average is B")
elif 70 <= aver_grade <= 79:
    print("Grade Average is C")
elif 60 <= aver_grade <= 69:
    print("Grade Average is D")
else:
    print ("Grade Average is F")

#Output: Ask code to calculate the previous code
print(aver_grade)
