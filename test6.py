from DAY6 import prime

def test1():
    assert prime(12) == 13

def test2():
    assert prime(24) == 29

def test3():
    assert prime(11) == 11

if __name__ == '__main__':
    test1()
    test2()
    test3()
    print('all test passed')   