#!/usr/bin/python


"""
    Starter code for the evaluation mini-project.
    Start by copying your trained/tested POI identifier from
    that which you built in the validation mini-project.

    This is the second step toward building your POI identifier!

    Start by loading/formatting the data...
"""

import pickle
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "r") )

### add more features to features_list!
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list)
labels, features = targetFeatureSplit(data)



### your code goes here 

from sklearn.model_selection import train_test_split
features_train,features_test,labels_train,labels_test = train_test_split(features,labels,test_size=0.3,random_state=42)

from sklearn import tree
clf = tree.DecisionTreeClassifier()
clf.fit(features_train,labels_train)
pred= clf.predict(features_test)

from sklearn.metrics import accuracy_score
acc = accuracy_score(pred,labels_test)
print acc

#NUmber of POIs predicted in test set
count = sum(1 for x in pred if x==1  )
print count
#OUTPUT:4

#number of people in test set
print len(pred)
#OUTPUT:29

#Number of true positives
truepos = sum(1 for i in range(0,len(pred)) if pred[i]==1 and labels_test[i]==1)
print truepos
#OUTPUT:0

#PRECISION AND RECALL
from sklearn.metrics import precision_score,recall_score
print precision_score(labels_test, pred)#, average='macro')
print recall_score(labels_test, pred)
