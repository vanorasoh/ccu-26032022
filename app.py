#!/usr/bin/env python
# coding: utf-8

# In[1]:


# pip install flask


# In[2]:


from flask import Flask, request, render_template


# In[3]:


app = Flask(__name__) #__name__ => to make sure it is yourself


# In[4]:


import joblib


# In[5]:


# dir(app)
#route by default look for .html. @app - declarator - indicate must run this function first before running the codes below
@app.route("/", methods=["GET","POST"])
def index():
    if request.method == "POST": #this happens after pressing button submit
        purchases = request.form.get("purchases") #add after testing
        suppcard = request.form.get("suppcard") #add after testing
        purchases = float(purchases) #add after testing
        suppcard = float(suppcard) #add after testing
        print(purchases, suppcard) #add after testing
        model1 = joblib.load("CART") #add after testing
        pred1 = model1.predict([[purchases, suppcard]]) #add after testing
        model2 = joblib.load("RF") #add after testing
        pred2 = model2.predict([[purchases, suppcard]]) #add after testing
        model3 = joblib.load("GB") #add after testing
        pred3 = model3.predict([[purchases, suppcard]]) #add after testing
        return(render_template("index.html", result1=pred1, result2=pred2, result3=pred3)) #change from "1" to pred1, pred2, pred3
    else:
        return(render_template("index.html", result1="2", result2="2", result3="2")) #this happens before pressing button submit
        
        
# rates = request.form.get("rates")
# print(rates)
# model = joblib.load("DBS_Reg")
# pred = model.predict([[float(rates)]])
# s = "The predicted DBS share price is " + str(pred)
        


# In[ ]:


if __name__=="__main__":
    app.run() #change from app.run() to app.run(host='0.0.0.0',port=80) if 5000 cannot work


# In[ ]:




