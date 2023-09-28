class Calculator:

    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
    def add(self):
        return num1 + num2
    def subtract(self):
        return num1 - num2
    def multiply(self):
        return num1 * num2
    def divide(self):
        return num1/num2
num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
obj=Calculator(num1,num2)
print(obj.add())
print(obj.subtract())
print(obj.multiply())
print(obj.divide())