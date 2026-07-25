import streamlit as st
import pandas as pd
import globalstuff as gs
from styling import apply_custom_styling, section_divider
from Subpages.addstuff import add_expense, add_income

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

# Center the forms with margin columns
margin_col1, form_col, margin_col2 = st.columns([0.5, 2, 0.5])

with form_col:
    col1, col2 = st.columns(2, gap="medium")
    
    with col1:
        st.markdown("### 📤 Add Expense")
        add_expense()
        
    with col2:
        st.markdown("### 📥 Add Income")
        add_income()

st.markdown("---")



