import streamlit as st
import pandas as pd
import globalstuff as gs
from styling import apply_custom_styling, section_divider
from contrast_checker import display_contrast_checker, check_page_contrast, apply_current_contrast

apply_custom_styling()
apply_current_contrast()

st.title("📋 Transaction History")
st.markdown("**View and manage all your transactions**")

st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    if st.button("🔍 Display Transaction History", use_container_width=True):
        try:
            df = pd.read_csv("budget_data.csv")
            if not df.empty:
                st.markdown("---")
                section_divider("All Transactions")
                
                # Format the display
                df_display = df.copy()
                df_display["Amount"] = df_display["Amount"].astype(float).apply(lambda x: f"${x:,.2f}" if x >= 0 else f"-${abs(x):,.2f}")
                
                st.dataframe(df_display, use_container_width=True, hide_index=True)
                
                st.markdown("---")
                st.info(f"📊 Total transactions: **{len(df)}**")
            else:
                st.info("📭 No transactions to display.")
        except FileNotFoundError:
            st.warning("📭 No transaction history found.")

with col2:
    if st.button("🗑️ Clear Transaction History", use_container_width=True):
        try:
            gs.clearbudgetdata()
            st.success("✅ Transaction history has been cleared!")
            st.rerun()
        except Exception as e:
            st.error(f"❌ Error clearing history: {str(e)}")

st.markdown("---")

# Additional info section
st.markdown("### 💡 Tips")
st.markdown("""
- **View History**: Click the button above to see all recorded transactions
- **Clear Data**: Use the clear button to reset all transaction history (cannot be undone)
- **Export Data**: You can download the CSV file directly from your file system
- **Date Format**: All timestamps are recorded in YYYY-MM-DD HH:MM:SS format
""")

st.markdown("---")

# Add contrast checkers
display_contrast_checker()
check_page_contrast()


