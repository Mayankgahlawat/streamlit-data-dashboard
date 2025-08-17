import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Interactive Data Dashboard")

uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    
    st.success("Here is a preview of your data:")
    st.dataframe(df.head())

    # --- SIDEBAR WIDGETS ---
    st.sidebar.header("Plotting Options")
    columns = df.columns.tolist()
    x_axis = st.sidebar.selectbox("Choose the X-axis", options=columns)
    y_axis = st.sidebar.selectbox("Choose the Y-axis", options=columns)

    # --- CREATE AND DISPLAY THE PLOT ---
    st.header(f"Scatter Plot: {y_axis} vs. {x_axis}")
    
    # Create a figure and axes for the plot
    fig, ax = plt.subplots()
    
    # Create the scatter plot
    ax.scatter(df[x_axis], df[y_axis])
    
    # Set labels for the plot
    ax.set_xlabel(x_axis)
    ax.set_ylabel(y_axis)
    
    # Display the plot in the Streamlit app
    st.pyplot(fig)