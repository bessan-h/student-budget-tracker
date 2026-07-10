import streamlit as st
import globalstuff as gs

#--Pages--
dashboard_page = st.Page(
    page="views/dashboard.py",
    title="Dashboard",
    icon=":material/dashboard:",
    default=True,
)

analysis_page = st.Page(
    page="views/analy.py",
    title="Analysis",
    icon=":material/analytics:",
)

transaction_history_page = st.Page(
    page="views/transactionhistory.py",
    title="Transaction History",
    icon=":material/history:",
)

budget_page = st.Page(
    page="views/budget.py",    
    title="Budget Overview",
    icon=":material/account_balance_wallet:",
)

#--Navigation--
pgs = st.navigation(pages=[dashboard_page, analysis_page, transaction_history_page, budget_page])

pgs.run()