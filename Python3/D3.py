import sys
import argparse

def fib(n, p = True):
    fibs = []
    x, y = 1, 1
    for i in range(n):
        z = x+y
        x = y
        y = z
        fibs.append(str(x))
    if p == True:
        return ' '.join(fibs)
    else:
        return x
    return M[n]

def createParser():
    parser = argparse.ArgumentParser()
    parser.add_argument ('N', type = int)
    parser.add_argument('-a', '--all', action='store_const', const=True)
    return parser

if __name__ == '__main__':
    parser = createParser()
    namespace = parser.parse_args()
    print (fib(namespace.N, True))
