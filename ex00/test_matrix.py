from matrix import Matrix


def test_input():
    m1 = Matrix([[0.0, 1.0], [2.0, 3.0], [4.0, 5.0]])
    assert m1.shape == (3, 2)
    assert m1.T() == "Matrix([[0., 2., 4.], [1., 3., 5.]])"
    