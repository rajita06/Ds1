
import streamlit as st
import pickle

# Load your trained model
model = pickle.load(open('model.pkl', 'rb'))

st.title('House Price Prediction')

# Input fields
size = st.slider('Size of house (sq ft)', 500, 5000, step=100)
location_map = {'Urban': 0, 'Suburban': 1, 'Rural': 2}
location = st.selectbox('Location', ['Urban', 'Suburban', 'Rural'])

# Predict button
if st.button('Predict'):
    # Prepare input data
    input_data = [[size, location_map[location]]]
    prediction = model.predict(input_data)
    st.success(f'Predicted Price: ${prediction[0]:,.2f}')
