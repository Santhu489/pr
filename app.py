import pandas as pd
import streamlit as st

# Load your dataset and do any necessary preprocessing here
genes = pd.read_csv("sfari_genes.csv")

def check_gene(gene_symbol):
    if gene_symbol in genes['gene-symbol'].values:
        gene_info = genes[genes['gene-symbol'] == gene_symbol]

        if gene_info['syndromic'].values[0] == 1:
            result = f"The gene {gene_symbol} is associated with autism."
        else:
            result = f"The gene {gene_symbol} is not associated with autism."
    else:
        result = "The gene symbol does not exist in the data."

    return result

def main():
    st.title("Autism gene predictor")

    gene_symbol = st.text_input("Enter Gene Symbol:")
    if st.button("Check"):
        result = check_gene(gene_symbol)
        st.write(result)

if __name__ == "__main__":
    main()
