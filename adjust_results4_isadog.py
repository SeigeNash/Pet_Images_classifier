#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/adjust_results4_isadog.py
#                                                                             
# PROGRAMMER: 
# DATE CREATED:                                 
# REVISED DATE: 
# PURPOSE: Create a function adjust_results4_isadog that adjusts the results 
#          dictionary to indicate whether or not the pet image label is of-a-dog, 
#          and to indicate whether or not the classifier image label is of-a-dog.
#          All dog labels from both the pet images and the classifier function
#          will be found in the dognames.txt file. We recommend reading all the
#          dog names in dognames.txt into a dictionary where the 'key' is the 
#          dog name (from dognames.txt) and the 'value' is one. If a label is 
#          found to exist within this dictionary of dog names then the label 
#          is of-a-dog, otherwise the label isn't of a dog. Alternatively one 
#          could also read all the dog names into a list and then if the label
#          is found to exist within this list - the label is of-a-dog, otherwise
#          the label isn't of a dog. 
#         This function inputs:
#            -The results dictionary as results_dic within adjust_results4_isadog 
#             function and results for the function call within main.
#            -The text file with dog names as dogfile within adjust_results4_isadog
#             function and in_arg.dogfile for the function call within main. 
#           This function uses the extend function to add items to the list 
#           that's the 'value' of the results dictionary. You will be adding the
#           whether or not the pet image label is of-a-dog as the item at index
#           3 of the list and whether or not the classifier label is of-a-dog as
#           the item at index 4 of the list. Note we recommend setting the values
#           at indices 3 & 4 to 1 when the label is of-a-dog and to 0 when the 
#           label isn't a dog.
#
##
def adjust_results4_isadog(results_dic, dogfile):
    """
    Adjusts the results dictionary to determine if classifier correctly 
    classified images 'as a dog' or 'not a dog' especially when not a match. 
    Demonstrates if model architecture correctly classifies dog images even if
    it gets dog breed wrong (not a match).
    Parameters:
      results_dic - Dictionary with 'key' as image filename and 'value' as a 
                    List. Where the list will contain the following items: 
                  index 0 = pet image label (string)
                  index 1 = classifier label (string)
                  index 2 = 1/0 (int)  where 1 = match between pet image
                    and classifer labels and 0 = no match between labels
                ------ where index 3 & index 4 are added by this function -----
                 NEW - index 3 = 1/0 (int)  where 1 = pet image 'is-a' dog and 
                            0 = pet Image 'is-NOT-a' dog. 
                 NEW - index 4 = 1/0 (int)  where 1 = Classifier classifies image 
                            'as-a' dog and 0 = Classifier classifies image  
                            'as-NOT-a' dog.
     dogfile - A text file that contains names of all dogs from the classifier
               function and dog names from the pet image files. This file has 
               one dog name per line dog names are all in lowercase with 
               spaces separating the distinct words of the dog name. Dog names
               from the classifier function can be a string of dog names separated
               by commas when a particular breed of dog has multiple dog names 
               associated with that breed (ex. maltese dog, maltese terrier, 
               maltese) (string - indicates text file's filename)
    Returns:
           None - results_dic is mutable data type so no return needed.
    """
    
    # reading the file, despite having the file as input in this function
    # all the dog names have been put inside a list 
    
    f = open(dogfile,"r")
    dog_name_list = f.readlines()
    for i in range(len(dog_name_list)):
        dog_name_list[i] = dog_name_list[i].strip("\n")
    
    # making a list containing all the keys of the dict results_dic
    
    dic_keys = list(results_dic.keys())

    # accessing all the elements of the dictionary through the keys
    # appendoing 0/1 in each list
    
    for i in dic_keys:
        
        ''' checking for pet label if pet label is in dog_name_list, then 1 is appended, else 0 '''
        if results_dic[i][0] in dog_name_list:
            results_dic[i].append(1)
        else:
            results_dic[i].append(0)
        
        # classifier labels are strings containing multiple classifier names. 
        # all the names in a single classifier stirng have to be dog names
        # that is the only condition for appending 1 at index 4
        # to verify that i made a counter, and a list containg all the words in a single classifier
        # if the counter's value == len(list_containing_names), then i append 1 in list 
        
        ''' checking for classifier label if classifier label is in dog_name_list, then 1 is appended, else 0 '''
        '''
        classifier_split = results_dic[i][1].split(",")     # classifier_split is a list containging all names
        count = 0

        for j in classifier_split:
            if j in dog_name_list:
                count += 1
            else:
                continue

        if count == len(classifier_split):
            results_dic[i].append(1)
        else:
            results_dic[i].append(0)
        '''
        
        if results_dic[i][1] in dog_name_list:
            results_dic[i].append(1)
        else:
            results_dic[i].append(0)
        