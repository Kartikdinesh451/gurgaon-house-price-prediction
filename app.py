from pathlib import Path
import joblib
import pandas as pd
import streamlit as st

ROOT = Path(__file__).resolve().parent
model = joblib.load(ROOT / "models" / "model.pkl")
pipeline = joblib.load(ROOT / "models" / "pipeline.pkl")

st.set_page_config(page_title="Gurgaon House Price Prediction", page_icon="🏠", layout="wide")

st.title("🏠 Gurgaon House Price Prediction")
st.caption("Portfolio-ready Random Forest regression pipeline with preprocessing and categorical encoding.")

c1, c2, c3 = st.columns(3)
with c1:
    longitude = st.number_input("Longitude", value=-118.39)
with c2:
    latitude = st.number_input("Latitude", value=34.12)
with c3:
    median_income = st.number_input("Median income", value=5.0, min_value=0.0)

c4, c5, c6 = st.columns(3)
with c4:
    housing_median_age = st.number_input("Housing median age", value=30.0, min_value=0.0)
with c5:
    total_rooms = st.number_input("Total rooms", value=2000.0, min_value=0.0)
with c6:
    total_bedrooms = st.number_input("Total bedrooms", value=300.0, min_value=0.0)

c7, c8, c9 = st.columns(3)
with c7:
    population = st.number_input("Population", value=800.0, min_value=0.0)
with c8:
    households = st.number_input("Households", value=300.0, min_value=0.0)
with c9:
    ocean_proximity = st.selectbox(
        "Location category",
        ["<1H OCEAN", "INLAND", "ISLAND", "NEAR BAY", "NEAR OCEAN"]
    )

if st.button("Predict House Value", type="primary"):
    row = pd.DataFrame([{
        "longitude": longitude,
        "latitude": latitude,
        "housing_median_age": housing_median_age,
        "total_rooms": total_rooms,
        "total_bedrooms": total_bedrooms,
        "population": population,
        "households": households,
        "median_income": median_income,
        "ocean_proximity": ocean_proximity,
    }])
    transformed = pipeline.transform(row)
    prediction = model.predict(transformed)[0]
    st.success(f"Estimated house value: ${prediction:,.0f}")
