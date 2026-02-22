# start

# create an empty list grades:
# input grades from the user
# when the list has 10 valid grades exit the loop
# use while loop until isdigit, then convert to int
grade_s: list[int] = []
while (len(grade_s)) < 10:
    grade: str = str((input('Enter a grade:')))
    while not grade.isdigit():
        grade: str = str((input('Enter a grade:')))
        continue
    grade = int(grade)
    if grade < 0 and grade < 100:
        grade: str = str((input('Enter a grade:')))
        continue
# add the number to the list if it is between 0-100, if not - don't add it
    grade_s.append(grade)
# AFTER THE LOOP IS FINISHED:
#   calc the sum of the grades using for loop, print it
#   calc the avg, print it
sum_: int = 0
for grade in (grade_s):
    sum_ += grade
    continue
print('sum= ', sum_)
print(f'avrege= {sum_ // (len(grade_s))}')
#   remove the last grade (hint: use pop)
grade_s.pop()
print(len(grade_s))
#   find the minimum grade (use for loop) and remove it from the list  (hint: remove)
min_: int = None
max_: int = None
for grade in grade_s:
    if min_ == None or min_ > grade:
        min_ = grade
        continue
for grade in grade_s:
    if max_ == None or max_ < grade:
        max_ = grade
        continue
grade_s.remove(min_)
grade_s.insert(0, max_)
grade_s.insert(len(grade_s) // 2, max_)

sum2_: int = 0
for grade in (grade_s):
    sum2_ += grade
    continue
print('sum= ', sum2_)
print(f'avrege= {sum2_ // (len(grade_s))}')

print(grade_s)

#   find the maximum grade (use for loop) and add another max grade at the: (1) end of the list (2) at the middle

