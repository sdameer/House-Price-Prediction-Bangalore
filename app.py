import streamlit as st
import numpy as np
import pickle
import json

# Load the trained model and column data
with open('bhppm.pickle', 'rb') as f:
    model = pickle.load(f)

with open("columns.json", "r") as f:
    columns = json.load(f)
    data_columns = columns['data_columns']
    location_columns = columns['location_columns']

# Function to predict price


def predict_price(location, sqft, bath, bhk):
    # Initialize feature array with zeros
    x = np.zeros(len(data_columns))

    # Set the corresponding feature values
    x[0] = sqft  # Set square footage
    x[1] = bath   # Set number of bathrooms
    x[2] = bhk    # Set number of bedrooms

    # Check if the location exists in the columns and set the corresponding index
    if location in data_columns:
        # Get the index of the location
        loc_index = data_columns.index(location)
        x[loc_index] = 1  # Set the location feature to 1
    else:
        st.error("Location not found in the dataset!")
        return None

    # Make prediction
    price = model.predict([x])[0]

# Convert price to lakhs or crores
    if price >= 100:  # If price is above 1 crore (₹1,00,00,000)
        price_str = f"₹ {price / 100:.2f} Crore"
    elif price >= 1:  # If price is above 1 lakh (₹1,00,000)
        price_str = f"₹ {price:.2f} Lakh"
    else:
        price_str = f"₹ {price * 100:.2f} Thousand"  # This is just an optional case if needed

    return price_str

# Streamlit UI
st.title('House Price Prediction')

st.header('Enter the details to predict the price of the house')

# Dropdown for location selection
location_columns = [location.replace('location_', '') for location in location_columns]
location = st.selectbox('Select the location', location_columns)


# Inputs for square footage, bathrooms, and bedrooms
sqft = st.number_input('Enter the square footage', min_value=100, max_value=10000, step=10)
bath = st.number_input('Enter the number of bathrooms', min_value=1, max_value=10, step=1)
bhk = st.number_input('Enter the number of bedrooms', min_value=1, max_value=10, step=1)

# Button to make the prediction
if st.button('Predict Price'):
    price = predict_price(f"location_{location}", sqft, bath, bhk)
    if price is not None:
        st.success(f'The predicted price of the house is ₹ {price}')
