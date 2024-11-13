from flask import Flask,render_template,request 

from utils import TitanicSurvival

app = Flask(__name__)

@app.route('/')
def hello_flask():
    print('Titanic Survival Prediction..')
    return render_template('index.html')

@app.route('/predict_survival',methods=['POST','GET'])
def survival_info():
    
    if request.method == 'GET':
        print('In GET Method...')
        
        # data = request.form 
        # Pclass = eval(data['Pclass'])
        # Gender = data['Gender']
        # Age = eval(data['Age'])
        # SibSp = eval(data['SibSp'])
        # Parch = eval(data['Parch'])
        # Fare = eval(data['Fare'])
        # Embarked = data['Embarked']
        
        # return f'Passenger is not Survived...'
        
        Pclass = eval(request.args.get('Pclass'))
        Gender = request.args.get('Gender')
        Age = eval(request.args.get('Age'))
        SibSp = eval(request.args.get('SibSp'))
        Parch = eval(request.args.get('Parch'))
        Fare = eval(request.args.get('Fare'))
        Embarked = request.args.get('Embarked')
        
        survival = TitanicSurvival(Pclass,Gender,Age,SibSp,Parch,Fare,Embarked)
        
        predict = survival.get_predicted_survival()
        
        if predict == 0:
            
            predict = 'Not Survived...'
            
        else :
            
            predict = 'Survived...'
            
        return render_template('index.html',prediction=predict)
        
print('__name__ :',__name__)

if __name__ == '__main__':
    app.run()