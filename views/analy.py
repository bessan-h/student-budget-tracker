
import streamlit as st
import pandas as pd
import globalstuff as gs

st.title("Analysis")
if gs.monthexpenses > 0:
    st.pyplot(gs.expensepiechart)
