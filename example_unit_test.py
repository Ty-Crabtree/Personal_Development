import pytest


@pytest.mark.parametrize('name', ["Ty", "Max"])
def test_print_hi(name):
    """
    This is an example python unit test.
    Make sure the function starts with 'test_'

    :param name: test string
    :return: None
    """
    assert print_hi(name) == 'Hi, {n}'.format(n=name)
    assert type(name) is str



def print_hi(name):
    """
    Example function

    :param name: test string
    :return: string output
    """
    output = 'Hi, {n}'.format(n=name)
    print('Hi, {n}'.format(n=name))
    return output


@pytest.mark.parametrize('name', ["Ty", "Max", "Ty & Max are Python developers"])
def test_print_hi(name):
    """
    This is an example python unit test.
    Make sure the function starts with 'test_'

    :param name: string
    :return: None
    """
    assert print_hi(name) == 'Hi, {n}'.format(n=name)
    assert type(name) is str


@pytest.mark.parametrize('num', [10, -1, 0])
def test_simple_math(num):
    """
    Tests simple_math function
    Gives a variety of ints (positve, 0, negative) to test function

    :param num: int
    :return: None
    """
    assert simple_math(num) + simple_math(num) == num + num + 4
    assert type(num) is int

def simple_math(num):
    """
    Simple arithmetic function

    :param num: int
    :return: int
    """
    return num + 2

if __name__ == '__main__':
    print_hi('example string!')
