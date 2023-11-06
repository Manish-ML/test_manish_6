import pickle
import numpy as np
model=pickle.load(open('classifier.pkl1','rb'))
from flask import Flask,render_template,request

app=Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/predict',methods=['POST'])
def predict():
    Gender= request.form.get('Gender')
    if Gender == "Male":
        Gender = 0
    else:
        Gender = 1
    Married = request.form.get('Married')
    if Married == "Unmarried":
        Married = 0
    else:
        Married = 1

    ApplicantIncome = int(request.form.get('ApplicantIncome'))


    LoanAmount =int( request.form.get('LoanAmount'))
    LoanAmount=LoanAmount/1000


    Credit_History= request.form.get('Credit_History')

    result=model.predict(np.array([[Gender,Married,ApplicantIncome,LoanAmount,Credit_History]]))
    if result[0] == 0:
        result='loan not paased'
    else:
        result='loan paased'
    return render_template('index.html',result=result)



if __name__ =='__main__':
    app.run(debug=True)

