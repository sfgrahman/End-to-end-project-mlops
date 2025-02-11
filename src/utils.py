from src.logger import logging
from src.exception import CustomException
import os, sys
import pickle
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import accuracy_score, confusion_matrix, precision_score,recall_score,f1_score, classification_report

def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)
        
        with open(file_path, "wb") as file_obj:
            pickle.dump(obj, file_obj)
    except Exception as e:
        raise CustomException(e, sys)
    
    
def load_object(file_path):
    try:
        with open(file_path, "rb") as file_obj:
            return pickle.load(file_obj)
    except Exception as e:
        raise CustomException(e, sys)
    
    
def evaluate_model(X_train, y_train, X_test, y_test, models, params):
    try:
        report = {}
        for i in range(len(list(models))):
            model = list(models.values())[i]
            param = params[list(models.keys())[i]]
            grid_search = GridSearchCV(model, param, cv=5)
            grid_search.fit(X_train, y_train)
            model.set_params(**grid_search.best_params_)
            model.fit(X_train, y_train)
            
            y_pred = model.predict(X_test)
            test_model_accuracy = accuracy_score(y_test, y_pred)
            report[model] = test_model_accuracy
            return report
    except Exception as e:
        raise CustomException(e,sys)