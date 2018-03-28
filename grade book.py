#Alan Arvizu
print ("Enter your grade for average to be calculated")

print(" algebra 2")

Algebra_2 = float(input("enter your grade: "))

print(" Ap chemistry")

Ap_chemistry = float(input("enter your grade: "))

print("computational thinking")

computational_thinking = float(input(" enter your grade: "))

print("geometry")

Ap_geometry = float(input("enter your grade: "))

print("Ap english") 

Ap_english = float(input("enter your grade: "))

student_grades = [Algebra_2,Ap_chemistry,computational_thinking,Ap_geometry,Ap_english,]

grade_average = (Algebra_2 + Ap_chemistry + computational_thinking + Ap_geometry + Ap_english) / 5

student_grades.append(grade_average)

print student_grades  

if grade_average in range(1,60):
    
    print ("student needs improvment")
    
elif grade_average in range(60,70):
 
 print ("student needs improvment")
 
elif grade_average in range (70,80):
 
    print("student is doing fairly well")
    
elif grade_average in range(80,90) :
     
     print("student is doing good")
     
elif grade_average in range(90,100):
    
    print("student is doing outstadning")
    
else:
    
    print ("your doing ok")
    
