import numpy as np
import pickle
import pandas as pd
import streamlit as st
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

heart_disease_model=pickle.load(open('D:/zeel/projects/disease prediction/heart_disease_model.sav','rb'))

def heart_prediction():
    st.title('Heart Disease Prediction')
    st.sidebar.markdown("Heart Prediction ")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.number_input('Age',min_value=0,max_value=200,value=0)
        
    with col2:
        sex = st.number_input('Sex male-1 and female-0',min_value=0,max_value=1,value=0)
        
    with col3:
        cp = st.number_input('Chest Pain types',min_value=0,max_value=4,value=0)
        
    with col1:
        trestbps = st.number_input('Resting Blood Pressure',min_value=0,max_value=300,value=0)
        
    with col2:
        chol = st.number_input('Serum Cholestoral in mg/dl',min_value=0,max_value=1000,value=0)
        
    with col3:
        fbs = st.number_input('Fasting Blood Sugar > 120 mg/dl 1-> true and 0->false',min_value=0,max_value=1,value=0)
        
    with col1:
        restecg = st.number_input('Resting Electrocardiographic results',min_value=0,max_value=6,value=0)
        
    with col2:
        thalach = st.number_input('Maximum Heart Rate achieved',min_value=0,max_value=1000,value=0)
        
    with col3:
        exang = st.number_input('Exercise Induced Angina 1->yes and 0-> no',min_value=0,max_value=1,value=0)
        
    with col1:
        oldpeak = st.number_input('ST depression induced by exercise',min_value=0.0,max_value=25.0,value=0.0)
        
    with col2:
        slope = st.number_input('Slope of the peak exercise ST segment',min_value=0,max_value=2,value=0)
        
    with col3:
        ca = st.number_input('Major vessels(0-3) colored by flourosopy',min_value=0,max_value=4,value=0)
        
    with col1:
        thal = st.number_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect',min_value=0,max_value=3,value=0)
        
    # code for Prediction
    heart_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Heart Disease Test Result'):
        heart_prediction = heart_disease_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg,thalach,exang,oldpeak,slope,ca,thal]])                          
        
        if (heart_prediction[0] == 1):
          heart_diagnosis = 'The person is having heart disease,icon="⚠️"'
          st.success(heart_diagnosis)
        else:
          heart_diagnosis = 'The person does not have any heart disease'
          st.success(heart_diagnosis)
          st.balloons()
        
    
