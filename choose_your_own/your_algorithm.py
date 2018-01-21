#!/usr/bin/python

import matplotlib.pyplot as plt
from prep_terrain_data import makeTerrainData
from class_vis import prettyPicture

features_train, labels_train, features_test, labels_test = makeTerrainData()


### the training data (features_train, labels_train) have both "fast" and "slow"
### points mixed together--separate them so we can give them different colors
### in the scatterplot and identify them visually
grade_fast = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==0]
bumpy_fast = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==0]
grade_slow = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==1]
bumpy_slow = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==1]


#### initial visualization
plt.xlim(0.0, 1.0)
plt.ylim(0.0, 1.0)
plt.scatter(bumpy_fast, grade_fast, color = "b", label="fast")
plt.scatter(grade_slow, bumpy_slow, color = "r", label="slow")
plt.legend()
plt.xlabel("bumpiness")
plt.ylabel("grade")
plt.show()
################################################################################


### your code here!  name your classifier object clf if you want the 
### visualization code (prettyPicture) to show you the decision boundary
#Naive Bayes
from sklearn.naive_bayes import GaussianNB
clf1 = GaussianNB()

clf1.fit(features_train,labels_train)

pred = clf1.predict(features_test)
from sklearn.metrics import accuracy_score
accuracy = accuracy_score(pred,labels_test)
print "Accuracy of Naive Bayes",accuracy

#SVM
from sklearn import svm
clf2 = svm.SVC(C=10000.0,kernel="rbf")
clf2.fit(features_train,labels_train)
pred= clf2.predict(features_test)
from sklearn.metrics import accuracy_score
accuracy = accuracy_score(pred,labels_test)
print "Accuracy of SVM:",accuracy

#Decision Tree Classifier
from sklearn import tree
print len(features_train[0]) #gives the number of features used to train
clf3 = tree.DecisionTreeClassifier(min_samples_split=40,max_depth=5)
clf3.fit(features_train,labels_train)
pred= clf3.predict(features_test)

from sklearn.metrics import accuracy_score
acc = accuracy_score(pred,labels_test)
print "Accuracy of Decision tree:",acc


#K Nearest Neighbours
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier
clf4= KNeighborsClassifier(n_neighbors=7,algorithm='kd_tree')
clf4.fit(features_train,labels_train)
pred = clf4.predict(features_test)
#accuracy
acc= accuracy_score(pred,labels_test)
print "Accuracy of KNN Algo: ",acc

#Adaboost
from sklearn.ensemble import AdaBoostClassifier
clf5 = AdaBoostClassifier(n_estimators=80)
clf5.fit(features_train,labels_train)
pred = clf5.predict(features_test)
#accuracy
acc= accuracy_score(pred,labels_test)
print "Accuracy of AdaBoost Algo: ",acc

#Random FOrest
from sklearn.ensemble import RandomForestClassifier
clf6 = RandomForestClassifier(n_estimators = 30,max_features='log2')
clf6.fit(features_train,labels_train)
pred = clf6.predict(features_test)
#accuracy
acc= accuracy_score(pred,labels_test)
print "Accuracy of Random Forest Algo: ",acc

#Ensemble of all classifiers
from sklearn.ensemble import VotingClassifier
estimators = []
estimators.append(('NVB', clf1))
estimators.append(('SVM', clf2))
estimators.append(('DT', clf3))
estimators.append(('KNN', clf4))
estimators.append(('AdaBoost', clf5))
estimators.append(('RandomForest', clf6))

# create the ensemble model
ensemble = VotingClassifier(estimators)
ensemble = ensemble.fit(features_train,labels_train)
pr =ensemble.predict(features_test)
acc = accuracy_score(pr,labels_test)
print "Accuracy of the ensemble model built:",acc

#OUTPUT GOT
##Accuracy of Naive Bayes 0.884
##Accuracy of SVM: 0.932
##Accuracy of Decision tree: 0.912
##Accuracy of KNN Algo:  0.936
##Accuracy of AdaBoost Algo:  0.924
##Accuracy of Random Forest Algo:  0.912

try:
    prettyPicture(clf, features_test, labels_test)
except NameError:
    pass
