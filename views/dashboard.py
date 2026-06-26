import streamlit as st
import pandas as pd
import globalstuff as gs

st.title("Student Budget Tracker")

# User Input
expense_type = st.selectbox("Expense Category", ["Food", "Rent", "Books", "Entertainment"])
amountexp= st.number_input("ExpenseAmount ($)", min_value=0.0, step=1.0)

if st.button("Add Expense"):
    if expense_type == "Food":
        gs.food += amountexp
    elif expense_type == "Rent":
        gs.rent += amountexp
    elif expense_type == "Books":
        gs.books += amountexp
    elif expense_type == "Entertainment":
        gs.entertainment += amountexp
    gs.monthexpenses += amountexp
    st.success(f"Added ${amountexp} to {expense_type}!")

amountinc = st.number_input("Income Amount ($)", min_value=0.0, step=1.0, key="income")
if st.button("Add Income"):
    
    gs.monthbudget += amountinc
    st.success(f"Added ${amountinc} to income!")
