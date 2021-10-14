import sys
import argparse

if __name__ == "__main__":
    N = sys.argv

M = {0: 0, 1: 1}

def fib(n):
    if n in M:
        return M[n]
    M[n] = fib(n - 1) + fib(n - 2)
    return M[n]

def createParser ():
    parser = argparse.ArgumentParser()
    parser.add_argument ('N', type = int)

    return parser


if __name__ == '__main__':
    parser = createParser()
    namespace = parser.parse_args()
    print (fib(namespace.N))

fib(N)
