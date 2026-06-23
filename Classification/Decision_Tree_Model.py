# Classification - Data Mining
import pandas as pd
import numpy as np

#Load data
data_path = "data/tennis_classification.csv"
dataset = pd.read_csv(data_path)
print(dataset.to_string)

attribute_list = dataset.columns.tolist
print(attribute_list)
#Basic Tree DS
class Tree:
    def __init__(self, node):
        self.node = node
        self.children = []
        self.is_leaf = None
        self.threshold = None
        

    def addChild(self, child):
        self.children.append(child)

    def popChild(self, child):
        self.children.pop

#Decision Tree Classifier
#Helper functions
def check_same_class(dataset):
    """Checks if all tuples are same class in dataset tuples, if true, returns 
    class C, else returns false."""
    class_C = dataset[0].getClass
    for tuple in dataset:
        if tuple.getClass != class_C:
            return False
        else:
            continue
    return class_C
    
def get_maj_class(dataset):
    """Return majority class and the class frequency from dataset of tuples."""
    class_dict = dict()

    for tuple in dataset:
        if tuple.getClass not in class_dict:
            class_dict.add(tuple.getClass)
            class_dict[tuple.getClass] = 1
        else:
            class_dict[tuple.getClass] += 1

        for key, value in class_dict.items():
            max_key = ""
            max_value = -1

            if value > max_value:
                max_value = value
                max_key = key
            
        return (max_key, max_value)

#Attribute selection methods - pg.284
def information_gain(dataset):
    
    return None

def gain_ratio(dataset):
    return None

def gini_impurity(dataset):
    classes = dataset.getClasses
    impurity_d = 0


    return None

#Decision Tree Construction
def build_tree(dataset, attribute_list):
    """ Generates a decision tree provided training tuples.

    Output:
    Decision Tree

    Parameters:
    dataset (set of training tuples) 
    attribute_list (set of candidate attributes)
    attribute_heuristic (selection method for splitting criterion)"""
    # Create node n
    tree = Tree("")
    if check_same_class(dataset) != False:
        tree.node = check_same_class(dataset)
        return tree.node
    
    if attribute_list == []:
        tree.node = get_maj_class(dataset)
        return tree.node
    
    #attribute_selection_method(dataset, attribute_list)




#ID3

#C4.5

#CART

#Data
