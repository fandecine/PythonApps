import time  # For sleep
from datetime import time as datetime_time  # For time input
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set page layout to wide
st.set_page_config(layout="wide")

# --- Title and Description ---
st.title('Streamlit Widgets Demonstration')
st.write('This app demonstrates various Streamlit widgets and how they interact with data.')

# --- Create Columns for Widgets ---
col1, col2 = st.columns(2)  # Creates two columns

with col1:
    # --- 1. Text Input ---
    user_input = st.text_input('Enter some text:', 'Streamlit is awesome!')
    st.write(f'You entered: {user_input}')

    # --- 2. Number Input ---
    user_number = st.number_input('Enter a number:', min_value=0, max_value=100, value=50)
    st.write(f'You entered the number: {user_number}')

    # --- 3. Slider ---
    slider_value = st.slider('Select a range of values:', 0, 100, (25, 75))
    st.write(f'You selected the range: {slider_value}')

    # --- 4. Selectbox ---
    option = st.selectbox('Choose a category:', ['Option A', 'Option B', 'Option C'])
    st.write(f'You selected: {option}')

    # --- 5. Multi-Select ---
    options = st.multiselect('Pick some options:', ['Option A', 'Option B', 'Option C'])
    st.write(f'You selected: {options}')

with col2:
    # --- 6. Checkbox ---
    checkbox_value = st.checkbox('Show additional information')
    if checkbox_value:
        st.write('You have selected the checkbox to display extra info.')

    # --- 7. Radio Buttons ---
    radio_option = st.radio('Choose one option:', ['Option A', 'Option B', 'Option C'])
    st.write(f'You selected: {radio_option}')

    # --- 8. File Uploader ---
    uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])
    if uploaded_file is not None:
        data = pd.read_csv(uploaded_file)
        st.write(data)

# --- 9. Date Input ---
selected_date = st.date_input('Pick a date')
st.write(f'You selected: {selected_date}')

# --- 10. Time Input ---
selected_time = st.time_input('Pick a time', datetime_time(8, 45))  # Using datetime.time
st.write(f'You selected: {selected_time}')

# --- 11. Color Picker ---
selected_color = st.color_picker('Pick a color', '#00f900')
st.write(f'You selected the color: {selected_color}')

# --- 12. Displaying a Map ---
df_map = pd.DataFrame({
    'latitude': np.random.uniform(low=37.0, high=38.0, size=100),
    'longitude': np.random.uniform(low=-122.0, high=-121.0, size=100),
})
st.map(df_map)

# --- Create Two Columns for Charts ---
col1, col2 = st.columns(2)

with col1:
    # --- Line Chart ---
    st.subheader('Line Chart')
    fig, ax = plt.subplots()
    ax.plot(np.linspace(0, 100, 100), np.random.randn(100) * 20 + 50)
    ax.set_title('Line Chart: Y vs. X')
    st.pyplot(fig)

    # --- Histogram ---
    st.subheader('Histogram')
    fig3, ax3 = plt.subplots()
    ax3.hist(np.random.randn(100) * 20 + 50, bins=15, color='green', edgecolor='black')
    ax3.set_title('Histogram of Y values')
    st.pyplot(fig3)

with col2:
    # --- Scatter Plot ---
    st.subheader('Scatter Plot')
    fig2, ax2 = plt.subplots()
    ax2.scatter(np.linspace(0, 100, 100), np.random.randn(100) * 20 + 50, c='red')
    ax2.set_title('Scatter Plot: Y vs. X')
    st.pyplot(fig2)

    # --- Boxplot ---
    st.subheader('Boxplot')
    fig4, ax4 = plt.subplots()
    sns.boxplot(x=np.random.choice(['A', 'B', 'C'], 100), y=np.random.randn(100) * 20 + 50, ax=ax4)
    ax4.set_title('Boxplot of Y by Category')
    st.pyplot(fig4)

# --- Progress Bar and Spinner ---
progress_col1, progress_col2 = st.columns(2)

with progress_col1:
    # --- 13. Progress Bar ---
    progress_bar = st.progress(0)
    for i in range(100):
        time.sleep(0.1)  # Correctly using time.sleep() from the standard library
        progress_bar.progress(i + 1)
    st.success('Done!')

with progress_col2:
    # --- 14. Spinner ---
    with st.spinner('Processing your request...'):
        time.sleep(2)  # Correctly using time.sleep() from the standard library
    st.success('Processing complete!')

# --- Expander for Detailed Explanation ---
with st.expander("See explanation"):
    st.write("Here is the detailed explanation of how Streamlit widgets work.")
    st.write("You can create interactive applications easily with a few lines of code.")

# --- Conclusion ---
st.write("This app demonstrates the variety of widgets Streamlit offers to create interactive applications!")
st.write("You can modify this code to add more data visualizations or widgets.")
