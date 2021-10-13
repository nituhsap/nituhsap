import sys
if __name__ == "__main__":
    a = []
    for param in sys.argv:
        a.append(param)

def mns(ls):
    dif = ls[0] - ls[1]
    print(dif)
    return dif

def invert(ls, func):
    b = (ls[-1], ls[-2])
    func(b)

invert(a, mns)