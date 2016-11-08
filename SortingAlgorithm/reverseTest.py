import sys

tempString = input("Input the string you want to reverse: ")
try:
    i = int(input("input the what number do you wanna to begin reverse: "))
except (TypeError, ValueError):
    sys.exit("You must input a integer for i")

if len(tempString) < i:
    i = len(tempString)


print((tempString[i - 1::-1] + tempString[len(tempString):i - 1:-1])[::-1])