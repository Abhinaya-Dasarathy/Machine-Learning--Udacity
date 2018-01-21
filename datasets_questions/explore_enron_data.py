#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

#find number of people in data set -data points
print len(enron_data) 
#OUTPUT:146

#find the number of features associated with each person
print (dict.values())
#OUTPUT: 21

#find the POI's
print sum(enron_data[each]["poi"] ==1 for each in enron_data)
#OUTPUT: 18

#Number of POIs in poi_names.txt = 35

#total stock value of James Prentice -1095040
print enron_data["PRENTICE JAMES"]["total_stock_value"]
