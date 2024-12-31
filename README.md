# House-Price-Prediction-Bangalore
House Price Prediction - Bangalore This project predicts the price of houses in Bangalore based on key factors such as location, square footage, number of bathrooms, and number of bedrooms. It uses a trained machine learning model and a simple web interface built with Streamlit for user interaction.
---

## Features

- **House Price Prediction:** Predicts prices in units such as Lakhs, Crores, and Thousands.
- **User-Friendly Interface:** A simple and interactive web app for inputting house details.
- **Location-Based Prediction:** Incorporates location as a key factor for prediction accuracy.

---

## Tech Stack

- **Programming Language:** Python
- **Libraries:**
  - Machine Learning: scikit-learn, numpy, pandas
  - Web Application: Streamlit
  - File Handling: pickle, json

---

## Dataset

The model is trained on real-world house price data from Bangalore, with features including:
- Location
- Square Footage
- Number of Bathrooms
- Number of Bedrooms

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/sdameer/House-Price-Prediction-Bangalore.git
   ```

2. Navigate to the project directory:
   ```bash
   cd House-Price-Prediction-Bangalore
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:
   ```bash
   streamlit run app.py
   ```

---

## Usage

1. Enter details such as location, square footage, number of bathrooms, and bedrooms in the Streamlit app.
2. Click on the **Predict Price** button.
3. View the predicted house price in Lakhs or Crores.

---

## Project Structure

- `app.py`: Main application file.
- `bhppm.pickle`: Trained machine learning model.
- `columns.json`: Metadata about features and locations.
- `requirements.txt`: List of dependencies.

---

## Future Improvements

- Add support for more cities.
- Enhance model accuracy with more data.
---

## License

This project is licensed under the MIT License. See the LICENSE file for details.

---

## Acknowledgments

- Kaggle for providing the dataset.
- The Python and Streamlit communities for their fantastic tools and support.

---

## Contact

For questions or feedback, feel free to reach out:
- kaggle : [sdameer](https://kaggle.com/sdameer)
- GitHub: [sdameer](https://github.com/sdameer)

