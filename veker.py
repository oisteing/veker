import streamlit as st
from datetime import datetime, date
import matplotlib.pyplot as plt
import numpy as np

st.title("Livet.")

# User input for birth date in DDMMYYYY format
birth_str = st.text_input("Skriv inn fødselsdato (DDMMYYYY):", "01011990")

try:
    # Parse input string
    birth_date = datetime.strptime(birth_str, "%d%m%Y").date()
    
    # Calculate weeks alive
    today = date.today()
    days_alive = (today - birth_date).days
    weeks_alive = days_alive // 7

    # Base grid parameters
    total_dots = 4000
    cols = 80
    rows = total_dots // cols

    # Generate base grid coordinates
    xs = np.tile(np.arange(cols), rows)
    ys = np.repeat(np.arange(rows), cols)

    # Determine counts
    lived = min(weeks_alive, total_dots)
    extra = max(weeks_alive - total_dots, 0)
    extra_rows = (extra + cols - 1) // cols if extra > 0 else 0

    # Adjust figure size to keep dots separated
    base_fig_width = 8
    base_fig_height = 5
    if extra_rows > 0:
        total_rows = rows + extra_rows
        # scale height proportionally
        fig_height = base_fig_height * (total_rows / rows)
    else:
        fig_height = base_fig_height

    # Plotting
    fig, ax = plt.subplots(figsize=(base_fig_width, fig_height))
    # Base gray dots
    ax.scatter(xs, ys, c="lightgray", s=10)
    # Red for weeks lived within first 4000
    if lived > 0:
        ax.scatter(xs[:lived], ys[:lived], c="red", s=10)
    # Light blue for extra weeks beyond 4000
    if extra > 0:
        extra_xs = np.tile(np.arange(cols), extra_rows)[:extra]
        extra_ys = np.repeat(np.arange(rows, rows + extra_rows), cols)[:extra]
        ax.scatter(extra_xs, extra_ys, c="lightblue", s=10)

    ax.set_aspect('equal')
    ax.axis('off')
    
    st.pyplot(fig)

    # Output text
    st.write(f"Du har levd {weeks_alive} veker.")
    if weeks_alive > total_dots:
        st.warning(f"Du er forbi 4000 med {total_dots} veker!")
except ValueError:
    st.error("Invalid date format. Please enter in DDMMYYYY format.")
