# app.py
import streamlit as st
import pandas as pd
import numpy as np
import joblib


model = joblib.load('model_rf.pkl')

# Your actual towns from the dataset
town_list = sorted([
    'Agbara-Igbesa', 'Agege', 'Ajah', 'Alimosho', 'Amuwo Odofin', 'Apapa', 'Apo', 'Asokoro District', 'Ayobo', 'Badagry', 'Bwari', 'Central Business District',      'Dakibiyu', 'Dakwo', 'Dape', 'Dei-Dei', 'Diplomatic Zones', 'Duboyi', 'Durumi', 'Dutse', 'Egbe', 'Ejigbo', 'Epe', 'Gaduwa', 'Galadimawa', 'Garki','Gbagada',     'Gudu', 'Guzape District', 'Gwagwalada', 'Gwarinpa', 'Ibeju', 'Ibeju Lekki', 'Idimu', 'Idu Industrial', 'Ifako-Ijaiye', 'Ijaiye', 'Ijede', 'Ijesha', 'Ikeja'     'Ikorodu', 'Ikotun', 'Ikoyi', 'Ilupeju', 'Imota', 'Ipaja', 'Isheri', 'Isheri North', 'Isolo', 'Jabi', 'Jahi', 'Kabusa', 'Kado', 'Kafe', 'Kagini', 'karmo'        'Karsana', 'Karshi', 'Karu', 'Katampe', 'Kaura', 'Ketu', 'Kosofe', 'Kubwa', 'Kuje', 'Kukwaba', 'Kurudu', 'Kyami', 'Lagos Island', 'Lekki', 
    'Life Camp','Lokogoma District', 'Lugbe District', 'Mabushi', 'Magodo', 'Maitama District', 'Mararaba', 'Maryland', 'Mbora (Nbora)', 'Mpape','Mushin',           'Nyanya','Ogudu','Ojo', 'Ojodu', 'Ojota', 'Oke-Odo', 'Orile', 'Orozo', 'Oshodi', 'Shomolu', 'Surulere', 'Utako', 'Victoria Island (VI)', 'Wumba', 'Wuse',        'Wuse 2','Wuye', 'Yaba'

])

title_list = [
    'Detached Duplex', 'Semi Detached Duplex', 'Terraced Duplexes',
    'Detached Bungalow', 'Semi Detached Bungalow',
    'Terraced Bungalow', 'Block of Flats'
]

state_list = ['Lagos', 'Abuja']

# --- UI ---
st.set_page_config(page_title="Nigerian House Price Predictor")
st.title(" Nigerian House Price Predictor")
st.markdown("Predicting house prices in **Lagos** and **Abuja**")

col1, col2 = st.columns(2)

with col1:
    state = st.selectbox("State", state_list)
    town = st.selectbox("Town", town_list)
    title = st.selectbox("Property Type", title_list)

with col2:
    bedrooms = st.slider("Bedrooms", 1, 10, 3)
    bathrooms = st.slider("Bathrooms", 1, 10, 2)
    total_no_of_rooms = st.slider("Total Rooms", 1, 20, 6)

# Interaction features
bath_per_bed = bathrooms / (bedrooms + 1)
room_per_bed = total_no_of_rooms / (bedrooms + 1)
bed_x_bath = bedrooms * bathrooms
is_large = int(total_no_of_rooms >= 5)

if st.button("Predict Price", type="primary"):
    input_df = pd.DataFrame([{
        'town': town,
        'title': title,
        'state': state,
        'bedrooms': float(bedrooms),
        'bathrooms': float(bathrooms),
        'total_no_of_rooms': float(total_no_of_rooms),
        'bath_per_bed': bath_per_bed,
        'room_per_bed': room_per_bed,
        'bed_x_bath': float(bed_x_bath),
        'is_large': is_large
    }])

    log_pred = model.predict(input_df)
    price = np.expm1(log_pred)[0]

    st.success(f"Estimated Price: ₦{price:,.0f}")
    st.caption("Prediction based on Lagos & Abuja property data")