import nose

import bdot
import bcolz
import numpy as np
from numpy.testing import assert_array_equal

def test_dot_int64():


	matrix = np.random.random_integers(0, 12000, size=(10000, 100))
	bcarray = bdot.carray(matrix, chunklen=2**13, cparams=bcolz.cparams(clevel=2))

	v = bcarray[0]

	result = bcarray.dot(v)
	expected = matrix.dot(v)

	assert_array_equal(expected, result)

def test_dot_int32():


	matrix = np.random.random_integers(0, 12000, size=(10000, 100)).astype('int32')
	bcarray = bdot.carray(matrix, chunklen=2**13, cparams=bcolz.cparams(clevel=2))

	v = bcarray[0]

	result = bcarray.dot(v)
	expected = matrix.dot(v)

	assert_array_equal(expected, result)

def test_dot_float64():


	matrix = np.random.random_sample(size=(10000, 100))
	bcarray = bdot.carray(matrix, chunklen=2**13, cparams=bcolz.cparams(clevel=2))

	v = bcarray[0]

	result = bcarray.dot(v)
	expected = matrix.dot(v)

	assert_array_equal(expected, result)


def test_dot_float32():


	matrix = np.random.random_sample(size=(10000, 100)).astype('float32')
	bcarray = bdot.carray(matrix, chunklen=2**13, cparams=bcolz.cparams(clevel=2))

	v = bcarray[0]

	result = bcarray.dot(v)
	expected = matrix.dot(v)

	assert_array_equal(expected, result)