import streamlit as st
import pandas as pd
import plotly.express as px

# Load triage results
df = pd.read_csv('triage_results_with_ml.csv')  # Ensure this file exists in your repo

# Page setup
st.set_page_config(page_title="Hospital Triage Dashboard", layout="wide")
st.title("🏥 Hospital Triage Classification Dashboard")

# 🔍 Search section
st.subheader("🔎 Search Patient by File Number")
file_number = st.text_input("Enter File Number")

if st.button("Search"):
    result = df[df['file'] == file_number]
    if not result.empty:
        diagnosis = result.iloc[0]['diagnosis_label']
        inference = result.iloc[0]['inference_label']
        reason_diag = result.iloc[0].get('reason_diagnosis', 'Reason for diagnosis not available')
        reason_inf = result.iloc[0].get('reason_inference', 'Reason for inference not available')

        st.success("Patient Found")
        st.markdown(
            f"<div style='font-size:18px;'>"
            f"<span title='{reason_diag}' style='color:darkred;'>🧠 Diagnosis: {diagnosis}</span><br>"
            f"<span title='{reason_inf}' style='color:darkblue;'>🩺 Inference: {inference}</span>"
            f"</div>",
            unsafe_allow_html=True
        )
    else:
        st.error("No patient found with that file number.")

# 📋 Show raw data
st.subheader("📋 Triage Results Table")
st.dataframe(df)

# 🧠 Pie chart: Diagnosis distribution
st.subheader("🧠 Diagnosis Classification Distribution")
fig_diag = px.pie(df, names='diagnosis_label', title='Diagnosis Classification')
st.plotly_chart(fig_diag, use_container_width=True)

# 🩺 Pie chart: Inference distribution
st.subheader("🩺 Inference Classification Distribution")
fig_inf = px.pie(df, names='inference_label', title='Inference Classification')
st.plotly_chart(fig_inf, use_container_width=True)

# 📁 Bar chart: Diagnosis per file
st.subheader("📁 Normalised Triage Classification by Referral File")
fig_bar = px.bar(df, x='file', color='diagnosis_label', title='Diagnosis per File')
st.plotly_chart(fig_bar, use_container_width=True)