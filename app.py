import streamlit as st
import numpy as np
import pandas as pd
import joblib
import matplotlib.pyplot as plt

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Student Performance Predictor",
    page_icon="🎓",
    layout="wide"
)

# ---------------- LOAD MODEL ----------------
try:
    package = joblib.load("model.pkl")
    model = package["model"]
    FEATURES = package["features"]
except Exception as e:
    st.error(f"Error loading model: {e}")
    st.stop()

# ---------------- HEADER ----------------
st.markdown(
    """
    <div style='text-align:center'>
        <h1>🎓 Student Performance Predictor</h1>
        <p style='font-size:18px;'>
        Predict final student grades using Machine Learning
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

st.divider()

# ---------------- SIDEBAR ----------------
with st.sidebar:
    st.header("📌 Project Information")

    st.write("""
    This project predicts a student's final grade (G3)
    using a Random Forest Machine Learning model.

    ### Features Used
    - First Period Grade (G1)
    - Mid-Year Grade (G2)
    - Study Time
    - Failures
    - Absences
    - Higher Education
    - Internet Access
    - Age
    """)

    st.success("Model: Random Forest Regressor")

# ---------------- METRICS ----------------
m1, m2, m3 = st.columns(3)

with m1:
    st.metric("Model", "Random Forest")

with m2:
    st.metric("Features", len(FEATURES))

with m3:
    st.metric("Target", "Final Grade")

st.divider()

# ---------------- INPUT SECTION ----------------
with st.container(border=True):

    st.subheader("📋 Student Details")

    col1, col2 = st.columns(2)

    with col1:
        G2 = st.slider("Mid-Year Grade (G2)", 0, 20, 10)

        G1 = st.slider("First Period Grade (G1)", 0, 20, 10)

        failures = st.selectbox(
            "Past Class Failures",
            [0, 1, 2, 3]
        )

        studytime = st.selectbox(
            "Weekly Study Time",
            [1, 2, 3, 4],
            format_func=lambda x: {
                1: "< 2 Hours",
                2: "2 - 5 Hours",
                3: "5 - 10 Hours",
                4: "> 10 Hours"
            }[x]
        )

    with col2:
        absences = st.number_input(
            "Number of Absences",
            0,
            90,
            5
        )

        higher = st.selectbox(
            "Wants Higher Education?",
            [1, 0],
            format_func=lambda x: "Yes" if x == 1 else "No"
        )

        internet = st.selectbox(
            "Internet Access at Home?",
            [1, 0],
            format_func=lambda x: "Yes" if x == 1 else "No"
        )

        age = st.slider(
            "Student Age",
            15,
            22,
            17
        )

# ---------------- PREDICTION ----------------
st.divider()

if st.button("🔮 Predict Final Grade", use_container_width=True):

    input_data = np.array([
        [
            G2,
            G1,
            failures,
            studytime,
            absences,
            higher,
            internet,
            age
        ]
    ])

    prediction = model.predict(input_data)[0]
    prediction = round(max(0, min(20, prediction)), 1)

    st.success("Prediction Generated Successfully")

    r1, r2 = st.columns(2)

    with r1:
        st.metric(
            "🎯 Predicted Final Grade",
            f"{prediction}/20"
        )

        percentage = int((prediction / 20) * 100)

        st.metric(
            "📈 Performance Score",
            f"{percentage}%"
        )

        st.progress(prediction / 20)

    with r2:

        if prediction >= 15:
            st.success("🌟 Excellent Performance Predicted")

        elif prediction >= 10:
            st.info("✅ Satisfactory Performance Predicted")

        else:
            st.warning("⚠️ Student May Need Additional Support")

    st.divider()

# ---------------- DATASET INSIGHTS ----------------

with st.expander("📈 Dataset Insights"):

    st.write("""
    Important factors affecting student performance:

    - Previous Grades (G1, G2)
    - Study Time
    - Number of Failures
    - Attendance
    - Access to Resources
    - Educational Aspirations
    """)

# ---------------- FOOTER ----------------

st.divider()

st.markdown(
    """
    <center>
    <h4>🎓 Student Performance Predictor</h4>
    Built by <b>Rushikesh Gaikwad</b><br>
    Synent Technologies Data Science Internship Project
    </center>
    """,
    unsafe_allow_html=True
)
