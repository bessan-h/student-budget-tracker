
import streamlit as st
import pandas as pd
import globalstuff as gs
import datetime as dt

def add_expense():
    with st.form("expense_form", border=False):
        st.markdown("**Select expense details:**")
        expense_type = st.selectbox(
            "Expense Category",
            ["Food 🍔", "Rent 🏠", "Books 📚", "Entertainment 🎮"],
            key="expense_category"
        )
        
        amountexp = st.number_input(
            "Expense Amount ($)",
            min_value=0.0,
            step=0.01,
            format="%.2f",
            key="expense_amount"
        )
        
        col1, col2 = st.columns([1, 1])
        with col1:
            submitted = st.form_submit_button("➕ Add Expense", use_container_width=True)
        with col2:
            st.empty()
        
        if submitted:
            if amountexp <= 0:
                st.error("❌ Please enter a valid amount greater than $0")
            else:
                # Extract category name without emoji
                category = expense_type.split()[0]
                
                if category == "Food":
                    gs.food += amountexp
                elif category == "Rent":
                    gs.rent += amountexp
                elif category == "Books":
                    gs.books += amountexp
                elif category == "Entertainment":
                    gs.entertainment += amountexp
                    
                gs.monthexpenses += amountexp
                st.success(f"✅ Added **${amountexp:.2f}** to {category}!")
                gs.savetransactiontocsv((amountexp*-1), category)
                gs.cycle()

def add_income():
    with st.form("income_form", border=False):
        st.markdown("**Add income:**")
        
        amountinc = st.number_input(
            "Income Amount ($)",
            min_value=0.0,
            step=0.01,
            format="%.2f",
            key="income_amount"
        )
        
        col1, col2 = st.columns([1, 1])
        with col1:
            submitted = st.form_submit_button("➕ Add Income", use_container_width=True)
        with col2:
            st.empty()
        
        if submitted:
            if amountinc <= 0:
                st.error("❌ Please enter a valid amount greater than $0")
            else:
                gs.monthbudget += amountinc
                st.success(f"✅ Added **${amountinc:.2f}** to your budget!")
                gs.savetransactiontocsv(amountinc, "Income")
                gs.cycle()
