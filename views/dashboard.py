import streamlit as st
import pandas as pd

st.title("Student Budget Tracker")

# User Input
expense_type = st.selectbox("Category", ["Food", "Rent", "Books", "Entertainment"])
amount = st.number_input("Amount ($)", min_value=0.0, step=1.0)

if st.button("Add Expense"):
    st.success(f"Added ${amount} to {expense_type}!")
    
