import streamlit as st
from diabetics import diabetes
from heartdisease import heart_prediction

def main_page():
    st.title("Diabetes and Heart Prediction website")
    st.sidebar.markdown("Diabetes and Heart Prediction website")
    st.write('This is a diabetes and heart prediction website! This both disease are nowadays very common to people as number of people are having these disease and many people are dying due to this disease')
    st.write('So to prevent people from dying they should know whether they are having this disease or not? When they feel like having some symtomps realted to this disease they can visit our website and predict the disease without even going to doctor and this model is very accurate.')
    st.write('We wanted to take care of the people so we made a good prediction model for this disease to save the life of the people')



page_names_to_funcs = {
    "✅Main Page": main_page,
    "🔍Diabetes Prediction ": diabetes,
    "📈 Heart prediction": heart_prediction,
}
selected_page = st.sidebar.selectbox("Select a page", page_names_to_funcs.keys())
page_names_to_funcs[selected_page]()