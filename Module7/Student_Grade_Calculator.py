#list of scores
scores = [20,19,15,14,12]

#calculate average
avg= sum(scores)//len(scores)
print("Average of the list is:", avg)

#determine grade using comparisons 
if avg == 20:
    grade = 'A+'
elif avg >=18: #if avg is between 18 and 19
    grade = 'A'
elif avg >=15:#if avg is between 15 and 17
    grade = 'B'
elif avg >=13:
    grade = 'C'
else:
    grade = 'F'
print("Grade is:", grade)

#Use assignment operators to update the student's grade

if avg % 10 >= 6: #avarage_score = 17 => 17 % 10 = 7
    grade += '+' #if grade is greater than or equal to 6, add a plus sign to the grade
    print("You received extra credit!")

print("New average is:", avg)
print("New grade is:", grade)
print(f"The student's Average score is: {avg}, and their is: {grade}.")
#or
# avg += 2 
# grade += "!"
# print("Updated average:", avg)
# print("Updated grade:", grade)


#Use membership operators to check if a specific score exists in the list of scores.
specific_score = 19
if specific_score in scores:
    print(f"Score {specific_score} exists in the list of scores.")
else:
    print(f"Score {specific_score} does not exist in the list of scores.")

#or
if 15 in scores:
    print("Score 15 exists in the list!")
else:
    print("Score 15 does not exist in the list!")


#use identity operators to compare two lists of scores.
scores_copy = scores  # Reference to the same list
scores_new = scores[:]  # Create a new list with the same values
if scores is scores_copy:
    print("scores and scores_copy refer to the same object.")
else:
    print("scores and scores_copy do not refer to the same object.")
if scores is scores_new:
    print("scores and scores_new refer to the same object.")
else:
    print("scores and scores_new do not refer to the same object.")


#Use bitwise operators to perform bitwise operations on the scores.
#first two scores are 20 and 19
result_and = scores[0] & scores[1]   # 20 & 19
print("Bitwise AND of first two scores:", result_and)

#first two scores are 20 and 19
result_or = scores[0] | scores[1]    # 20 | 19
print("Bitwise OR of first two scores:", result_or)

# shift left the first score by 1
result_shift = scores[0] << 1         # 20 << 1
print("Left shift of first score by 1:", result_shift)