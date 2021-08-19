#Importing required Libraries
#flask for API development
from flask import Flask, request, render_template
#requests and bs4 for web scraping
import requests
from bs4 import BeautifulSoup
#pickle for reading .pkl file
import pickle
#numpy for array
import numpy as np

#web scraping for dollar value in INR
req=requests.get("https://themoneyconverter.com/USD/INR")
soup= BeautifulSoup(req.content, "html.parser")
res= soup.output

value=res.get_text()
val=float(value[8:14])

#reading .pkl file
path='dpp.pkl'
model = pickle.load(open(path, 'rb'))

#creating instance for Flask 
app=Flask(__name__)
app.secret_key="diam1234"

#getting input from frontend
@app.route('/input',methods=['GET','POST'])
def input():
    details=request.form
    #getting carat, cut, color, clarity, depth and table as input to predict diamond price
    carat= float(details['carat'])
    cut= int(details['cut'])
    color = int(details['color'])
    clarity = int(details['clarity'])
    depth=float(details['depth'])
    table=float(details['table'])
    #passing values as numpy array and predicting the price in dollar
    prediction=model.predict([[carat ,cut, color, clarity, depth, table ]])
    #converting dollar to INR using web scraped data
    p=val*prediction[0]
    p=round(p,3)
    msg="Diamond price is Rs."+str(p)
    print(msg)
    #rendering price to output page
    return render_template('output.html', msg=msg)

#rendering to input page
@app.route('/')
def submit():
    return render_template('input.html')
#main function
if __name__ == '__main__':
    app.run(debug=True)
