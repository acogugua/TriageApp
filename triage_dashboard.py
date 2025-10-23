#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st
import pandas as pd
import plotly.express as px

# Load triage results
df = pd.read_csv('triage_results_with_ml.csv')##
#df = pd.read_csv('triage_batch_results.csv')

# Page setup
st.set_page_config(page_title="Hospital Triage Dashboard", layout="wide")
st.title("🏥 Hospital Triage Classification Dashboard")

# Show raw data
st.subheader("📋 Triage Results Table")
st.dataframe(df)

# Pie chart: Diagnosis distribution
st.subheader("🧠 Diagnosis Classification Distribution")
fig_diag = px.pie(df, names='diagnosis_label', title='Diagnosis Classification')
st.plotly_chart(fig_diag, use_container_width=True)

# Pie chart: Inference distribution
st.subheader("🩺 Inference Classification Distribution")
fig_inf = px.pie(df, names='inference_label', title='Inference Classification')
st.plotly_chart(fig_inf, use_container_width=True)

# Bar chart: Diagnosis per file
st.subheader("📁 Normalised Triage Classification by Referral File")
fig_bar = px.bar(df, x='file', color='diagnosis_label', title='Diagnosis per File')
st.plotly_chart(fig_bar, use_container_width=True)


# In[ ]:




