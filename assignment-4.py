# 1. List: Create a list of numbers from 1 to 10 and print only the even numbers
numbers = list(range(1, 11))
even_numbers = [n for n in numbers if n % 2 == 0]
print("Even numbers:", even_numbers)


# 2. Tuple: Given t = (3, 5, 7, 3), count how many times 3 appears
t = (3, 5, 7, 3)
print("Count of 3:", t.count(3))


# 3. Set: Find the common elements between {1,2,3,4} and {3,4,5,6}
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
print("Common elements:", set1 & set2)


# 4. For Loop: Print all numbers from 1 to 20 that are divisible by 3
print("Numbers divisible by 3:")
for n in range(1, 21):
    if n % 3 == 0:
        print(n, end=" ")
print()


# 5. Dictionary: Create a dictionary of 3 students with their marks, then print the student with the highest mark
students = {"Ali": 85, "Sara": 92, "John": 78}
top_student = max(students, key=students.get)
print("Top student:", top_student, "with marks:", students[top_student])


# 7. List & Function: Function that doubles all elements in a list
def double_list(lst):
    return [x * 2 for x in lst]

print("Doubled list:", double_list([1, 2, 3, 4]))


# 8. Dictionary & Loop: Print keys with even values
data = {'a': 1, 'b': 2, 'c': 3}
print("Keys with even values:")
for k, v in data.items():
    if v % 2 == 0:
        print(k)


# 9. Set & Function: Function that returns a set of unique elements
def unique_elements(lst):
    return set(lst)

print("Unique elements:", unique_elements([1, 2, 2, 3, 4, 4, 5]))


# 10. Combined Challenge: Print names of people older than 21
people = [{'name': 'Ali', 'age': 20}, {'name': 'Sara', 'age': 25}]
print("People older than 21:")
for person in people:
    if person['age'] > 21:
        print(person['name'])
