import numpy as np
import pickle
import streamlit as st

#loading the saved model
loaded_model=pickle.load(open('D:/zeel/projects/disease prediction/diabetes_model.sav','rb'))

def diabetes():
    st.title('Diabetes prediction')
    st.sidebar.markdown("Diabetes Prediction")
    Pregnancies=st.number_input('Number of pregnancies')
    Glucose=st.number_input("Glucose level")
    BloodPressure=st.number_input("Blood Pressure value")
    SkinThickness=st.number_input("Skin thickness value")
    Insulin=st.number_input("Insulin value")
    BMI=st.number_input("BMI value")
    DiabetesPedigreeFunction=st.number_input("Diabetes Pedigree Function value")
    Age=st.number_input("Age of the person")

    diabetes=''
    
    if st.button("Diabetes Test Result"):
        diabetes=loaded_model.predict([[ Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]])
    # st.success(diabetes)
        if diabetes[0]==0:
            st.success("Not having diabetes")
            st.balloons()
        elif diabetes[0]==1:
            st.success("Having diabetes", icon="⚠️")
            
        else:
            st.success("CLick the button to check the diabetes")