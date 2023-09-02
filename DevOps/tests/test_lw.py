"""
test lw multiply function
"""

import pytest
from lw import multiply


# Run the actual multiply test
def test_multiply_success():
    """
    Verify 2 * 3 equals 6
    """
    assert multiply(2, 3) == 6

# Check for text input
def test_multiply_value_err():
    """
    Verify string input fails
    """
    with pytest.raises(TypeError):
        multiply("two", "three")
