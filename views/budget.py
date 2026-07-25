import streamlit as st
import pandas as pd
import globalstuff as gs
from styling import apply_custom_styling, render_metric_card, section_divider
from contrast_checker import display_contrast_checker, check_page_contrast

apply_custom_styling()

st.title("💼 Budget Overview")
st.markdown("**Track your spending and stay within budget**")

budget = float(gs.monthbudget)
expenses = float(gs.monthexpenses)
remaining = budget - (expenses * -1)
percent_spent = 0.0
if budget > 0:
    percent_spent = min(100.0, max(0.0, round((-1*expenses) / budget * 100.0, 1)))

st.markdown("---")

# Display metrics in styled cards
col1, col2, col3 = st.columns(3)

with col1:
    render_metric_card("Total Budget", f"${budget:,.2f}", "💵", "primary")

with col2:
    render_metric_card("Total Expenses", f"${(expenses*-1):,.2f}", "📊", "warning")

with col3:
    render_metric_card("Remaining Balance", f"${remaining:,.2f}", "✅" if remaining > 0 else "⚠️", 
                       "success" if remaining > 0 else "danger")

st.markdown("---")

section_divider("Spending Progress")
if budget > 0:
    st.progress(percent_spent / 100)
    
    # Progress info with styling
    progress_text = f"**{percent_spent}%** of your budget has been spent"
    if percent_spent < 50:
        st.success(f"🟢 {progress_text} — Great job staying under control!")
    elif percent_spent < 80:
        st.info(f"🟡 {progress_text} — Keep monitoring your spending.")
    else:
        st.warning(f"🟠 {progress_text} — Getting close to your limit!")
else:
    st.info("📌 Set a budget first to track your spending progress.")

st.markdown("---")

section_divider("Budget Status")
if remaining < 0:
    st.error(f"🔴 **Over Budget** — You've exceeded your budget by ${abs(remaining):,.2f}. Review your expenses and adjust your plan.")
elif remaining == 0:
    st.warning(f"🟡 **Fully Allocated** — Your budget is fully allocated. Keep an eye on new expenses.")
else:
    st.success(f"🟢 **On Track** — You still have **${remaining:,.2f}** left in your budget. Nice work!")

st.markdown("---")

# Add contrast checkers
display_contrast_checker()
check_page_contrast()


