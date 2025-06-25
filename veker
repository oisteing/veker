import streamlit as st
from datetime import datetime, date
import matplotlib.pyplot as plt
import numpy as np

st.title("Livet.")

# User input for birth date in DDMMYYYY format
birth_str = st.text_input("Fødselsdato (DDMMYYYY):", "01011980")

try:
    # Parse input string
    birth_date = datetime.strptime(birth_str, "%d%m%Y").date()
    
    # Calculate weeks alive
    today = date.today()
    days_alive = (today - birth_date).days
    weeks_alive = days_alive // 7
    
    # Total dots
    total_dots = 4000
    
    # Grid dimensions (e.g., 80 cols x 50 rows)
    cols = 80
    rows = total_dots // cols
    
    # Generate grid coordinates
    xs = np.tile(np.arange(cols), rows)
    ys = np.repeat(np.arange(rows), cols)
    
    # Determine colors: red for weeks alive, light gray for remaining
    colors = np.array(["lightgray"] * total_dots)
    colors[:min(weeks_alive, total_dots)] = "red"
    
    # Plotting
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.scatter(xs, ys, c=colors, s=10)
    ax.set_aspect('equal')
    ax.axis('off')
    
    st.pyplot(fig)
    
    st.write(f"Du har levd i {weeks_alive} veker.")
    if weeks_alive > total_dots:
        st.warning(f"You've surpassed {total_dots} weeks!")
except ValueError:
    st.error("Invalid date format. Please enter in DDMMYYYY format.")
    
