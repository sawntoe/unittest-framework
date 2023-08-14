class UnitTest:
    def __init__(self) -> None:
        self.registry = []
    
    def register(self, func):
        self.registry.append(func)
        return func
    def run(self):
        for x in self.registry:
            x()
    
ut = UnitTest()

@ut.register
def test():
    print("hello")

ut.run()