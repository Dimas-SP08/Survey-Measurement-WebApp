# AI-Powered Survey Measurement Web App

**Developed by: Dimas S.P.** *(Vocational High School Student – Modeling Design & Building Information)*

---

[![Python Version](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](https://python.org)
[![Streamlit Version](https://img.shields.io/badge/Streamlit-1.49-ff4b4b.svg)](https://streamlit.io)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A modern, intelligent web application designed to process, analyze, and visualize land survey data. This tool leverages the **Google Gemini API** to provide AI-powered data validation and automated professional report generation, bridging the gap between raw field data and actionable insights.

---

### Project Evolution

This web application is a modern reimagining of a desktop application I previously built. The project was developed to master modern web technologies like Streamlit and to explore the practical applications of Artificial Intelligence in the civil engineering domain.

**To see the development journey from a command-line tool (v1.0) to a full-featured desktop application (v4.0), you can visit the predecessor repository here: [Survey-Measurement-Desktop](https://github.com/Dimas-SP08/Land-Measurement-code)**

---

## Key Features

-   **Interactive Web Interface**: Built with **Streamlit** for a seamless and intuitive user experience accessible from any web browser.
-   **Automated Survey Calculations**: Automatically computes essential metrics like elevation, height difference, and survey point status (RISE/FALL/FLAT), eliminating manual errors.
-   **🤖 Gemini AI Integration**:
    -   **Anomaly Detection**: Intelligently scans measurement data to identify potential errors or inconsistencies, ensuring higher data accuracy.
    -   **Automated Report Generation**: Generates comprehensive, professional-grade survey reports with a single click, summarizing findings and analyses.
-   **Dynamic Data Visualization**: Features interactive charts and plots for elevation profiles, height differences, and distance vs. elevation distributions, making complex data easy to understand.
-   **Professional Export Options**:
    -   Download AI-generated analysis reports in **Microsoft Word (.docx)** format.
    -   Export complete data tables and embedded graphs to **Microsoft Excel (.xlsx)**.
    -   Save individual plots and charts as high-quality **PNG** images.

---

## Application Workflow

### Step 1: Start Survey
Click the **"Start Survey Now"** button to begin.
![Step 1](Land_Measurement_WebApp/Image/_1_start.png)

---

### Step 2: Input Initial Parameters
Enter the number of measurement points, initial elevation (AMSL), and the purpose of the survey.
![Step 2](Land_Measurement_WebApp/Image/_2_data_init.png)

---

### Step 3: Input Measurement Data
Fill in the top, middle, and bottom thread data, as well as the distance between points.
![Step 3](Land_Measurement_WebApp/Image/_3_input_thread.png)

---

### Step 4: AI-Powered Anomaly Analysis
Use Gemini AI to review your data and detect potential anomalies.
![Step 4](Land_Measurement_WebApp/Image/_4_Analyze_anomalies.png)

---

### Step 5: View Table & Chart Results
Check the calculation results in a clean table and interactive graph visualizations.
![Step 6 & 7](Land_Measurement_WebApp/Image/_6_table.png)

---

### Step 6: Generate AI Report
Create a professional survey summary and report with a single click using the power of AI.
![Step 8](Land_Measurement_WebApp/Image/_8_ai_report.png)
---

## Technology Stack
-   **Backend**: Python
-   **Web Framework**: Streamlit
-   **Data Manipulation**: Pandas
-   **Data Visualization**: Matplotlib
-   **AI & Machine Learning**: Google Gemini API
-   **File Handling**: openpyxl (Excel), python-docx (Word), Pillow (Images)

---

## Installation & Local Execution

To run this application on your local machine, follow these steps:

**1. Clone the Repository**
```bash
git clone [https://github.com/Dimas-SP08/Survey-Measurement-WebApp.git](https://github.com/Dimas-SP08/Survey-Measurement-WebApp.git)
cd Survey-Measurement-WebApp
