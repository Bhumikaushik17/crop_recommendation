import streamlit as st
import numpy as np
import pickle

# Load model and scalers
model = pickle.load(open('model.pkl', 'rb'))
mx = pickle.load(open('minmaxscaler.pkl', 'rb'))
sc = pickle.load(open('standardscaler.pkl', 'rb'))

# Crop dictionary
crop_dict = {
    1:'rice', 2:'maize', 3:'chickpea', 4:'kidneybeans', 5:'pigeonpeas',
    6:'mothbeans', 7:'mungbean', 8:'blackgram', 9:'lentil', 10:'pomegranate',
    11:'banana', 12:'mango', 13:'grapes', 14:'watermelon', 15:'muskmelon',
    16:'apple', 17:'orange', 18:'papaya', 19:'coconut', 20:'cotton',
    21:'jute', 22:'coffee'
}

st.title("🌾 Crop Recommendation System")
st.markdown("**Enter the following soil and weather details:**")

N = st.number_input("Nitrogen (N)", 0, 140)
P = st.number_input("Phosphorus (P)", 5, 145)
K = st.number_input("Potassium (K)", 5, 205)
temperature = st.number_input("Temperature (°C)", 0.0, 50.0)
humidity = st.number_input("Humidity (%)", 10.0, 100.0)
ph = st.number_input("pH", 3.5, 10.0)
rainfall = st.number_input("Rainfall (mm)", 20.0, 300.0)

if st.button("Recommend Crop"):
    input_data = np.array([[N, P, K, temperature, humidity, ph, rainfall]])
    scaled_data = mx.transform(input_data)
    final_input = sc.transform(scaled_data)
    prediction = model.predict(final_input)[0]
    crop_name = crop_dict[prediction]
    st.success(f"🌱 Recommended Crop: **{crop_name.upper()}**")
