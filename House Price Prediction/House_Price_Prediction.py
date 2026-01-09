import streamlit as st
import joblib

def yes_no(label, key=None):
    return 1 if st.selectbox(label, options=["yes", "no"], key=key) == "yes" else 0

house_pred_model = joblib.load('housing_model.pkl')

st.title("House Prediction App")
area_sq_ft = st.number_input("Enter Area in sq-ft", value=0)
bedroom = st.number_input("Enter Bedrooms", value=0)
bathroom = st.number_input("Enter Bathrooms", value=0)
stories = st.number_input("Enter Stories", value=0)

main_road = yes_no("Select mainroad", "mainroad")
guestroom = yes_no("Select guestroom", "guestroom")
basement = yes_no("Select basement", "basement")
hotwaterheating = yes_no("Select hotwaterheating", "hotwatreheating")
airconditioning = yes_no("Select airconditioning", "airconditioning")
parking = yes_no("Select parking", "parking")
prefarea = yes_no("Select prefarea", "prefarea")
furnishing_status = st.select_slider("Furnishing Status", options=["Unfurnished", "Semi-Furnished", "Furnished"], value="Semi-Furnished")
furnishing_status = {"Unfurnished" : 0, "Semi-Furnished" : 1, "Furnished" : 2}[furnishing_status]

pred = st.button("Predict")
if pred:
    features = [[area_sq_ft, bedroom, bathroom, stories, main_road, guestroom, basement, hotwaterheating, airconditioning, parking, prefarea, furnishing_status]]
    price = house_pred_model.predict(features)[0]
    st.success(f"Predicted House Price: {price:,.0f}")