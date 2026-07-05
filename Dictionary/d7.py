student = {
    "name": "Ravi",
    "age": 22,
    "course": "Python"
}

print("Original Dictionary:")
print(student)

# Add
student["city"] = "Ranchi"

# Update
student["age"] = 23

# Access
print("Name:", student["name"])

# Loop
print("\nDictionary Items:")
for key, value in student.items():
    print(key, ":", value)

# Remove
student.pop("course")

print("\nFinal Dictionary:")
print(student)