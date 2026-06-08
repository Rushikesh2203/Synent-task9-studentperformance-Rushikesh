Synent Technologies – Data Science Internship

🎓 Student Performance Predictor

---

📌 Problem Statement

Academic performance is influenced by many factors beyond just study hours ,family background, internet access, past failures, and attendance all play
a role. This project builds a machine learning model that predicts a student's final grade (G3) based on these lifestyle and academic factors,
and deploys it as an interactive web application.

---

📂 Dataset

| Property | Details |
|----------|---------|
| Name | Student Performance Dataset |
| Source | [Kaggle / UCI ML Repository](https://www.kaggle.com/datasets/ucimachinelearning/ict-student-performance-dataset) |
| Size | 395 rows × 33 columns |
| Target Column | G3 (Final Grade, scale 0–20) |

Key Features Used:
- `G1` — First period grade
- `G2` — Second period grade
- `failures` — Number of past class failures
- `studytime` — Weekly study time
- `absences` — Number of school absences
- `higher` — Wants to pursue higher education
- `internet` — Internet access at home
- `age` — Student age

---

🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| Python 3.10 | Core language |
| Pandas | Data manipulation |
| NumPy | Numerical operations |
| Matplotlib / Seaborn | Visualization |
| Scikit-learn | Machine learning |
| Joblib | Model serialization |
| Streamlit | Web app deployment |
| Jupyter Notebook | Development environment |

---

🔄 Project Workflow

```
Data Collection → Data Cleaning → EDA → Model Building → Deployment
```

---

📊 Approach

1. Data Cleaning
- Loaded dataset (semicolon-separated CSV)
- Verified zero missing values
- Checked and removed duplicate rows
- Encoded categorical columns using LabelEncoder
- Confirmed correct data types for all columns

2. Exploratory Data Analysis
- Plotted distribution of final grades (G3)
- Analyzed impact of study time, failures, and absences on grades
- Generated correlation heatmap to identify strongest predictors
- Found G1 and G2 (prior grades) are most correlated with G3

3. Model Building
- Selected top 8 features based on correlation analysis
- Split data: 80% training / 20% testing
- Trained and compared three models:
  - Linear Regression
  - Decision Tree Regressor
  - Random Forest Regressor
- Evaluated using RMSE, MAE, and R² Score

4. Deployment
- Saved best model using Joblib
- Built interactive Streamlit web app
- Deployed on Streamlit Cloud

---

📈 Results

| Model | RMSE | MAE | R² Score |
|-------|------|-----|---------|
| Linear Regression | 1.82 | 1.34 | 0.81 |
| Decision Tree | 2.10 | 1.58 | 0.75 |
| Random Forest | 1.61 | 1.19 | 0.86 |

✅ Random Forest performed best with an R² of 0.86,
meaning it explains 86% of the variance in final grades.

---

## 🔍 Key Insights

1. G1 and G2 are the strongest predictors of G3 (correlation > 0.80)
2. Students with zero past failures** scored significantly higher on average
3. More study time** generally leads to better grades, but shows
   diminishing returns beyond 5 hours/week
4. Higher absences loosely correlate with lower final grades
5. Students who want higher education consistently outperformed others

---

🚀 Live Demo

🔗 [Click here to try the app](https://your-streamlit-url.streamlit.app)

---

▶️ How to Run Locally

```bash
# 1. Clone the repository
git clone https://github.com/YourUsername/synent-task9-studentperformance-rushikesh.git

# 2. Navigate into the folder
cd synent-task9-studentperformance-rushikesh

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the app
streamlit run app.py
```

---

📜 License

This project was built as part of the Synent Technologies
Data Science Internship Program.
