from main.py import *

## Feel free to add your own tests here.
def test_multiply():
    assert subquadratic_multiply(BinaryNumber(2), BinaryNumber(2)) == 2*2
    assert subquadratic_multiply(BinaryNumber(0), BinaryNumber(98531)) == 0
    assert subquadratic_multiply(BinaryNumber(493293), BinaryNumber(0)) == 0
    assert subquadratic_multiply(BinaryNumber(3), BinaryNumber(4)) == 3*4
    assert subquadratic_multiply(BinaryNumber(1), BinaryNumber(16)) == 1*16