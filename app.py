import streamlit as st
import pandas as pd

st.title("Simple Data Analysis App")

# Upload CSV file
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    # Remove any leading/trailing whitespace from column names
    df.columns = df.columns.str.strip()

    st.subheader("Data Preview")
    st.write(df.head())

    st.subheader("Data Summary")
    st.write(df.describe())

    st.subheader("Filter Data")
    columns = df.columns.tolist()
    selected_column = st.selectbox("Select column to filter by", columns)

    # Get unique values and cast them to strings to avoid type issues
    unique_values = df[selected_column].dropna().unique()
    unique_values = sorted([str(val) for val in unique_values])
    selected_value = st.selectbox("Select value", unique_values)

    # Filter the DataFrame using string comparison
    filtered_df = df[df[selected_column].astype(str) == selected_value]

    if filtered_df.empty:
        st.warning("No data found for selected filter.")
    else:
        st.write("Filtered Data:")
        st.write(filtered_df)

        st.subheader("Plot Data")
        x_column = st.selectbox("Select x-axis column", columns, key="x_axis")
        y_column = st.selectbox("Select y-axis column", columns, key="y_axis")

        if st.button("Generate Plot"):
            if x_column in filtered_df.columns and y_column in filtered_df.columns:
                # Check if Y column is numeric
                if pd.api.types.is_numeric_dtype(filtered_df[y_column]):
                    try:
                        # Optional: Group by x_column if there are duplicates
                        plot_data = (
                            filtered_df.groupby(x_column)[y_column]
                            .mean()
                            .sort_index()
                        )
                        st.line_chart(plot_data)
                    except Exception as e:
                        st.error(f"Could not generate chart: {e}")
                else:
                    st.warning("Selected Y-axis column must contain numeric values.")
            else:
                st.warning("Selected columns are not available in the filtered data.")
else:
    st.write("Waiting on file upload...")
