
import streamlit as st
import pandas as pd
import globalstuff as gs

st.title("Budget Overview")
st.markdown("#### Your current budget snapshot")

budget = float(gs.monthbudget)
expenses = float(gs.monthexpenses)
remaining = budget - (expenses * -1)
percent_spent = 0.0
if budget > 0:
    percent_spent = min(100.0, max(0.0, round(expenses / budget * 100.0, 1)))

col1, col2, col3 = st.columns(3)
col1.metric("Total Budget", f"${budget:,.2f}")
col2.metric("Total Expenses", f"${(expenses*-1):,.2f}")
col3.metric("Remaining Balance", f"${remaining:,.2f}")

st.divider()
st.subheader("Spending progress")
if budget > 0:
    st.progress(percent_spent / 100)
    st.write(f"**{percent_spent}%** of your budget has been spent.")
else:
    st.info("Set a budget first to track your spending progress.")

if remaining < 0:
    st.error("You are over budget. Review your expenses and adjust your plan.")
elif remaining == 0:
    st.warning("Your budget is fully allocated. Keep an eye on new expenses.")
else:
    st.success("Nice work — you still have room left in your budget.")

st.write("---")
st.markdown(
    "Use the Budget Overview page to monitor your monthly plan and make smarter spending decisions. "
    "Add transactions in other pages to keep this summary up to date."
)

