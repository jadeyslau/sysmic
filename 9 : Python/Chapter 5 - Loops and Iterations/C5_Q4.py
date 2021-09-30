numbers = [7, 16, 0.3, 0, 15, -4, 5, 3, 15]

mean = sum(numbers)/len(numbers)
top  = []
for n in numbers:
    val = (n - mean)**2
    top.append(val)

variance = sum(top)/len(numbers)

print("Mean: ",mean)
print("Variance: ", variance)
