import pickle
import numpy as np
from practice_dataset import PracticeDataset
import theano
from pylearn2.utils import serial

if __name__ == "__main__":
    print 'convert: test.csv -> test.pkl'
    pyln_data = PracticeDataset(which_set='test')
    pickle.dump(pyln_data, open('test.pkl', 'w'))
    test = pickle.load(open('test.pkl'))
    
    model = serial.load("mlp_best.pkl")
    
    inputs = test.X.astype("float32")
    yhat = model.fprop(theano.shared(inputs,name='inputs')).eval()
    
    print 'testing ' + str(test.X.shape[0]) + ' data'
    count = 0.
    for i in range(test.X.shape[0]):
        if np.argmax(test.y[i])==np.argmax(yhat[i]):
            count += 1.
    
    print "accuracy = ", count / test.X.shape[0]
    print "yhat : "
    print yhat