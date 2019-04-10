from tkinter import Tk, Button, Frame
import pandas as pd
from time import sleep
import numpy as np
import pickle as p
import random
from sklearn.preprocessing import Normalizer
from keras.models import Sequential
from keras.layers import Convolution1D, Dense, Dropout, MaxPooling1D, LSTM
import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
top = Tk()

print
skip = sorted(random.sample(range(2984145),2984145-2000))
x = pd.read_csv('D:/Major Project/Datasets/data.csv', skiprows=skip)
x.sample(frac=1)

scaler = Normalizer().fit(x)
X = scaler.transform(x)
X = np.array(X)

with open("D:/Major Project/Pickle/knn.pkl", "rb")as f:
    knn = p.load(f)
with open("D:/Major Project/Pickle/RF.pkl", "rb")as f:
    rf = p.load(f)

X_test = np.reshape(X, (X.shape[0],X.shape[1],1))

lstm_output_size = 70
cnn = Sequential()
cnn.add(Convolution1D(64, 3, activation="relu", input_shape=(41, 1)))
cnn.add(Convolution1D(64, 3, activation="relu"))
cnn.add(MaxPooling1D(pool_size=2))
cnn.add(Convolution1D(128, 3, activation="relu"))
cnn.add(Convolution1D(128, 3, activation="relu"))
cnn.add(MaxPooling1D(pool_size=2))
cnn.add(LSTM(lstm_output_size))
cnn.add(Dropout(0.1))
cnn.add(Dense(5, activation="softmax"))
cnn.load_weights("D:/Major Project/HDF5/checkpoint-09.hdf5")
cnn.compile(loss="sparse_categorical_crossentropy", optimizer="SGD", 
            metrics=['accuracy'])

c = cnn.predict_classes(X_test)
k = knn.predict(x)
rf = rf.predict(x)

os.system('cls')
print("-----------------Multi Layered IDS------------------------------------")
print("This project is research based, we pass an unlabeled dataset as a")
print("datastream into the system, the values shown are the predicted classes")
print("Index\tClasses")
def pred(i):
    global c, k, rf
    if c[i] == k[i]:
        pre = k[i]
    else:
        pre = rf[i]
    return pre

def stream():
    for i in range(0,len(x)):
        p = pred(i)
        if p == 0:
            #o.insert(END, "Normal\n")
            print(i,"\tNormal")
        elif p == 1:
            #o.insert(END, "DDoS\n")
            print(i,"\tDDoS")
        elif p == 2:
            #o.insert(END, "Probe\n")
            print(i,"\tProbe")
        elif p==3:
            #o.insert(END, "R2L\n")
            print(i,"\tR2L")
        else:
            #o.insert(END, "U2R\n")
            print(i,"\tU2R")
        sleep(0.5)

f = Frame(top)
f.pack()
top.title("IDS")
w = Button(f, text="Start", width=25, fg='green', command=stream)
w.pack()
top.mainloop()
        