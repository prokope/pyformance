# pyformance
A study performance dashboard

This project is a **personal performance dashboard** that visualizes study statistics such as correct answer rates, daily study time, and most studied subjects — all based on a dataset of exercises completed over time. It is built using **Python (Pandas)** for data processing and **HTML/CSS/JavaScript** for front-end visualization, with **Chart.js** for dynamic graphs.

---

## 🚀 How It Works

1. **Data Collection and Preparation**  
   A dataset is manually or automatically updated with study logs, containing:
   - Date
   - Number of answered, correct, and wrong questions
   - Time spent studying
   - Subject studied

2. **Data Processing (Python)**  
   Using the `pandas` library:
   - Calculates the **percentage of correct answers**
   - Computes the **average daily study time**
   - Aggregates the **most studied subjects by time**
   - Exports a summary to a `.json` file (`dashboard_summary.json`)

3. **Dashboard Rendering (Front-end)**  
   - A fade-in animation is shown on page load for a smoother user experience.
   - After the animation, data from the JSON file is loaded via JavaScript.
   - A Chart.js graph displays the information dynamically.
   - Users can switch between different data views by clicking a button.
   - 
## 📷 Example Screenshots

Here are a few screenshots of the dashboard in action:

![Main Dashboard View](./frontend/assets/most-studied-subjects.png)
![Correct Answers Pie Chart](./frontend/assets/exercises-performance.png)
![Daily Study Average](./frontend/assets/daily-study-average.png)
