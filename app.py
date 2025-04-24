import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Simple Data Analysis App")

uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)


    df.columns = df.columns.str.strip()

    st.subheader("Data Preview")
    st.write(df.head())

    st.subheader("Data Summary")
    st.write(df.describe())

    st.subheader("Filter Data")
    columns = df.columns.tolist()
    selected_column = st.selectbox("Select column to filter by", columns)
    unique_values = df[selected_column].unique()
    selected_value = st.selectbox("Select value", unique_values)

    filtered_df = df[df[selected_column] == selected_value]
    st.write("Filtered Data:")
    st.write(filtered_df)

    st.subheader("Plot Data")
    x_column = st.selectbox("Select x-axis column", columns, key="x_axis")
    y_column = st.selectbox("Select y-axis column", columns, key="y_axis")

    if st.button("Generate Plot"):
        if x_column in filtered_df.columns and y_column in filtered_df.columns:
            try:
                # Ensure x_column can be set as index
                plot_data = filtered_df.set_index(x_column)[y_column]
                st.line_chart(plot_data)
            except Exception as e:
                st.error(f"Could not generate chart: {e}")
        else:
            st.warning("Selected columns are not available in the filtered data.")
else:
    st.write("Waiting on file upload...")
