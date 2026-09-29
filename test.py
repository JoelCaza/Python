print("Hello, World!")

def inc(x):
    return x + 1

def sumar(a, b):
    return a + b

def test_inc():
    assert inc(3) == 5
    assert inc(-1) == 0
    assert inc(0) == 1
    assert sumar(2, 3) == 4