import streamlit as st
from pint import UnitRegistry
import os

# Initialize the unit registry
ureg = UnitRegistry()
st.set_page_config(page_title="Advanced Unit Converter", layout="centered")
st.title("🔢 Advanced Unit Converter")

# Dictionary containing categories and their units
categories = {
    "Length": ["meter", "kilometer", "inch", "foot", "yard", "mile", "nautical_mile", "light_year", "parsec", "astronomical_unit"],
    "Mass": ["kilogram", "gram", "milligram", "microgram", "pound", "ounce", "stone", "ton"],
    "Speed": ["meter/second", "kilometer/hour", "mile/hour", "knot", "mach", "speed_of_light"],
    "Temperature": ["kelvin", "celsius", "fahrenheit"],
    "Time": ["second", "minute", "hour", "day", "week", "month", "year"],
    "Volume": ["liter", "milliliter", "cubic_meter", "cubic_foot", "gallon", "quart", "pint"],
    "Energy": ["joule", "kilojoule", "calorie", "kilocalorie", "watt_hour", "kilowatt_hour"],
    "Power": ["watt", "kilowatt", "megawatt", "horsepower"],
    "Pressure": ["pascal", "bar", "atmosphere", "psi"],
    "Data Storage": ["bit", "byte", "kilobyte", "megabyte", "gigabyte", "terabyte", "petabyte"]
}

# UI Components
category = st.selectbox("Select a category", list(categories.keys()))
form_unit = st.selectbox("From", categories[category])
to_unit = st.selectbox("To", categories[category])
value = st.number_input("Enter a value", min_value=0.0, step=0.1)

# Convert button
if st.button("Convert"):
    try:
        # Special handling for temperature
        if category == "Temperature":
            if form_unit == "celsius" and to_unit == "fahrenheit":
                result = (value * 9/5) + 32
            elif form_unit == "fahrenheit" and to_unit == "celsius":
                result = (value - 32) * 5/9
            elif form_unit == "kelvin" and to_unit == "celsius":
                result = value - 273.15
            elif form_unit == "celsius" and to_unit == "kelvin":
                result = value + 273.15
            elif form_unit == "fahrenheit" and to_unit == "kelvin":
                result = (value - 32) * 5/9 + 273.15
            elif form_unit == "kelvin" and to_unit == "fahrenheit":
                result = (value - 273.15) * 9/5 + 32
            else:
                result = value
        else:
            # Ensure units exist in the registry before converting
            if form_unit in ureg and to_unit in ureg:
                result = (value * ureg(form_unit)).to(to_unit).magnitude
            else:
                raise ValueError(f"One or both units '{form_unit}' or '{to_unit}' are not recognized.")

        st.success(f"{value} {form_unit} = {result:.4f} {to_unit}")
    except Exception as e:
        st.error(f"Error: {e}")



