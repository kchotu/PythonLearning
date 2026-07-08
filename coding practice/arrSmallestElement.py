numbers = [5,3,2,0]

smallest = numbers[0]

for num in numbers:
    if num < smallest:
        smallest = num

print(smallest)