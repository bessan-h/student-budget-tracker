import streamlit as st
import pandas as pd
import globalstuff as gs
import datetime as dt

st.title("Transaction History")

if st.button("Clear Transaction History"):
    gs.clearbudgetdata()
    st.success("Transaction history cleared!")
if st.button("Display Transaction History"):
    try:
        df = pd.read_csv("budget_data.csv")
        st.dataframe(df)
    except FileNotFoundError:
        st.warning("No transaction history found.")

