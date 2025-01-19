import pandas as pd
import streamlit as st
import altair as alt
from PIL import Image
import base64

# --------------------------
# Page Title and Logo Display
# --------------------------

# Load and encode the image for display
image_path = 'dna-logo.png'
image = Image.open(image_path)

with open(image_path, "rb") as img_file:
    img_base64 = base64.b64encode(img_file.read()).decode("utf-8")

# Display the image centered on the page
st.markdown(
    f"""
    <div style="text-align: center;">
        <img src="data:image/png;base64,{img_base64}" alt="Logo" style="width: 200px;">
    </div>
    """,
    unsafe_allow_html=True
)

# Title and description
st.write("""
# DNA Nucleotide Count Web App

This app calculates and displays the nucleotide composition of a given DNA sequence.

***
""")

# --------------------------
# User Input Section
# --------------------------

# Text area for user to input DNA sequence
st.header('Enter DNA sequence')
sequence_input = """>DNA Query 2
GAACACGTGGAGGCAAACAGGAAGGTGAAGAAGAACTTATCCTATCAGGACGGAAGGTCCTGTGCTCGGG
ATCTTCCAGACGTCGCGACTCTAAATTGCCCCCTCTGAGGTCAAG"""

# Process input sequence
sequence = st.text_area("Sequence input", sequence_input, height=250)
sequence = sequence.splitlines()[1:]  # Remove the sequence name (first line)
sequence = ''.join(sequence)  # Concatenate list to a single string

st.write("***")

# --------------------------
# Display Input Sequence
# --------------------------

st.header('INPUT (DNA Query)')
st.write(sequence)

# --------------------------
# DNA Nucleotide Count Calculation
# --------------------------

st.header('OUTPUT (DNA Nucleotide Count)')

# Function to count each nucleotide
def DNA_nucleotide_count(seq):
    counts = {
        'A': seq.count('A'),
        'T': seq.count('T'),
        'G': seq.count('G'),
        'C': seq.count('C')
    }
    return counts

# Perform count and store result
nucleotide_counts = DNA_nucleotide_count(sequence)

# 1. Display counts as a dictionary
st.subheader('1. Nucleotide Count Dictionary')
st.write(nucleotide_counts)

# 2. Display counts as text
st.subheader('2. Nucleotide Count Details')
st.write(f"There are {nucleotide_counts['A']} adenine (A)")
st.write(f"There are {nucleotide_counts['T']} thymine (T)")
st.write(f"There are {nucleotide_counts['G']} guanine (G)")
st.write(f"There are {nucleotide_counts['C']} cytosine (C)")

# 3. Display counts in a DataFrame
st.subheader('3. Nucleotide Count DataFrame')
df = pd.DataFrame.from_dict(nucleotide_counts, orient='index', columns=['Count']).reset_index()
df.rename(columns={'index': 'Nucleotide'}, inplace=True)
st.write(df)

# 4. Display counts as a bar chart using Altair
st.subheader('4. Nucleotide Count Bar Chart')
chart = alt.Chart(df).mark_bar().encode(
    x='Nucleotide',
    y='Count'
).properties(width=alt.Step(80))  # Controls width of the bars
st.write(chart)

