# Q1. You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.

str = "My name is Umesh Nepal"
print(str.swapcase())


# Q2. The user enters a string and a substring. You have to print the number of times that the substring occurs in the given string. String traversal will take place from left to right, not from right to left.

string = input("Enter a string \n")
substring = input("Enter a substring\n")

repeat = 0
for i in range(0, len(string) - len(substring)+1):
    if string[i:i+len(substring)] == substring:
        repeat += 1

print (repeat)

#Q3. You are given a string and your task is remove all Upper case letters.

word='My name is Umesh Nepal'
for i in word:
    if not i.isupper():
        print(i,end="")
        
        
#Q4. Write a class in which its one method accepts a string from console and another method to print the characters that have odd indexes.
class PrintOdd:
    def __init__(self):
        self.word= "" 
        
    def input_value(self):
        self.word = input("Enter a string :\n")
        
    def output_value(self):
        result=self.word[1::2]
        print(result)

po=PrintOdd()
po.input_value()
po.output_value()

#Q5. Write a Python program to replace last value of tuples in a list
li = [(10, 20, 30), (30, 40, 50), (50, 60, 70)]
print([i[0:-1] + (100,) for i in li])