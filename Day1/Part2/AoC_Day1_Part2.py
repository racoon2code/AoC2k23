data = open("data.txt", "r")

result = 0

for row in data:

    list1 = []
    

    for index, sign in enumerate(row):
        if sign == "e":
            if index == row.find("eight", index):
                list1.append(8)
        if sign == "f":
            if index == row.find("four", index):
                list1.append(4)
            if index == row.find("five", index):
                list1.append(5)
        if sign == "n":
            if index == row.find("nine", index):
                list1.append(9)
        if sign == "o":
            if index == row.find("one", index):
                list1.append(1)
        if sign == "s":
            if index == row.find("seven", index):
                list1.append(7)
            if index == row.find("six", index):
                list1.append(6)
        if sign == "t":
            if index == row.find("three", index):
                list1.append(3)
            if index == row.find("two", index):
                list1.append(2)
        if sign == "1":
            list1.append(1)
        if sign == "2":
            list1.append(2)
        if sign == "3":
            list1.append(3)
        if sign == "4":
            list1.append(4)       
        if sign == "5":
            list1.append(5)
        if sign == "6":
            list1.append(6)
        if sign == "7":
            list1.append(7)
        if sign == "8":
            list1.append(8)
        if sign == "9":
            list1.append(9)
    

    number = str(list1[0]) + str(list1[-1])
         
    result += int(number)
    
    
print(result)