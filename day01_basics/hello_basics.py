name = "demon slayer"
releasedData = 47
ratings = 65.5
earnedProfit = 98756.85


print(name)
print(type(releasedData), name)


def reverse_string(reverseString):

    reversedString = ""

    for i in range(len(reverseString) - 1, -1, -1):
        print(reverseString[i])
        reversedString = reversedString + reverseString[i]
       
    return
   

reverse_string(name)


def check_number(num):
    if num > 0:
        return "number is greater then Zero"
    elif num < 0:
        return "Number is less then zero"
    else:
        return "Zero"


# Test cases:
check_number(10)
check_number(-5)
check_number(0)
