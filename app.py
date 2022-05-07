from flask import Flask,render_template,request
import pickle
import json
from sklearn.preprocessing import StandardScaler
import jinja2

app=Flask(__name__)
import os
# file_=open('C:\\Users\\SIVARAM\\Desktop\\entry_machine_models\\heartdises\\srk.pkl','rb')
file_=open('srk.pkl','rb')
model=pickle.load(file_)

@app.route('/',methods=['GET'])
def home():
    return render_template('index.html')

standard_to = StandardScaler()

@app.route("/srk", methods=['GET','POST'])
def srk():
        Currentsmoker=1
        Diabetes=1
        PrevalentHyp=1

        if request.method =='POST':
                Age=request.form['age']
                Cigsperday=int(request.form['cig/day'])  
                bPMeds=float(request.form['BPMeds']) 
                PrevalentStroke=float(request.form['prevalentStroke']) 
                TotChol=float(request.form['totCholvalue'])   
                SysBP=float(request.form['sysBPvalue']) 
                DiaBP =float(request.form['diaBPvalue']) 
                bMIvalue =float(request.form['BMIvalue']) 
                HeartRate=float(request.form['heartRatevalue']) 
                Glucose =float(request.form['glucosevalue']) 
                male=request.form['gender']
                if (male=='Male'):
                  male=1
                else:
                  male=0
                  Currentsmoker=request.form['smoker']
                if (Currentsmoker=='_yes_') :
                    Currentsmoker=1
                else:
                   Currentsmoker=0 
                   PrevalentHyp=request.form['prevalentHyp']
                if (PrevalentHyp=='yes'):
                 PrevalentHyp=1
                else:
                 PrevalentHyp=0
                
                 Diabetes =request.form['diabetes__']   
                if (Diabetes=='yes'):
                      Diabetes=1
                      
                else:
                        Diabetes=0
                        Prediction_=model.predict([[male,Age,Currentsmoker,Cigsperday,bPMeds,PrevalentStroke,PrevalentHyp,Diabetes,TotChol,SysBP,DiaBP,bMIvalue,HeartRate,Glucose]])
                        Output=Prediction_[0]
                if Output == 1:
                 return render_template('index1.html',prediction_text='these person getting chances to cancer after 10 years')
                else:
                 return render_template('index1.html',prediction_text='these person has not getting cancer after 10 years')
  
        else:
           return render_template('index.html')
      
if __name__=='__main__':
 app.run(debug=True)
