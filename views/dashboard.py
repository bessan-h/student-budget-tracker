import streamlit as st
import pandas as pd
import globalstuff as gs
from styling import apply_custom_styling, section_divider

apply_custom_styling()
gs.loadbudgetdata()

col1, col2 = st.columns([2, 1])
with col1:
    st.title("💰 Student Budget Tracker")
with col2:
    st.empty()

st.markdown("---")

section_divider("Quick Actions")
st.markdown("**Add a new transaction below:**")

col1, col2 = st.columns(2)
with col1:
    st.markdown("### 📤 Add Expense")
    add_expense()
    
with col2:
    st.markdown("### 📥 Add Income")
    add_income()

st.markdown("---")


