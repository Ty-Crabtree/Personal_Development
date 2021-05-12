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


def print_hi(name):
    """
    Example function
    :param name: test string
    :return: string output
    """
    output = 'Hi, {n}'.format(n=name)
    print('Hi, {n}'.format(n=name))
    return output


if __name__ == '__main__':
    print_hi('hello world!')
