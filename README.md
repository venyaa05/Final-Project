<div align="center">

<img src="titanic_readme_assets/titanic-banner.gif" width="100%" alt="Animated Titanic Survival Analysis banner">

<br>

<h2>💗🚢 Titanic Survival Analysis 🚢💛</h2>

<p><b>✨ Track • Analyze • Visualize ✨</b></p>

<p>
  <img src="https://img.shields.io/badge/PYTHON-FFD447?style=for-the-badge&logo=python&logoColor=306998">
  <img src="https://img.shields.io/badge/PANDAS-FF69B4?style=for-the-badge&logo=pandas&logoColor=FFFFFF">
  <img src="https://img.shields.io/badge/MATPLOTLIB-FFD447?style=for-the-badge&logo=matplotlib&logoColor=FFFFFF">
  <img src="https://img.shields.io/badge/SEABORN-E95A9B?style=for-the-badge&logoColor=FFFFFF">
</p>

<p><i>Turn passenger data into clear survival insights 📊</i></p>

</div>

---

# 💗 01 — PROJECT OVERVIEW

<div align="center">

### 🚢 Titanic Survival Analysis

A beginner-friendly data analysis project using **Python, Pandas, Matplotlib and Seaborn** to inspect the Titanic dataset, handle missing values, calculate survival statistics, and visualize important patterns.

</div>

---

# 💛 02 — WHAT THIS PROJECT DOES

| 🔎 Feature | 💡 Description |
|:---|:---|
| 📂 Data Loading | Loads the Titanic CSV dataset using Pandas |
| 👀 Data Inspection | Displays rows, data types and dataset information |
| 🧹 Data Cleaning | Handles missing `Age` and `Embarked` values |
| 💗 Survival Analysis | Calculates survival counts and overall survival rate |
| 👩 Gender Analysis | Compares survival rates by gender |
| 🎫 Class Analysis | Compares survival rates by passenger class |
| 🎂 Age Analysis | Visualizes passenger age distribution |
| 🔥 Correlation | Examines relationships among numerical variables |
| 📊 Visualization | Creates five analytical charts |

---

# 🌸 03 — DATASET SNAPSHOT

| 📌 Item | Value |
|:---|---:|
| 👥 Passenger Records | **891** |
| 🧾 Columns | **12** |
| 🎯 Target Variable | `Survived` |
| 👤 Passenger ID | `PassengerId` |
| 🎫 Passenger Class | `Pclass` |
| 🚻 Gender | `Sex` |
| 🎂 Age | `Age` |
| 👨‍👩‍👧 Family Variables | `SibSp`, `Parch` |
| 💰 Fare | `Fare` |
| 🚢 Embarkation | `Embarked` |
| 🛏️ Cabin | `Cabin` |

---

# 💗 04 — DATA CLEANING

Missing values were checked before the main analysis.

```python
df["Age"] = df["Age"].fillna(df["Age"].median())
df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])
```

| Column | Missing Values |
|:---|---:|
| 🎂 `Age` | **177** |
| 🛏️ `Cabin` | **687** |
| 🚢 `Embarked` | **2** |
| ✅ Other columns | **0** |

> 💡 `Age` is filled using the median, while `Embarked` is filled using the mode.

---

# 💛 05 — KEY RESULTS

## 🚢 Overall Survival

| Outcome | Passengers |
|:---|---:|
| ❌ Did Not Survive | **549** |
| 💗 Survived | **342** |

### ✨ Overall Survival Rate: **38.38%**

---

## 👩 Survival by Gender

| Gender | Survival Rate |
|:---|---:|
| 👩 Female | **74.20%** |
| 👨 Male | **18.89%** |

---

## 🎫 Survival by Passenger Class

| Passenger Class | Survival Rate |
|:---|---:|
| 🥇 1st Class | **62.96%** |
| 🥈 2nd Class | **47.28%** |
| 🥉 3rd Class | **24.24%** |

---

# 📊 06 — VISUALIZATIONS

<div align="center">

### 🚢 Titanic Survival
<img src="titanic_readme_assets/titanic-survival.png" width="72%">

### 👩 Survival by Gender
<img src="titanic_readme_assets/survival-by-gender.png" width="72%">

### 🎫 Survival by Class
<img src="titanic_readme_assets/survival-by-class.png" width="72%">

### 🎂 Age Distribution
<img src="titanic_readme_assets/age-distribution.png" width="72%">

### 🔥 Correlation Heatmap
<img src="titanic_readme_assets/correlation-heatmap.png" width="72%">

</div>

---

# 🔥 07 — CORRELATION HIGHLIGHTS

| Variables | Correlation |
|:---|---:|
| `Pclass` ↔ `Fare` | **-0.55** |
| `SibSp` ↔ `Parch` | **0.41** |
| `Survived` ↔ `Fare` | **0.26** |
| `Survived` ↔ `Pclass` | **-0.34** |
| `Age` ↔ `Pclass` | **-0.34** |

> 📌 The heatmap helps identify positive and negative relationships among numerical variables.

---

# 🌷 08 — TECHNOLOGIES USED

| Technology | Purpose |
|:---|:---|
| 🐍 **Python** | Main programming language |
| 🐼 **Pandas** | Data loading, cleaning and analysis |
| 📊 **Matplotlib** | Plot generation |
| 🌊 **Seaborn** | Statistical visualizations |
| 📄 **CSV** | Dataset format |

---

# ⚙️ 09 — HOW TO RUN

### 1️⃣ Install dependencies

```bash
pip install pandas matplotlib seaborn
```

### 2️⃣ Keep these files together

```text
📁 Titanic-Survival-Analysis
│
├── 🐍 10.Final project.py
├── 📄 Titanic-Dataset.csv
├── 📁 titanic_readme_assets
│   ├── 🎞️ titanic-banner.gif
│   ├── 🖼️ titanic-survival.png
│   ├── 🖼️ survival-by-gender.png
│   ├── 🖼️ survival-by-class.png
│   ├── 🖼️ age-distribution.png
│   └── 🖼️ correlation-heatmap.png
│
└── 📘 README.md
```

### 3️⃣ Run the project

```bash
python "10.Final project.py"
```

---

# 💕 10 — PROJECT WORKFLOW

<div align="center">

**📄 CSV DATA**

⬇️

**📥 LOAD DATA**

⬇️

**🔍 INSPECT**

⬇️

**🧹 CLEAN**

⬇️

**📊 ANALYZE**

⬇️

**📈 VISUALIZE**

⬇️

**💡 INTERPRET**

</div>

---

# 🌟 11 — PROJECT HIGHLIGHTS

| ⭐ Metric | Result |
|:---|:---|
| 👥 Dataset Size | **891 passengers** |
| 💗 Overall Survival | **38.38%** |
| 👩 Highest Gender Survival | **Female — 74.20%** |
| 🎫 Highest Class Survival | **1st Class — 62.96%** |
| 🔥 Strongest Listed Correlation | **Pclass ↔ Fare — -0.55** |
| 📊 Charts Created | **5** |

---

# 🌸 12 — CONCLUSION

This project demonstrates a complete beginner-friendly data analysis pipeline:

### **Load → Inspect → Clean → Analyze → Visualize → Interpret**

The analysis shows clear differences in survival across **gender** and **passenger class**, while the charts make those patterns easier to understand.

---

<div align="center">

### 💗 Made with Python • Pandas • Matplotlib • Seaborn 💛

🚢✨ **Data tells the story. Visualization makes it visible.** ✨🚢

</div>
