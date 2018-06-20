#!/usr/bin/python3

#import sklearn to access data for iris flower
from sklearn.datasets import load_iris

#to use decision algorithm import tree
#from sklearn import tree

#loading all data
iris=load_iris()

#printing features name
print(iris.feature_names)

#target names
print(iris.target_names)

#features data list
print(iris.data)

#target data list
print(iris.target)

#for only setosa
setosa=iris.data[0:50]
print(setosa)
#setosa data values
setosa_data=(iris.target[0:50])
print(setosa_data)
print(setosa_data.size)

