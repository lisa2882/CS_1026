salary = float(input("Enter a salary or -1 to finish: "))
count = 0
total = 0
while salary >= 0.0:
    total += salary
    count += 1
    salary = float(input("Enter a salary or -1 to finish: "))
print("Total salary cost is:", total, "for", count, "salaries.")
print("Average salary cost is:", total/count)
