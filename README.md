# Anomaly-Detection-KDD99-CNNLSTM
This is a project that uses three models developed to classify incming packets on a KDD99 dataset. Three layers are used: KNN, CNN+LSTM, and a Random Forest Classifier. This project is a research based project and the model gives a minor boost in performance over using any of the given models individually.

The KDD'99 dataset is used as is and is preprocessed as a part of the projects source.

The final accuracy is 0.97833. The individual accuracy of a single model is:

KNN: 0.976835

CNN+LSTM: 0.9667878

Random Forest: 0.96381378

The main idea was to have 3 different classifier models trained on the same data. Then, we were to use all these models as a single ensemble learning model (or a voting classifier, somewhere in the middle). There are 2 main layers in the system:
- The first layer has the KNN and the CNN+LSTM. They work together and give 2 different outputs.
- The second layer has the Random Forest classifier to classify all the conflicted instances from the previous layer.
 
### Author's Note
This project was done as a capstone project for my undergrad program, so it's not the implementation, but I will link the research paper in the readme once it gets published. Hope it helps.