# 🔁 E-Learning Platform Analysis Project

[![Python Version](https://img.shields.io/badge/python-3.11%2B-blue.svg)](https://www.python.org/)
[![GitHub forks](https://img.shields.io/github/forks/zufran123/e-learning-analysis?style=flat)](https://github.com/zufran123/e-learning-analysis/network/members)
[![GitHub stars](https://img.shields.io/github/stars/zufran123/e-learning-analysis?style=flat)](https://github.com/zufran123/e-learning-analysis/stargazers)
[![GitHub last commit](https://img.shields.io/github/last-commit/zufran123/e-learning-analysis?style=flat)](https://github.com/zufran123/e-learning-analysis/commits)
[![Data Source](https://img.shields.io/badge/Data-Kaggle-blue?style=flat)](https://www.kaggle.com/)
![visitors](https://visitor-badge.laobi.icu/badge?page_id=zufran123.e-learning-analysis)


---

This **E-Learning Platform Analysis Project** is a comprehensive data-driven solution that provides detailed insights into user engagement, feedback, course popularity, and platform usage using Python and SQLite. It mimics a real-world education analytics pipeline that can be used by ed-tech platforms or academic institutions to evaluate user activity, identify top-performing courses, and generate automated PDF reports for stakeholders.

Built using Python and core data libraries like `pandas`, `matplotlib`, and `FPDF`, the project integrates SQL-based data extraction, modular scripts for analytics, and auto-generated visual reports — all optimized for clarity and reproducibility. The SQLite database (`e_learning.db`) holds structured user interaction data such as enrollments, feedback, watch history, and course info.

It features robust automation that:
- Executes SQL queries to extract insights
- Generates bar plots and charts of course/user engagement
- Converts metrics into downloadable PDF reports

This project showcases the power of **data analytics + reporting** in ed-tech, providing real-time actionable feedback for platform optimization and decision-making.

---

## ⚠️ Challenges Faced

- Designing modular and reusable Python scripts for analytics and reporting.
- Structuring and querying relational data efficiently in SQLite.
- Automating multi-step processes like DB connection, querying, charting, and PDF generation.
- Managing compatibility between Python, SQLite drivers, and FPDF.
- Handling cases of missing feedback, zero-enrollment users, and course duplication.

---

## ⚖️ Data Considerations

- Dataset includes platform activity simulations: users, enrollments, feedback, and watch history.
- All tables are joined using appropriate keys and filtered to ensure data consistency.
- Feedback normalization and enrollment merging were handled during analysis to ensure accurate KPIs.

---

## 🚀 Future Improvements

- Add Streamlit-based dashboard for real-time interactive insights.
- Integrate advanced SQL views and stored procedures.
- Implement admin-level analytics and alerts for underperforming courses.
- Add authentication and file storage for user-specific PDF access.
- Connect to a cloud database (PostgreSQL/Azure SQL) for deployment-ready version.

---

## 📋 Project Management

This project was developed with a structured modular approach involving:

- Python scripts for clean data analysis & reporting  
- SQL for querying structured data  
- GitHub for version control and sharing  
- PDF reports for professional data presentation

---

## 📊 Project Overview

- **Objective:** Analyze learner engagement and generate reports for an online learning platform.
- **Domain:** EdTech / Education Analytics
- **Problem Type:** Exploratory & Descriptive Analytics
- **Key Metrics Analyzed:** User feedback, enrollments, watch history, top courses, user roles

---

## 🧰 Tools & Technologies

- **Language:** Python 3.11+
- **Libraries Used:**
  - pandas
  - sqlite3
  - matplotlib
  - fpdf
  - os / shutil

---

## 📁 Project Structure

```
e-learning-platform-analysis-final/
├── data/
│   └── elearning_platform_data.csv       # Raw data (optional)
├── src/
│   ├── connect_db.py                     # Database connection handler
│   ├── query_runner.py                   # SQL execution and data fetching
│   ├── analysis.py                       # Core data analysis logic
│   ├── pdf_report.py                     # PDF report generator using FPDF
│   └── main.py                           # Main orchestrator script
├── visualizations/
│   ├── course_enrollment.png             # Bar chart of course enrollments
│   ├── user_roles.png                    # Pie chart of user roles
│   └── elearning_report.pdf              # Auto-generated summary report
├── e_learning.db                         # SQLite database (with schema & data)
├── requirements.txt                      # Python dependencies
├── README.md                             # Project documentation
└── .gitignore
```

---

## 🔍 Key Features

- 📊 SQL-driven database analytics with custom queries  
- ✅ Automated PDF report generation using FPDF  
- 📄 Modular scripts for separation of concerns  
- 📉 Matplotlib-based visual insights  
- 💡 Ready for scaling with Streamlit or cloud integration

---

## 📈 Visualizations Included

- 📌 Course-wise enrollment bar plot  
- 📌 User roles distribution pie chart  
- 📌 Feedback and ratings aggregation  
- 📌 Optional custom queries for deeper analysis

---

## 🚀 How to Run the Project

### 1. Clone the Repository:

```bash
git clone https://github.com/zufran123/e-learning-platform-analysis.git
cd e-learning-platform-analysis
```

### 2. Create Virtual Environment:

```bash
python -m venv venv
venv\Scripts\activate   # For Windows
```

### 3. Install Dependencies:

```bash
pip install -r requirements.txt
```

### 4. Run the Project:

```bash
python src/main.py
```

> This will run the full flow: connect DB → run analysis → generate visualizations → export PDF.

---

## 📂 Database Schema

The SQLite database `e_learning.db` contains:

- `users` — Basic user info  
- `courses` — Course catalog  
- `enrollments` — Enrolled users per course  
- `feedback` — Course-wise ratings and reviews  
- `watch_history` — User activity timestamps  

> You can modify or extend the schema using the `src/connect_db.py` file and corresponding `.sql` files if needed.

---

## 📈 Future Add-ons

- Add dashboards with Streamlit or Power BI  
- Generate per-user reports dynamically  
- Schedule automatic report generation weekly/monthly  
- Add GitHub Actions for automation

---

## 🙌 Acknowledgements

- Built as part of a portfolio-ready analytics suite for educational data.  
- Inspired by real-world use cases in ed-tech and LMS platforms.

---

## 👨‍💻 Author

**Mohd Zufran**  
[![LinkedIn: mohdzufran](https://img.shields.io/badge/LinkedIn-mohdzufran-blue?style=flat-square&logo=linkedin)](https://linkedin.com/in/mohdzufran)

---

## 📄 License

This Open Source Software is licensed under the **MIT License**.  
Please give proper credit by including the license and attributing the original author.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

