student = {
    "name": "Ravi",
    "age": 22,
    "course": "Python"
}

#Print Keys
for key in student:
    print(key)

# Print Values
for value in student.values():
    print(value)

    #f you want to print both keys and values


for key, value in student.items():
    print(key, ":", value)    