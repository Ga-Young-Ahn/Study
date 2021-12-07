class FourCal:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
        
    def sum(self):
        result = self.num1 + self.num2
        return result
        
    def mul(self):
        result = self.num1 * self.num2
        return result
        
    def sub(self):
        result = self.num1 - self.num2
        return result
    
    def div(self):
        result = self.num1 / self.num2
        return result
    
a = FourCal(4,2)
print(a.sum())
print(a.mul())
print(a.sub())
print(a.div())