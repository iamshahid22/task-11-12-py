# tax calculation for salary
salary = int(input("Enter ur salary:"))

if salary<=250000:
    tax = 0
elif salary<=500000:
    tax = salary*0.05
elif salary<=1000000:
    tax = salary*0.07
else:
    tax = salary*0.10
    
print(f"Salary: {salary}")
print(f"Calculated tax: {tax}")