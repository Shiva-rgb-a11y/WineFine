# 🍷 WineFine — Wine Quality Predictor

[![GitHub Stars](https://img.shields.io/github/stars/Shiva-rgb-a11y/WineFine?style=social)](https://github.com/Shiva-rgb-a11y/WineFine)  
🔗 **Live on GitHub**: [https://github.com/Shiva-rgb-a11y/WineFine](https://github.com/Shiva-rgb-a11y/WineFine)


![WineFine Interface](https://raw.githubusercontent.com/Shiva-rgb-a11y/WineFine/main/static/red-wine.avif)




---

## ✨ Overview
**WineFine** is a machine learning-powered web application built with Flask that predicts the **quality score** of red wine based on its physicochemical properties.  
You simply enter features like acidity, alcohol, pH, etc., and it tells you how good your wine is—like a digital sommelier! 🍷

---

## 🚀 Features
- ✅ ML model using **ElasticNet Regression**
- ✅ Data preprocessing & transformation pipeline
- ✅ R2 score evaluation
- ✅ Fully responsive **Flask web app**
- ✅ Stylish red-gold **dark UI** 🍷
- ✅ User-friendly input form with prediction

---

## 🖥️ Tech Stack

| Machine Learning | Web Interface | Utilities | Logging |
|------------------|----------------|-----------|---------|
| Scikit-learn     | Flask           | Pandas, NumPy | Custom logger |
| ElasticNet Model | HTML, CSS, JS   | Joblib, YAML  | File + Stream logs |

---

## 🧪 How It Works

1. Data is read from the CSV file.
2. Column names & data types are validated.
3. Train/test split happens (80/20).
4. Features are scaled using `StandardScaler`.
5. Model is trained using `ElasticNet`.
6. Final model is saved using `joblib`.
7. Flask app accepts user input and makes predictions in real-time.

---

## ✅ How to Run Locally

> Run on your machine using these simple steps:

### 🔁 Step 1: Clone the Repository

```bash
git clone https://github.com/Shiva-rgb-a11y/WineFine.git
cd WineFine

pip install -r requirements.txt

🍷 Responsive, Red-Gold Themed Predictor

