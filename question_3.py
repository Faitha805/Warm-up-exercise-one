#3
# WITI has tasked you to automate a simple grading system. 
# As a python student, write a program using functions and conditions to display the grades that 
# the students will be receiving based on the mark scored in a subject. 
# The grades are:
# 90% - 100%  Grade is A
# 80% - 89%   Grade is  B
# 70% - 79%   Grade is C                                                        
# 60% - 69%   Grade is D                  
# 50% - 59%   Grade is E  
# < 50% Fail 


print("Grading Student's Mark")
#Entry of students marks
mark_scored = int(input("Enter the mark scored: "))

#Grading a students mark
if 90 <= mark_scored <= 100 :
    print("Grade is A")

elif 80 <= mark_scored <= 89 :
    print("Grade is B")

elif 70 <= mark_scored <= 79 :
    print("Grade is C")

elif 60 <= mark_scored <= 69 :
    print("Grade is D")

elif 50 <= mark_scored <= 59 :
    print("Grade is E")

else :
    print("Fail") 
