import streamlit as st
import pandas as pd

# Load CSV file
file_path = st.file_uploader("sfari_genes.csv", type=["csv"])

# Check if a file is uploaded
if file_path is not None:
    # Read CSV file into DataFrame
    df = pd.read_csv(file_path)

    # Display DataFrame
    st.write("## Displaying CSV Data")
    st.dataframe(df)

    # Prediction Section
    st.write("## Autism Gene Prediction")

    # User input for gene symbol
    gene_symbol = st.text_input("Enter a gene symbol:")

    if st.button("Predict"):
        # Check if the gene symbol exists in the data
        if gene_symbol in df['gene-symbol'].values:
            # Extract the corresponding row from the dataframe
            gene_info = df[df['gene-symbol'] == gene_symbol]

            # Check if the gene is syndromic or not
            if gene_info['syndromic'].values[0] == 1:
                st.write(f"The gene {gene_symbol} is associated with autism.")
            else:
                st.write(f"The gene {gene_symbol} is not associated with autism.")
        else:
            st.write("The gene symbol does not exist in the data.")

