import sys

if __name__ == "__main__":
    i = 0
    a = []
    for param in sys.argv:
        i += 1
        a.append(param)

    print(i)
    for param in a:
        print(param)