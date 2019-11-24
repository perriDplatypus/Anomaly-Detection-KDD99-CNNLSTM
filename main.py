import pandas as pd
import numpy as np
import pickle as p
from sklearn import metrics
from sklearn.preprocessing import Normalizer
from keras.models import Sequential
from keras.layers import Convolution1D, Dense, Dropout, MaxPooling1D, LSTM

x = pd.read_csv('/home/abhay/Major Project/Datasets/test_data.csv')
y = pd.read_csv('/home/abhay/Major Project/Datasets/test_label.csv')

lstm_output_size = 70
with open("/home/abhay/Major Project/Pickle/knn.pkl", "rb")as f:
    knn = p.load(f)
with open("/home/abhay/Major Project/Pickle/RF.pkl", "rb")as f:
    rf = p.load(f)
with open("/home/abhay/Major Project/Pickle/NB.pkl", "rb")as f:
    nb = p.load(f)
with open("/home/abhay/Major Project/Pickle/SGD.pkl", "rb")as f:
    sgd = p.load(f)

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
cnn.load_weights("/home/abhay/Major Project/HDF5/checkpoint-09.hdf5")
cnn.compile(loss="sparse_categorical_crossentropy", optimizer="SGD",
            metrics=['accuracy'])
print("Created models and loaded weights from file")

scaler = Normalizer().fit(x)
X = scaler.transform(x)
y_test = np.array(y)
X = np.array(X)
X_test = np.reshape(X, (X.shape[0], X.shape[1], 1))

y_knn = knn.predict(x)
print("KNN Done")

y_rf = rf.predict(x)
print("RF Done")

y_cnn = cnn.predict_classes(X_test)
print("CNN Done")

pred = np.empty([y_knn.size, 1], dtype=int)
a = 0

for i in y_knn:
    if i == y_cnn[a]:
        pred[a] = i
    else:
        pred[a] = y_rf[a]
    a += 1

print("Accuracy =", metrics.accuracy_score(y, pred))
print("Confusion Matrix =\n", metrics.confusion_matrix(y, pred))
print("Classification Report =\n", metrics.classification_report(y, pred))
