import streamlit as st
import pandas as pd
import requests
import os


# Backend Configuration
BACKEND_URL = os.getenv(
    "BACKEND_URL",
    "https://ai-water-intake-tracker-agent-1.onrender.com"
)


# Page Config
st.set_page_config(
    page_title="AI Water Tracker",
    layout="wide"
)


# Sidebar Input
st.sidebar.title("Log Your Water Intake")

user_id = st.sidebar.text_input("User ID", placeholder="e.g. user_123")
intake_ml = st.sidebar.number_input(
    "Water Intake (ml)",
    min_value=0,
    step=100
)

submit = st.sidebar.button("Submit")


# Main Header
st.markdown(
    """
    <h1 style='text-align: center;'> 💧AI Water Tracker Dashboard</h1>
    <hr>
    """,
    unsafe_allow_html=True
)


# Validation
if user_id.strip() == "":
    st.info("Enter your User ID in the sidebar to begin tracking.")
    st.stop()


# Log Intake (API Call)
if submit and intake_ml > 0:
    response = requests.post(
        f"{BACKEND_URL}/log_intake/",
        json={
            "user_id": user_id,
            "intake_ml": intake_ml
        }
    )

    if response.status_code == 200:
        st.success(f" Logged {intake_ml} ml for {user_id}")
        ai_feedback = response.json().get("analysis", "")
    else:
        st.error("Failed to log intake. Please try again.")
        st.stop()
else:
    ai_feedback = ""


# Fetch History (API Call)
history_response = requests.get(
    f"{BACKEND_URL}/history/{user_id}"
)

history = history_response.json().get("history", [])


# History Section
st.subheader("Water Intake History")

if history:
    df = pd.DataFrame(history, columns=["Water Intake (ml)", "Date"])
    df["Date"] = pd.to_datetime(df["Date"])

    st.dataframe(df, use_container_width=True)

    # Intake Trend Chart
    st.subheader(" Intake Trend")
    chart_df = df.groupby("Date")["Water Intake (ml)"].sum().reset_index()
    st.line_chart(
        chart_df,
        x="Date",
        y="Water Intake (ml)",
        use_container_width=True
    )


    # AI Feedback Section
    if ai_feedback:
        st.subheader("AI Hydration Feedback")

        st.markdown(
            f"""
            <div style="
                background-color:#0f172a;
                color:white;
                padding:20px;
                border-radius:12px;
                border-left:6px solid #0ea5e9;
            ">
            {ai_feedback}
            </div>
            """,
            unsafe_allow_html=True
        )

else:
    st.info("No intake records found. Start logging your water intake.")
