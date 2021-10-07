class Something(Exception):
    def __init__(self, text = "stop"):
        self.text = text
        super().__init__(self.text)

def smth():
    raise Something("Something happens")

def sqrrer(list):
    list = list**(0,5)
    return smth()

def summer(x, y, list):
    return (x + y + sqrrer(list))

print ("input list")
x, y, list = 3, 5, float(input())
summer(x, y, list)