
grade: int = 100
temperature: float = 37.5
is_adult: bool = True
name: str = 'Danny!'

# input all grades for class with 30 students
# print all grades
grades: list[int] = [100, 92, 99, 80]
names: list[str] = ['danny', 'moshe', 'suzi', 'sharon']
working: list[bool] = [True, False, True, True]
floats: list[float] = [3.4, 9.9999, -7.1]
comb: list[any] = [3.7, 1, 'danny', True]

list_of_lists: list[ list[int] ] = [ [], [1,2,3], [7,7,7,7,7,7] ]

list_numbers: list[int] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
# use the ':' --> each print 1 line of code
# print the numbers from 3-9
# print from start-5
# print from 6-end
# print all even numbers (zuggim)
# print all odd numbers (ei-zugim)
# print all multiple 5 numbers (mahpela 5)
# print in reverse

# print

print(grades)
print(working)
print(list_of_lists)

grades: list[int] = [100, 92, 99, 80]
grades.append(88)
grades.insert(0, 97)

print(f"{grades} len={len(grades)}")

#   0    1   2   3   4   5
# [97, 100, 92, 99, 80, 88]

grades.pop(4)  # remove index 4
print(grades, 'after pop index 4 [=80]')
grades.remove(92)
print(grades, 'after remove 92')

list1: list[int] = [1, 3, 5, 1, 1, 7, 1, 1, 0]
while 1 in list1:
    list1.remove(1)
print(list1)

print("'a' in ['a', 'b', 'c']?", 'a' in ['a', 'b', 'c'])
print("1 in [1, 2, 3]?", 1 in [1, 2, 3])

# run over the list items
#        0  1  2  3  4  5  6  7  8  -> range(9) len==9 -> 0 .. 8
list1 = [1, 3, 5, 1, 1, 7, 1, 1, 0]
for i in range(len(list1)):
    print(list1[ i ], end= ' ')

print()
for item in list1:
    print(item, end=' ')


# create an empty list grades:
'''
list[int] = []  # empty list
'''
# input grades from the user
# when the list has 10 valid grades exit the loop
# use while loop until isdigit, then convert to int
'''
grade_s = input('grade?')
while not grade.isdigit():
    grade_s = input('grade?')
grade = int(grade_s)  # work 100%   
'''
# add the number to the list if it is between 0-100, if not - don't add it
# AFTER THE LOOP IS FINISHED:
#   calc the sum of the grades using for loop, print it
#   calc the avg, print it
#   remove the last grade (hint: use pop)
#   find the minimum grade (use for loop) and remove it from the list  (hint: remove)
#   find the maximum grade (use for l0oop) and add another max grade at the: (1) end of the list (2) at the middle

grades: list[int] = []

while len(grades) < 10:
    grade_str = input('grade?')
    while not grade.isdigit():
        grade_str = input('grade?')
    grade = int(grade_str)  # work 100%

    if grade < 0 or grade > 100:
        print('not in range...')
        continue

    grades.append(grade)

# better - but longer
# for i in range(1, len(grades)):
#     if grades[i] > _max:
#         _max = grades[i]

_max = grades[0]
for grade in grades:
    if grade > _max:
        _max = grade

_min = grades[0]
for grade in grades:
    if grade < _min:
        _min = grade

_sum = 0
for grade in grades:
    _sum += grade

_avg = _sum / len(grades)
print(f"avg is {_avg:.2f}")

#   remove the last grade (hint: use pop)
grades.pop(-1)
grades.pop(len(grades) - 1)  # same

#   find the minimum grade (use for loop) and remove it from the list  (hint: remove)
grades.remove(_min)

#   find the maximum grade (use for loop) and add another max grade at the: (1) end of the list (2) at the middle
grades.insert(len(grades) // 2, _max)
grades.append(_max)