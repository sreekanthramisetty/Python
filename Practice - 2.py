class Ide_E:
    def execute(self):
        print("Compling")
        print("Executing")

class Laptop:
    def code(self,ide):
        ide.execute()

ide = Ide_E()
Lap1 = Laptop()
Lap1.code(ide)


