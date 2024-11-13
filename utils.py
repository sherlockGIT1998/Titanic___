import pickle 
import json 
import numpy as np
import pandas as pd
import warnings
warnings.filterwarnings('ignore')
import config 

class TitanicSurvival():
    
    def __init__(self,Pclass,Gender,Age,SibSp,Parch,Fare,Embarked):
        
        self.Pclass = Pclass
        self.Gender = Gender
        self.Age = Age
        self.SibSp = SibSp
        self.Parch = Parch
        self.Fare = Fare
        
        self.Embarked_col = 'Embarked_' + Embarked
        
    def load_models(self):
        
        with open(config.MODEL_FILE_PATH,'rb') as f:
            self.logistic_model = pickle.load(f)
            
        with open(config.JSON_FILE_PATH,'r') as f :
            self.save_data = json.load(f)
            
            self.column_names = np.array(self.save_data['column_names'])
            
    def get_predicted_survival(self):
        
        self.load_models()
        
        Embarked_col_index = np.where(self.column_names==self.Embarked_col)[0]
        
        array = np.zeros(len(self.save_data['column_names']))
        
        array[0] = self.Pclass
        array[1] = self.save_data['Gender'][self.Gender]
        array[2] = self.Age
        array[3] = self.SibSp
        array[4] = self.Parch
        array[5] = self.Fare

        array[Embarked_col_index] = 1

        print('Array is :',array)
        
        predict = self.logistic_model.predict([array])[0]
        
        return predict
    
if __name__ == '__main__':
    
    Pclass = 3.00
    Gender = 'male'
    Age = 22.00
    SibSp = 1.00
    Parch = 0.00
    Fare = 7.25

    Embarked = 'C'
    
    survival = TitanicSurvival(Pclass,Gender,Age,SibSp,Parch,Fare,Embarked)
    
    predict = survival.get_predicted_survival()
    
    if predict == 0 :
        
        print('Not Survived...')
    
    else :
        
        print('Survived...')
        
        