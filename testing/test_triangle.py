from triangle import triangle
import pytest

def test_triangle_3():
    length = 3
    result = triangle(length)
    assert result == " #\n###\n"