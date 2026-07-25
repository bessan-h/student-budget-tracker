import altair as alt
import streamlit as st
import pandas as pd
import globalstuff as gs
from styling import apply_custom_styling, render_metric_card, section_divider
from contrast_checker import display_contrast_checker, check_page_contrast

apply_custom_styling()

st.title("📈 Financial Analysis")
st.markdown("**Deep dive into your spending patterns and trends**")

try:
    df = pd.read_csv("budget_data.csv", parse_dates=["Timestamp"])
    if df.empty:
        st.info("📭 No transactions have been recorded yet. Start by adding some transactions in the Dashboard!")
    else:
        df["Amount"] = df["Amount"].astype(float)
        total_income = df[df["Amount"] > 0]["Amount"].sum()
        total_spending = df[df["Amount"] < 0]["Amount"].sum()
        net_total = df["Amount"].sum()

        if "view" not in st.session_state:
            st.session_state.view = "Month"

        st.markdown("---")
        
        section_divider("Summary Metrics")
        col1, col2, col3 = st.columns(3)
        with col1:
            render_metric_card("Total Income", f"${total_income:,.2f}", "📥", "success")
        with col2:
            render_metric_card("Total Spending", f"-${abs(total_spending):,.2f}", "📤", "warning")
        with col3:
            net_style = "success" if net_total >= 0 else "danger"
            render_metric_card("Net Total", f"${net_total:,.2f}", "💰", net_style)

        st.markdown("---")
        
        section_divider("Spending by Category")
        summary = (
            df.groupby("Category", as_index=False)["Amount"]
            .sum()
            .sort_values(by="Amount", ascending=False)
        )
        summary["Amount"] = summary["Amount"].map(
            lambda value: f"${value:,.2f}" if value >= 0 else f"-${abs(value):,.2f}"
        )
        st.dataframe(summary, use_container_width=True, hide_index=True)

        st.markdown("---")
        
        section_divider("Recent Transactions")
        recent = (
            df.sort_values(by="Timestamp", ascending=False)
            .head(10)
            .reset_index(drop=True)
        )
        recent["Amount"] = recent["Amount"].map(
            lambda value: f"${value:,.2f}" if value >= 0 else f"-${abs(value):,.2f}"
        )
        recent["Timestamp"] = recent["Timestamp"].dt.strftime("%Y-%m-%d %H:%M:%S")
        st.dataframe(recent, use_container_width=True, hide_index=True)

        st.markdown("---")
        
        section_divider("Visual Analytics")

        st.markdown("### Category Breakdown")
        category_chart_data = (
            df.groupby("Category")["Amount"]
            .sum()
            .abs()
            .sort_values(ascending=False)
            .rename_axis("Category")
            .reset_index()
        )
        
        # Enhanced bar chart with altair for better styling
        category_chart = alt.Chart(category_chart_data).mark_bar().encode(
            x=alt.X("Amount:Q", title="Amount ($)"),
            y=alt.Y("Category:N", title="", sort="-x"),
            color=alt.value("#6366f1"),
            tooltip=["Category:N", "Amount:Q"]
        ).properties(
            height=300,
            title="Spending by Category"
        )
        st.altair_chart(category_chart, use_container_width=True)

        st.markdown("---")
        
        st.markdown("### Balance Trend")
        # Time window control for the line chart
        col1, col2 = st.columns([3, 1])
        with col1:
            view_options = ["Day", "Week", "Month", "Year"]
            selected_view = st.segmented_control(
                "Select Time Window",
                options=view_options,
                default=st.session_state.view
            )
            st.session_state.view = selected_view

        running_balance = df.sort_values("Timestamp").copy()
        running_balance["Cumulative Balance"] = running_balance["Amount"].cumsum()

        latest_timestamp = running_balance["Timestamp"].max()
        if st.session_state.view == "Day":
            cutoff = latest_timestamp - pd.Timedelta(days=1)
        elif st.session_state.view == "Week":
            cutoff = latest_timestamp - pd.Timedelta(days=7)
        elif st.session_state.view == "Year":
            cutoff = latest_timestamp - pd.Timedelta(days=365)
        else:
            cutoff = latest_timestamp - pd.Timedelta(days=30)

        chart_data = running_balance[running_balance["Timestamp"] >= cutoff]

        balance_chart = alt.Chart(chart_data).mark_line(point=True, strokeWidth=3).encode(
            x=alt.X("Timestamp:T", title="Date"),
            y=alt.Y("Cumulative Balance:Q", title="Balance ($)"),
            color=alt.value("#8b5cf6"),
            tooltip=["Timestamp:T", "Cumulative Balance:Q"]
        ).properties(
            height=400,
            title=f"Running Balance Over Time ({st.session_state.view} Window)"
        )
        st.altair_chart(balance_chart, use_container_width=True)
        gs.loadbudgetdata()
        
except FileNotFoundError:
    st.warning("📭 No transaction history found. Start tracking your budget in the Dashboard!")

st.markdown("---")

# Add contrast checkers
display_contrast_checker()
check_page_contrast()
