'''
Created on 2015/05/26

@author: kagaminaoto
'''

import glob
import PIL.Image as Image
import PIL.ImageOps as ImageOps
import numpy
import os
import random

def img2text(path,shape):
    im = Image.open(path)
    im = ImageOps.grayscale(im).resize(shape)
    l = (numpy.asarray(im).flatten() / 255.0).tolist()
    l = [str(e) for e in l]
    return " ".join(l)

'''
@summary: converts images to csv files for pylearn2
imgPaths : list of paths that include image files you want to convert
shape : 2D tuple that indicates the shape which you want to resize the grayscales of images to
trainCsvPath : path of csv file that includes train data
testCsvPath : path of csv file that includes test data
trainsNum : number of data you distribute to train data
'''
def img2csv(imgPaths, shape, trainCsvPath, testCsvPath, trainsNum):
    import csv
    lines = []
    for index,path in enumerate(imgPaths):
        for e in glob.glob(path):
            if os.path.isfile(e):
                print e
                l = img2text(e,shape)
                lines.append([index,l])
            
    random.shuffle(lines)
            
    ftr = open(trainCsvPath, "w")
    writerTr = csv.writer(ftr)
    for l in lines[:trainsNum]:
        writerTr.writerow(l)
    ftr.close()
    
    fts = open(testCsvPath, "w")
    writerTs = csv.writer(fts)
    for l in lines[trainsNum:]:
        writerTs.writerow(l)
    fts.close()
    
if __name__ == "__main__":
    img2csv(["dogs/*/*","cats/*/*"], (48,48), "train.csv", "test.csv", 7000)