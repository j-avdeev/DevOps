""" example for GitHub Actions with Sphinx """

# input value raised to the power of 2.5
def make_w(a : int)->int:
    """
    Does a calculation with 'a' 

    :param a: represnts 'w'
    :type a: int
    :return: a result based on 'a
    :rtype: int
    :raises: Value error if parameter entered is not int
    """
    try:
        return a**2.5
    except ValueError:
        print("require type int.  Try again...")

