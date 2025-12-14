class Add:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def compute(self):
        return self.a + self.b
    
    def display(self):
        print(f"Adding {self.a} and {self.b}")
        result = self.compute()
        print(f"Result: {result}")

if __name__ == "__main__":
    adder = Add(5, 7)
    adder.display()
    print("add two variables")
