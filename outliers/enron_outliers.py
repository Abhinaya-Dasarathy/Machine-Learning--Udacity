#!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit


### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )

features = ["salary", "bonus"]


# So there is a outlier in the data : KEY name -> TOTAL : Spreadsheet quirk
print data_dict["TOTAL"] 
#Remove this outlier from the dictionary
data_dict.pop("TOTAL",0)
data = featureFormat(data_dict, features)

### your code below

#Abhi notes
#FOUND TWO MORE OUTLIERS WITH HUGE SALARY AS WELL AS BONUS
# BUT NOT TAKING THEM OUT AS THEY ARE ENRON BOSSES AND DEFINITELY POIs FOR US

for point in data:
    salary = point[0]
    bonus = point[1]
    matplotlib.pyplot.scatter(salary,bonus)

matplotlib.pyplot.xlabel("Salary")
matplotlib.pyplot.ylabel("Bonus")
matplotlib.pyplot.show()
