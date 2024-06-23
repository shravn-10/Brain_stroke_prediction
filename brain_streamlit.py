# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 11:05:49 2023

@author: saish
"""

import streamlit as st
import numpy as np
import pickle as pkl

filepath="brain_model.sav"

model=pkl.load(open(filepath,"rb"))


def predict(gender,age,hypertension,heart_disease,ever_married,work_type,Residence_type,avg_glucose_level,bmi,smoking_status):
    if gender=="Male":
        gender=1
    else:
        gender=0
        
    if hypertension=="Yes":
        hypertension=1
    else:
        hypertension=0
        
    if heart_disease=="Yes":
        heart_disease=1
    else:
        heart_disease=0 
        
    if ever_married=="Yes":
        ever_married=1
    else:
        ever_married=0     
        
    if work_type=="Govt_job":
        work_type=0
    elif work_type=="Private":
        work_type=1
    elif work_type=="Self-employed":
        work_type=2
    else:
        work_type=3
        
    if Residence_type=="Urban":
        Residence_type=1
    else:
        Residence_type=0

    if smoking_status=="Unknown":
        smoking_status=0
    elif smoking_status=="formerly smoked":
        smoking_status=1
    elif smoking_status=="smoking_status":
        smoking_status=2
    else:
        smoking_status=3 	          
 
        
    x=[gender,age,hypertension,heart_disease,ever_married,work_type,Residence_type,avg_glucose_level,bmi,smoking_status]
    x=np.array(x).reshape(1,-1)
    print(x)
    
    result=model.predict(x)[0]
    print(result)
    return result




def main():
    gender=st.radio("Select Sex:",["Male","Female"])
    
    age=st.number_input("Age:")
    
    hypertension=st.radio("hypertension:",["Yes","No"])
    
    heart_disease=st.radio("Heart disease:",["Yes","No"])
    
    ever_married=st.radio("Select marriage details:",["Yes","No"])
    
    work_type=st.radio("Select job type:",["Govt_job","Private","Self-employed","Children"])
    
    Residence_type=st.radio("Select residence type:",["Urban","Rural"])
    
    avg_glucose_level=st.number_input("Enter the avg glucose level:")
    
    bmi=st.number_input("BMI:")
    
    smoking_status=st.radio("Smoker:",["Unknown","formerly smoked","never smoked","smokes"])
    
    if st.button("predict stroke or not"):
        print(gender,age,hypertension,heart_disease,ever_married,work_type,Residence_type,avg_glucose_level,bmi,smoking_status)
        result=predict(gender,age,hypertension,heart_disease,ever_married,work_type,Residence_type,avg_glucose_level,bmi,smoking_status)
        
        if result==1:     
            st.write("You are at risk for Brain Stroke")
        else:
            st.write("you are safe, no risk of brain stroke")
           
        
        
if __name__=="__main__":
    main()        
