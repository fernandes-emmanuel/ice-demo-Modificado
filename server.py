import sys, Ice
import Demo

class PrinterI(Demo.Printer):
    def __init__(self):
        self.count = 0

    def printString(self, s, current=None):
        print(s)
        self.count += 1
        return s + "*"

    def printUpper(self, s, current=None):
        print(s.upper())
        self.count += 1
        return s.upper() + "*"

    def countWords(self, s, current=None):
        return len(s.split())

    def getPrintCount(self, current=None):
        return self.count

communicator = Ice.initialize(sys.argv)

adapter = communicator.createObjectAdapterWithEndpoints("SimpleAdapter", "default -p 5678")
object = PrinterI()
adapter.add(object, Ice.Identity("SimplePrinter"))
adapter.activate()

communicator.waitForShutdown()
