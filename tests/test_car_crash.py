from desdeo_problem.testproblems.CarCrash import car_crash_problem
from desdeo_problem.problem import MOProblem
import pytest
import numpy as np
import numpy.testing as npt

def test_number_of_variables():
    p: MOProblem = car_crash_problem()

    assert p.n_of_variables == 5

def test_number_of_objectives():
    p: MOProblem = car_crash_problem()

    assert p.n_of_objectives == 3

def test_car_crash():
    p: MOProblem = car_crash_problem()

    # evaluate the problem with some variable values
    xs = np.array([2, 2, 2, 2, 2])

    objective_vectors = p.evaluate(xs).objectives

    assert objective_vectors.shape[0] == 1

    expected_result = np.array([[1683.133345, 9.6266, 0.1233]])

    npt.assert_allclose(objective_vectors, expected_result)

def test_car_bounds_error():
    with pytest.raises(ValueError):
        p: MOProblem = car_crash_problem(var_iv=([0, 0, 0.9, 4, 4]))
