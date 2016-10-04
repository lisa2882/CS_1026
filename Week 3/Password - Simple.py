firstName = input("Please input your first name: ")
lastName = input("Please input your last name: ")
age = int(input("Please input your age: "))
yearOfBirth = str(2016 - age)

password = firstName[len(firstName) - 1] + yearOfBirth + lastName[0].upper()
print("I share with you ... your password: ", password)
