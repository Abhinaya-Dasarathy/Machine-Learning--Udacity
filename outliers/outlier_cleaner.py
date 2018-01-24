#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    
    cleaned_data = []

    ### your code goes here
    error = (predictions-net_worths)**2
    #print len(error)
    combined_data = map(lambda x,y,z:(x,y,z),ages,net_worths,error)
    #print len(combined_data)
    sorted_data = sorted(combined_data, key=lambda x: x[2])
    #print len(sorted_data)
    cleaned_data = sorted_data[:int(len(sorted_data)*0.9)]
    #print len(cleaned_data)
    return cleaned_data

