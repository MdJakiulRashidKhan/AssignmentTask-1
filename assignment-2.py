# 1. Conversion int to float
c = 60
d = 22
print("Before conversion:", c, type(c), d, type(d))

# convert int to float
c = float(c)
d = float(d)
print("After conversion:", c, type(c), d, type(d))


# 2. Create a dictionary & print your info
my_info = {
    "name": "Md Jakiul Rashid Khan",
    "age": 28,
    "email": "zakiulsoraz@gmail.com",
    "skills": ["Python", "JavaScript", "React", "SQL"]
}
print("My Info Dictionary:", my_info)


# 3. Example of if, elif, else
marks = 75

if marks >= 80:
    print("Grade: A+")
elif marks >= 60:
    print("Grade: A")
elif marks >= 40:
    print("Grade: B")
else:
    print("Grade: Fail")
