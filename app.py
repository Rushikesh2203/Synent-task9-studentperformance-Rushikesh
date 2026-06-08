# app.py
import streamlit as st
import numpy as np
import pickle

# Load the saved model
model = pickle.load(open('model.pkl', 'rb'))

st.set_page_config(page_title="Student Grade Predictor", page_icon="🎓")
st.title("🎓 Student Final Grade Predictor")
st.write("Fill in the student details below to predict their final grade (G3).")

st.divider()

# ── User Inputs ──────────────────────────────────────
col1, col2 = st.columns(2)

with col1:
    G2 = st.slider("Mid-Year Grade (G2)", 0, 20, 10)
    G1 = st.slider("First Period Grade (G1)", 0, 20, 10)
    failures = st.selectbox("Past Class Failures", [0, 1, 2, 3])
    studytime = st.selectbox("Weekly Study Time",
                             [1, 2, 3, 4],
                             format_func=lambda x: {
                                 1: "< 2 hours",
                                 2: "2–5 hours",
                                 3: "5–10 hours",
                                 4: "> 10 hours"
                             }[x])

with col2:
    absences = st.number_input("Number of Absences", 0, 90, 5)
    higher = st.selectbox("Wants Higher Education?", [1, 0],
                          format_func=lambda x: "Yes" if x == 1 else "No")
    internet = st.selectbox("Internet Access at Home?", [1, 0],
                            format_func=lambda x: "Yes" if x == 1 else "No")
    age = st.slider("Student Age", 15, 22, 17)

st.divider()

# ── Predict ──────────────────────────────────────────
if st.button("🔮 Predict Final Grade", use_container_width=True):
    input_data = np.array([[G2, G1, failures, studytime,
                            absences, higher, internet, age]])
    
    prediction = model.predict(input_data)[0]
    prediction = round(max(0, min(20, prediction)), 1)  # Clamp between 0–20
    
    st.success(f"📊 Predicted Final Grade: **{prediction} / 20**")
    
    if prediction >= 15:
        st.info("🌟 Excellent performance predicted!")
    elif prediction >= 10:
        st.info("✅ Satisfactory performance predicted.")
    else:
        st.warning("⚠️ Student may need additional support.")