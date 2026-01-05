import streamlit as st
import pandas as pd
from src.database import log_intake, get_intake_history
from src.agent import WaterIntakeAgent


st.set_page_config(page_title="AI Water Tracker",layout="wide"
)


st.sidebar.title("Log Your Water Intake")

user_id = st.sidebar.text_input("User ID", placeholder="e.g. user_123")
intake_ml = st.sidebar.number_input(
    "Water Intake (ml)",
    min_value=0,
    step=100
)

submit = st.sidebar.button("Submit")

st.markdown(
    """
    <h1 style='text-align: center;'> 💧AI Water Tracker Dashboard</h1>
    <hr>
    """,
    unsafe_allow_html=True
)


if user_id.strip() == "":
    st.info("Enter your User ID in the sidebar to begin tracking.")
    st.stop()


if submit and intake_ml > 0:
    log_intake(user_id, intake_ml)
    st.success(f" Logged {intake_ml} ml for {user_id}")

history = get_intake_history(user_id)


st.subheader("Water Intake History")

if history:
    df = pd.DataFrame(history, columns=["Water Intake (ml)", "Date"])
    df["Date"] = pd.to_datetime(df["Date"])

    st.dataframe(df, use_container_width=True)

    st.subheader(" Intake Trend")
    chart_df = df.groupby("Date")["Water Intake (ml)"].sum().reset_index()
    st.line_chart(chart_df, x="Date", y="Water Intake (ml)", use_container_width=True)

    st.subheader("AI Hydration Feedback")
    total_intake = df["Water Intake (ml)"].sum()
    agent = WaterIntakeAgent()
    feedback = agent.analyze_intake(total_intake)

    st.markdown(
        f"""
        <div style="
            background-color:#00000;
            padding:20px;
            border-radius:12px;
            border-left:6px solid #0ea5e9;
        ">
        {feedback}
        </div>
        """,
        unsafe_allow_html=True
    )

else:
    st.info("No intake records found. Start logging your water intake")
