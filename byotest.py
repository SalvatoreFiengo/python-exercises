def test_are_equal(a,b):
    """
    Test that two values are equal. Raises AssertionError if both values
    are not equal.
    `a` is the actual value produced
    `b` is the value that was supposed to be produced
    """
    assert b==a, "Expected {0}, got {1}".format(a,b)

def test_are_not_equal(a,b):
    """
    Test that two values are not equal. Raises AssertionError if both values
    are not equal.
    `a` is the actual value produced
    `b` is the value that was supposed to be produced
    """
    assert b!=a, "expected {0} to be not equal to {1}".format(a,b)

def test_is_in(collection, item):
    """
    Test if item is in collection. Raises AssertionError if item is not in collection
    """
    assert item in collection, "{1} not in collection {0}".format(collection, item)

def test_is_not_in(collection, item):
    """
    Test if item is not in collection. Raises AssertionError if item is in collection
    """
    assert item not in collection, "{1} is in collection {0}".format(collection, item)

def test_is_in_between(upper,lower,actual):
    """
    Test if actual is between upper value and lower. 
    Raises AssertionError if actual is not in between upper and lower values 
    """

    assert upper<=actual<=lower, "{2} is not between {0} and {1}".format(upper,lower,actual)

# Test to fail the `test_are_equal` function
# test_are_equal(3,2)

# Test to fail the `test_not_equal` function
# test_are_not_equal(0, 0)

# Test to fail the `test_is_in` function
# test_is_in([1], 2)

# Test to fail the `test_not_in` function
# test_is_not_in([1], 1)

# Test to fail the `test_between` function
# test_is_in_between(10, 1, 200)