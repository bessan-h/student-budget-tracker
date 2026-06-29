import altair as alt
import streamlit as st
import pandas as pd
import globalstuff as gs

st.title("Analysis")

try:
    df = pd.read_csv("budget_data.csv", parse_dates=["Timestamp"])
    if df.empty:
        st.write("No transactions have been recorded yet.")
    else:
        df["Amount"] = df["Amount"].astype(float)
        total_income = df[df["Amount"] > 0]["Amount"].sum()
        total_spending = df[df["Amount"] < 0]["Amount"].sum()
        net_total = df["Amount"].sum()

        if "view" not in st.session_state:
            st.session_state.view = "Month"

        st.subheader("Summary Metrics")
        col1, col2, col3 = st.columns(3)
        col1.metric("Total Income", f"${total_income:,.2f}")
        col2.metric("Total Spending", f"-${abs(total_spending):,.2f}")
        col3.metric("Net Total", f"${net_total:,.2f}")

        st.subheader("Spending by Category")
        summary = (
            df.groupby("Category", as_index=False)["Amount"]
            .sum()
            .sort_values(by="Amount", ascending=False)
        )
        summary["Amount"] = summary["Amount"].map(
            lambda value: f"${value:,.2f}" if value >= 0 else f"-${abs(value):,.2f}"
        )
        st.dataframe(summary, use_container_width=True)

        st.subheader("Recent Transactions")
        recent = (
            df.sort_values(by="Timestamp", ascending=False)
            .head(10)
            .reset_index(drop=True)
        )
        recent["Amount"] = recent["Amount"].map(
            lambda value: f"${value:,.2f}" if value >= 0 else f"-${abs(value):,.2f}"
        )
        recent["Timestamp"] = recent["Timestamp"].dt.strftime("%Y-%m-%d %H:%M:%S")
        st.dataframe(recent, use_container_width=True)

        st.subheader("Charts")

        category_chart_data = (
            df.groupby("Category")["Amount"]
            .sum()
            .abs()
            .sort_values(ascending=False)
            .rename_axis("Category")
            .reset_index()
        )
        st.bar_chart(category_chart_data.set_index("Category"))

        # Time window control for the line chart
        view_options = ["Day", "Week", "Month", "Year"]
        selected_view = st.segmented_control(
            "Select Time Window",
            options=view_options,
            default=st.session_state.view,
            label_visibility="collapsed"
        )
        st.session_state.view = selected_view
        st.markdown(f"**Line chart window:** {st.session_state.view}")

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

        balance_chart = alt.Chart(chart_data).mark_line(point=True).encode(
            x=alt.X("Timestamp:T", title="Date"),
            y=alt.Y("Cumulative Balance:Q", title="Total Money"),
            tooltip=["Timestamp:T", "Cumulative Balance:Q"]
        ).properties(
            width=700,
            height=350,
            title=f"Running Balance Over Time ({st.session_state.view} Window)"
        )
        st.altair_chart(balance_chart, use_container_width=True)

        if gs.monthexpenses > 0:
            st.subheader("Expense Breakdown")
            st.pyplot(gs.expensepiechart)
        else:
            st.write("No expenses to analyze yet.")
except FileNotFoundError:
    st.warning("No transaction history found.")