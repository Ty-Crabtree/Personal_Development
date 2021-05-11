# This is a sample Python script.
import pytest

@pytest.mark.parametrize('name', ["Ty", "Max"])
def test_print_hi(name):
    print(name)
    assert print_hi(name) == 'Hi, {n}'.format(n=name)

def print_hi(name):
    output = 'Hi, {n}'.format(n=name)
    print('Hi, {n}'.format(n=name))
    return output

if __name__ == '__main__':
    print_hi('hello wolrd!')
