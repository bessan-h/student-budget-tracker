
import streamlit as st
import pandas as pd
import globalstuff as gs
st.title("Budget Overview")

st.write(f"Total Budget: ${gs.monthbudget}")
st.write(f"Total Expenses: ${gs.monthexpenses}")
st.write(f"Remaining Balance: ${gs.monthbudget - gs.monthexpenses}")

