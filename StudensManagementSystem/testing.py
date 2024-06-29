class Test:

    def __int__(self, name):
        self.name = name

    def __str__(self):
        return f'string of class {self.name}'




test = Test()
test.name = "ivan"
print(test)