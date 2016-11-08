tempString = input("Input the string you want to reverse: ")
i = int(input("input the num of i: "))

print((tempString[i - 1::-1] + tempString[len(tempString):i - 1:-1])[::-1])