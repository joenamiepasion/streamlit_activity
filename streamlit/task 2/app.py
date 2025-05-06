import streamlit as st
import pandas as pd

st.title("CSV Data Viewer")
st.write("Upload a CSV file to explore the data.")

# File uploader
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    try:
        # Load the CSV file into a DataFrame
        df = pd.read_csv(uploaded_file)

        # Check if the CSV has at least 5 columns
        if df.shape[1] >= 5:
            st.success("File uploaded and loaded successfully!")

            # Checkbox to show raw data
            if st.checkbox("Show raw data"):
                st.subheader("Raw Data")
                st.dataframe(df)

            # Selectbox to choose a column to filter
            selected_column = st.selectbox("Select a column to filter:", df.columns)

            if selected_column:
                unique_values = df[selected_column].unique()
                selected_value = st.selectbox(f"Select a value from '{selected_column}':", unique_values)

                # Filter and display the data
                filtered_df = df[df[selected_column] == selected_value]
                st.subheader("Filtered Data")
                st.dataframe(filtered_df)

        else:
            st.error("The uploaded file must contain at least 5 columns.")

    except Exception as e:
        st.error(f"Error loading file: {e}")
else:
    st.info("Please upload a CSV file to begin.")
