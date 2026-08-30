<div align="center">

<img src="titanic_readme_assets/titanic-banner.gif" width="100%" alt="Titanic Survival Analysis">

<br><br>

# TITANIC SURVIVAL ANALYSIS

### Track • Analyze • Visualize

<p>
<img src="https://img.shields.io/badge/PYTHON-FFD447?style=for-the-badge&logo=python&logoColor=306998">
<img src="https://img.shields.io/badge/PANDAS-E06AA8?style=for-the-badge&logo=pandas&logoColor=FFFFFF">
<img src="https://img.shields.io/badge/MATPLOTLIB-FFD447?style=for-the-badge&logo=matplotlib&logoColor=FFFFFF">
<img src="https://img.shields.io/badge/SEABORN-D45D91?style=for-the-badge&logoColor=FFFFFF">
</p>

<p><i>Turn passenger data into clear survival insights</i></p>

</div>

---

# 01 — PROJECT OVERVIEW

This project performs a Titanic dataset analysis using Python, Pandas, Matplotlib and Seaborn.

The workflow covers data inspection, missing-value handling, survival-rate calculations, comparative analysis and data visualization.

---

# 02 — WHAT THIS PROJECT DOES

| Feature | Description |
|:---|:---|
| Data Loading | Loads the Titanic CSV dataset using Pandas |
| Data Inspection | Displays the first rows and dataset information |
| Missing Values | Checks and handles missing values |
| Survival Count | Calculates survivor and non-survivor totals |
| Gender Analysis | Compares survival rates by gender |
| Class Analysis | Compares survival rates by passenger class |
| Age Distribution | Visualizes passenger ages |
| Correlation | Displays numerical correlations |
| Visualization | Creates five analytical charts |

---

# 03 — DATASET SNAPSHOT

| Item | Value |
|:---|---:|
| Passenger Records | 891 |
| Columns | 12 |
| Target Variable | `Survived` |
| Passenger ID | `PassengerId` |
| Passenger Class | `Pclass` |
| Gender | `Sex` |
| Age | `Age` |
| Family Variables | `SibSp`, `Parch` |
| Fare | `Fare` |
| Embarkation | `Embarked` |
| Cabin | `Cabin` |

---

# 04 — DATA CLEANING

Missing values are checked before analysis.

```python
df["Age"] = df["Age"].fillna(df["Age"].median())
df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])
```

| Column | Missing Values |
|:---|---:|
| `Age` | 177 |
| `Cabin` | 687 |
| `Embarked` | 2 |
| Other columns | 0 |

---

# 05 — KEY RESULTS

## Overall Survival

| Outcome | Passengers |
|:---|---:|
| Did Not Survive | 549 |
| Survived | 342 |

### Overall Survival Rate: 38.38%

## Survival by Gender

| Gender | Survival Rate |
|:---|---:|
| Female | 74.20% |
| Male | 18.89% |

## Survival by Passenger Class

| Passenger Class | Survival Rate |
|:---|---:|
| 1st Class | 62.96% |
| 2nd Class | 47.28% |
| 3rd Class | 24.24% |

---

# 06 — VISUALIZATIONS

<div align="center">

### Titanic Survival

<img src="titanic_readme_assets/titanic-survival.png" width="75%">

### Survival by Gender

<img src="titanic_readme_assets/survival-by-gender.png" width="75%">

### Survival by Class

<img src="titanic_readme_assets/survival-by-class.png" width="75%">

### Age Distribution

<img src="titanic_readme_assets/age-distribution.png" width="75%">

### Correlation Heatmap

<img src="titanic_readme_assets/correlation-heatmap.png" width="75%">

</div>

---

# 07 — CORRELATION HIGHLIGHTS

| Variables | Correlation |
|:---|---:|
| `Pclass` and `Fare` | -0.55 |
| `SibSp` and `Parch` | 0.41 |
| `Survived` and `Fare` | 0.26 |
| `Survived` and `Pclass` | -0.34 |
| `Age` and `Pclass` | -0.34 |

---

# 08 — TECHNOLOGIES USED

| Technology | Purpose |
|:---|:---|
| Python | Main programming language |
| Pandas | Data loading, cleaning and analysis |
| Matplotlib | Plot generation |
| Seaborn | Statistical visualization |
| CSV | Dataset format |

---

# 09 — HOW TO RUN

### Install dependencies

```bash
pip install pandas matplotlib seaborn
```

### Project structure

```text
Titanic-Survival-Analysis/
|
|-- 10.Final project.py
|-- Titanic-Dataset.csv
|-- README.md
|
`-- titanic_readme_assets/
    |-- titanic-banner.gif
    |-- titanic-survival.png
    |-- survival-by-gender.png
    |-- survival-by-class.png
    |-- age-distribution.png
    `-- correlation-heatmap.png
```

### Run

```bash
python "10.Final project.py"
```

---

# 10 — PROJECT WORKFLOW

<div align="center">

**LOAD DATA**

↓

**INSPECT DATA**

↓

**CLEAN DATA**

↓

**ANALYZE**

↓

**VISUALIZE**

↓

**INTERPRET**

</div>

---

# 11 — PROJECT HIGHLIGHTS

| Metric | Result |
|:---|:---|
| Dataset Size | 891 passengers |
| Overall Survival | 38.38% |
| Highest Gender Survival | Female — 74.20% |
| Highest Class Survival | 1st Class — 62.96% |
| Strongest Listed Correlation | Pclass and Fare — -0.55 |
| Charts Created | 5 |

---

# 12 — CONCLUSION

This project demonstrates a complete data-analysis workflow:

**Load → Inspect → Clean → Analyze → Visualize → Interpret**

The results show clear differences in passenger survival across gender and passenger class, supported by numerical analysis and visualizations.

---

<div align="center">

### TITANIC SURVIVAL ANALYSIS

**Python • Pandas • Matplotlib • Seaborn**

</div>
