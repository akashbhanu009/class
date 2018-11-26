class car:

    def __init__(self):
        self.name="lenovo"
        self.e=self.engine() #make an reference variable of class engine (child) into parent (class car)

    def model(self):
        print("Car name=> ",self.name)

    class engine:
        def __init__(self):
            self.Engine="1000CC"
        def CarEngine(self):
            print("Engine have=> ",self.Engine)

c=car()
c.model()
x=c.e
x.CarEngine()