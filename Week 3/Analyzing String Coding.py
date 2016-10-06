str1 = input("Please input a string: ")
str2 = input("Please input another string: ")

if str1.isdigit() and str2.isdigit():
    average = (int(str1) + int(str2)) / 2
    print("The average of teh two numvers is", average)
elif not str1.isdigit() and not str2.isdigit():
    if str2 in str1:
        count = str1.count(str2)
        print("The second string occurs in the first", count, "times")
