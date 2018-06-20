#Manual delete the 1 data from each i.e divide the data

#!/usr/bin/python3
#import sklearn to access data for iris flower
from sklearn.datasets import load_iris

#to use decision algorithm import tree
from sklearn import tree

#numpy is imported to divide the data
import numpy 

#loading all data
iris=load_iris()

#range for all 3 categories in iris
X=[0,50,100]

#training target i.e removing exactly one data from each flower
train_data=numpy.delete(iris.data,X,axis=0)

#removing same from target
train_target=numpy.delete(iris.target,X) 

#testing target
test_data=iris.data[X]
test_target=iris.target[X]
print(test_target)
print(test_data)

#calling classifier
clf=tree.DecisionTreeClassifier()

#train data
trained=clf.fit(train_data,train_target)

#testing phase
output=trained.predict(test_data)

#printing output
print(output)
