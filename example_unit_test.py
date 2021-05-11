# This is a sample Python script.
import pytest

@pytest.mark.parametrize('name', ["Ty", "Max"])
def test_print_hi(name):
    assert 'Hi, ' + str(name)

def print_hi(name):
    print('Hi, {n}'.format(n=name))  # Press ⌘F8 to toggle the breakpoint.

if __name__ == '__main__':
    print_hi('hello wolrd!')
