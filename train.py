'''
Created on 2015/05/25

@author: kagaminaoto

@summary: the toy program to practice pylearn2 with the iris dataset(in sklearn.datasets)
'''

import os
from pylearn2.config import yaml_parse
from sklearn.datasets import load_iris
import random

'''
@summary: make csv files from data
'''
def data2csv(labels,data,trainCsvPath,testCsvPath,trainsNum):
    lines = []
    for d, t in zip(labels,data):
        l = ""
        l += str(d) + ","
        l += " ".join([str(e) for e in t]) + os.linesep
        lines.append(l)
        
    random.shuffle(lines)
            
    ftr = open(trainCsvPath, "w")
    ftr.writelines(lines[:trainsNum])
    ftr.close()
    
    fts = open(testCsvPath, "w")
    fts.writelines(lines[trainsNum:])
    fts.close()
    

if __name__ == "__main__":
    files = ["test.X.npy","test.Y.npy","train.X.npy","train.Y.npy"]
    for f in files:
        if os.path.exists(f):
            os.remove(f)
    
    data = load_iris()
    data2csv(data['target'],data['data'],"train.csv","test.csv",90)
            
    train = open("mlp_practice.yaml","r").read()
    hyper_params = {'train_stop' : 72,
                    'valid_stop' : 89,
                    'dim_h0' : 3,
                    'max_epochs' : 100,
                    'save_path' : '.'}

    train = train % (hyper_params)
    train = yaml_parse.load(train)
    train.main_loop()
    
    print("")
    print("----------")
    print("train finished")