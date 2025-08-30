class myClass:
    __privateVar = 27
    def __privMeth(self):
        print("I'm inide class myClass")
    def hello(self):
        print("Privet Variable value: ",myClass.__privateVar)
foo = myClass()
foo.hello()
foo.__priMeth