__author__ = 'martinrasumoff'

import h5py
import numpy

import scipy.io

data = {}

f = scipy.io.loadmat('data-starplus-04847-v7.mat')

# read in the structure
data = f['data']

# get the fields
#x = data[0,0]['x']
#y = data[0,0]['y']

print "hello"
