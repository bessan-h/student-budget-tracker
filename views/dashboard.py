import streamlit as st
import pandas as pd
import globalstuff as gs
from Subpages.addstuff import add_expense, add_income
st.title("Student Budget Tracker")

# User Input
st.header("Add Transaction")
add_expense()
add_income()



