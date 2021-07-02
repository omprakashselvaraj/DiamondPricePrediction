# DIAMOND PRICE PREDICTION
Diamond Price Prediction is an application to predict the price of diamond by their properties.

# URL
Run this App [Diamond-Price-Predictor](https://diamond-priceprediction.herokuapp.com/).

# CREATED BY
[OMPRAKASH S](https://www.linkedin.com/in/omprakashs2410/)

[JOTHI BATHRA L](https://www.linkedin.com/in/jothi-bathra/)

# DATASET
Thanks to KAGGLE.. you can find dataset here.. [DATASET](https://www.kaggle.com/shivam2503/diamonds)

# Features
- Carat : Carat weight of the Diamond.
- Cut : Describe cut quality of the diamond. Quality in increasing order Fair, Good, Very Good, Premium, Ideal .
- Color : Color of the Diamond. from J (worst) to D (best)
- Clarity : Diamond Clarity refers to the absence of the Inclusions and Blemishes. In order from worst to best :- I1,SI2, SI1, VS2, VS1, VVS2, VVS1, IF
- Depth : The Height of a Diamond, measured from the Culet to the table, divided by its average Girdle Diameter.
- Table : The Width of the Diamond's Table expressed as a Percentage of its Average Diameter.
- Price : the Price of the Diamond.

# Image
![IMAGE](https://www.petragems.com/product_images/uploaded_images/gia-diagramcut.jpg)

# DATA CATEGORY'S
- Qualitative Features (Categorical) : Cut, Color, Clarity.
- Quantitative Features (Numerical) : Carat, Depth , Table , Price.


# Installation
one can install required packages for this application using
```
pip install -r requirements
```

# Separate environment
Alwas create a separate __conda environment/any environment__ so that you can avoid version errors between packages

# Usage
After installing the required packages use the following command to start the flask app
```
python diamond.py
```

# Important Tools used
- python 3.8
- anaconda - jupyter notebook
- backend api: flask
- conda environment
- frontend : HTML,CSS & JAVASCRIPT
- webscraping - beautifulsoap(bs4)

# MODEL USED
Random Forest Regressor

# Accuracy
The accuaracy of model is 96.74

# Input
Fill the Information about diamond required by model in web app's UI

# Output
The model will predict the price of diamond in dollars($) , it is converted into INR using webscraped dollar value and dispayed in output page
