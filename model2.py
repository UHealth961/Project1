import numpy as np
import pandas as pd
import seaborn as sns
from scipy.stats import mode
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix

DATA_PATH = "C:\\Users\\myria\\Desktop\\Datasets\\Training.csv"
data = pd.read_csv(DATA_PATH).dropna(axis = 1) #Removing empty columns

# Encoding our last column (prognosis) into numerical value
l_encoder=LabelEncoder()
data["prognosis"]=l_encoder.fit_transform(data["prognosis"])

X=data.iloc[:,:-1] #All rows and all columns except the last one (prognosis)
Y=data.iloc[:,-1] #All rows and last column

# Initializing all 3 models
models={
    "Support Vector Classifier":SVC(),
    "Gaussian Naive Bayes" : GaussianNB(),
    "Random Forest" : RandomForestClassifier(random_state=20)
}


# Training all 3 models on the whole data
final_svm_model=SVC()
final_svm_model.fit(X,Y)

final_nb_model=GaussianNB()
final_nb_model.fit(X,Y)

final_rf_model=RandomForestClassifier(random_state=20)
final_rf_model.fit(X,Y)

# Inputs: Symptoms ; Outputs: Predictions
symptoms=X.columns.values

symptom_index={}
for index, value in enumerate(symptoms):
    symptom=" ".join([i.capitalize() for i in value.split("_")])
    symptom_index[symptom]=index
    
data_dict={
    "symptom_index":symptom_index,
    "predictions_classes":l_encoder.classes_
}

def predictDisease(symptoms):
    symptoms=symptoms.split(",")
    input_data=[0]*len(data_dict["symptom_index"]) #input data for the models
    
    for symptom in symptoms:
        index=data_dict["symptom_index"][symptom]
        input_data[index]=1
        
    input_data=np.array(input_data).reshape(1,-1)
    
    svm_prediction=data_dict["predictions_classes"][final_svm_model.predict(input_data)[0]]
    nb_prediction=data_dict["predictions_classes"][final_nb_model.predict(input_data)[0]]
    rf_prediction=data_dict["predictions_classes"][final_rf_model.predict(input_data)[0]]
    
    final_prediction=mode([svm_prediction, nb_prediction, rf_prediction])[0][0]
    
    predictions=final_prediction
    
    return predictions