import sys
import argparse

def aller():
    parser = argparse.ArgumentParser()
    parser.add_argument ('-a', '--all', nargs=0)

    return parser


def filer():
    parser = argparse.ArgumentParser()
    parser.add_argument ('-a', '--all')

    return parser


if __name__ == '__main__':
    al = aller()
    fil = filer()
    ff = fil.parse_args(sys.argv[1:])
    N = sys.argv

M = {0: 0, 1: 1}

def fib(n):
    if n in M:
        return M[n]
    M[n] = fib(n - 1) + fib(n - 2)
    return M[n]

fib(N)

if ff == True:
    if al == True:
        with open(ff, "w") as out:
            for i in range(1, N):
                out.write(fib(i))
    else:
        with open(ff, "w") as out:
            out.write(fib(N))

else:
    if al == True:
        for i in range(1, N):
            print(fib(i))
    else:
        print(fib(N))