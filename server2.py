import sys, Ice
import Demo

class PrinterI(Demo.Printer):
    def __init__(self, t):
        self.t = t
        self.count = 0

    def printString(self, s, current=None):
        print(self.t, s)
        self.count += 1
        return s + "*"

    def printUpper(self, s, current=None):
        print(self.t, s.upper())
        self.count += 1
        return s.upper() + "*"

    def countWords(self, s, current=None):
        return len(s.split())

    def getPrintCount(self, current=None):
        return self.count

communicator = Ice.initialize(sys.argv)

adapter = communicator.createObjectAdapterWithEndpoints("SimpleAdapter", "default -p 5678")
object1 = PrinterI("Object1 says:")
object2 = PrinterI("Object2 says:")
adapter.add(object1, Ice.Identity("SimplePrinter1"))
adapter.add(object2, Ice.Identity("SimplePrinter2"))
adapter.activate()

communicator.waitForShutdown()
