def count():
    fs = []
    for i in range(1, 4):
        def f(i):
            return i*i
        fs.append(f(i))
    return fs

if __name__ == '__main__':
    f1 = count()
    print(f1[0],f1[1])
