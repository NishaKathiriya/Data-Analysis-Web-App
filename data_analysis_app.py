# Install required libraries before running the app
# pip install streamlit pandas seaborn matplotlib

import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Setting up the layout
st.title("📊 Python Data Analysis Web App")
st.write("Upload a dataset (CSV) and explore the data interactively.")

# Sidebar menu
st.sidebar.header("Menu")
menu_options = ["Upload Dataset", "Preview Dataset", "Check Datatype", "Dataset Dimensions", "Find Null Values", "Find Duplicate Values", "Overall Statistics", "About and Credits"]
selection = st.sidebar.radio("Select an option", menu_options)

# Function to load data
@st.cache_data
def load_data(file):
    return pd.read_csv(file)

# Dataset uploader
if selection == "Upload Dataset":
    uploaded_file = st.file_uploader("Choose a CSV file", type=["csv"])
    if uploaded_file is not None:
        # Save the uploaded dataset in session state
        st.session_state['data'] = load_data(uploaded_file)
        st.success("Dataset successfully uploaded!")

# Check if data is available
if 'data' in st.session_state:
    data = st.session_state['data']

# Preview dataset
if selection == "Preview Dataset":
    if 'data' in st.session_state:
        st.subheader("Preview Dataset")
        st.write("Head of the dataset:")
        st.write(data.head())
        st.write("Tail of the dataset:")
        st.write(data.tail())
    else:
        st.error("Please upload a dataset first.")

# Check Datatype of each column
if selection == "Check Datatype":
    if 'data' in st.session_state:
        st.subheader("Column Datatypes")
        st.write(data.dtypes)
    else:
        st.error("Please upload a dataset first.")

# Dataset dimensions
if selection == "Dataset Dimensions":
    if 'data' in st.session_state:
        dim_option = st.radio("Choose to view the number of rows or columns:", ('Rows', 'Columns'))
        if dim_option == 'Rows':
            st.write(f"Number of rows: {data.shape[0]}")
        else:
            st.write(f"Number of columns: {data.shape[1]}")
    else:
        st.error("Please upload a dataset first.")

# Find null values
if selection == "Find Null Values":
    if 'data' in st.session_state:
        st.subheader("Null Values in Dataset")
        st.write(data.isnull().sum())
        if data.isnull().sum().sum() == 0:
            st.success("No null values in the dataset!")
        else:
            st.write("Visualizing null values:")
            fig, ax = plt.subplots(figsize=(10, 6))
            sns.heatmap(data.isnull(), cbar=False, cmap='viridis')
            st.pyplot(fig)
    else:
        st.error("Please upload a dataset first.")

# Find duplicate values
if selection == "Find Duplicate Values":
    if 'data' in st.session_state:
        st.subheader("Duplicate Values in Dataset")
        duplicate_count = data.duplicated().sum()
        st.write(f"Number of duplicate rows: {duplicate_count}")
        if duplicate_count > 0:
            remove_duplicates = st.checkbox("Remove duplicate rows")
            if remove_duplicates:
                data = data.drop_duplicates()
                st.write("Duplicate rows removed!")
    else:
        st.error("Please upload a dataset first.")

# Overall statistics
if selection == "Overall Statistics":
    if 'data' in st.session_state:
        st.subheader("Dataset Statistics")
        st.write(data.describe())
    else:
        st.error("Please upload a dataset first.")

# About and Credits section
if selection == "About and Credits":
    st.subheader("About and Credits")
    st.write("""
    This app is designed to provide an interactive and user-friendly way to explore datasets using Python and Streamlit.
    
    **Author:** Nisha Kathiriya
    
    **Libraries Used:**
    - Streamlit: For building the web app interface
    - Pandas: For data manipulation
    - Seaborn: For visualizing missing values
    - Matplotlib: For plotting graphs
    
    **GitHub:** [Nisha Kathiriya](https://github.com/NishaKathiriya)
    """)

# Instructions to run Streamlit:
# In your terminal/command prompt, navigate to the folder where this script is saved, and run:
# streamlit run your_script_name.py
