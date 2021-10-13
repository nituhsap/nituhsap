import sys

if __name__ == "__main__":
    i = 0
    a = []
    for param in sys.argv:
        i += 1
        a.append(param)

def evens(a):
    x = 0
    for i in a:
        if int(i) == True:
            if i % 2 == 0:
                x += 1
    print(x)

evens(a)