from flask import Flask, request, render_template
import requests
from bs4 import BeautifulSoup

req=requests.get("https://themoneyconverter.com/USD/INR")
soup= BeautifulSoup(req.content, "html.parser")
res= soup.output

value=res.get_text()
val=float(value[8:14])
print(val)
import pickle
import numpy as np
path='dpp.pkl'
model = pickle.load(open(path, 'rb'))


app=Flask(__name__)
app.secret_key="diam1234"


@app.route('/input',methods=['GET','POST'])
def input():
    details=request.form
    carat= float(details['carat'])
    cut= int(details['cut'])
    color = int(details['color'])
    clarity = int(details['clarity'])
    depth=float(details['depth'])
    table=float(details['table'])

    prediction=model.predict([[carat ,cut, color, clarity, depth, table ]])
    p=val*prediction[0]
    p=round(p,3)
    msg="Diamond price is Rs."+str(p)
    print(msg)
    return render_template('output.html', msg=msg)

@app.route('/')
def submit():
    return render_template('input.html')

if __name__ == '__main__':
    app.run(debug=True)
