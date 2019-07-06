if __name__ == '__main__':
    n = int(input())
    ar = input()
    a = list(map(int,ar.split(" ")))
    t = tuple(a)
    print(hash(t))
